"""SecureCollab's Phase 2 request path (VULNERABLE), as a local fixture.

A FastAPI origin sits behind a simulated TLS-terminating edge. The edge's
own job -- proving the browser-to-edge hop with TLS 1.3 -- is not modeled
here at all, on purpose: this fixture starts *after* TLS has already
terminated, exactly where the two questions this module teaches actually
live. `SECURITY.md` names the forbidden outcomes; do not "fix" this file
in place -- see `fixed/app.py` for the structural repair and `../README.md`
for how to run both.

Two independent defects live here:

1. `_resolve_company` (C2): a client-supplied `X-Company` header overrides
   the company the caller's own API key is bound to. TLS terminating at
   the edge authenticates the browser-to-edge hop; it says nothing at all
   about who set which HTTP header on the request that follows, so an
   origin that reads company identity from a header is handing out
   authorization to whatever a caller claims.

2. `_CACHE` (C1): the shared cache is keyed on the request path alone. A
   cache entry filled while resolving company A's request answers company
   B's later request for the same path, because the key never recorded
   which company filled the slot.

A third fixture, `hop_is_trustworthy` (C3), is not a break in the request
path above -- it is a separate, colocated check for a related but distinct
question this module also teaches: whether a TLS hop's *peer* is the peer
a policy intended, not merely whether *some* certificate chained to a
trusted CA. It is exposed at `POST /internal/relay` so it is exercised the
same way as everything else in this fixture: through a real request and
response, not a bare function call.
"""

from __future__ import annotations

from fastapi import FastAPI, Header, HTTPException, Request

# Server-side truth: which API key belongs to which company. A caller never
# gets to state which company they are; the origin looks it up from a
# credential only the origin issued.
API_KEYS: dict[str, str] = {
    "key-A": "companyA",
    "key-B": "companyB",
    "key-Z": "companyZ",
    "key-Q": "companyQ",
}

_ORIGIN_STORE: dict[tuple[str, str], str] = {}
_CACHE: dict[str, str] = {}  # VULNERABLE: keyed on note_id (path) only

_ACCEPTED_TLS_VERSIONS = {"1.2", "1.3"}


def reset() -> None:
    """Called by the test fixture before every test; there is no
    persistent state between tests or between mental experiments."""
    _ORIGIN_STORE.clear()
    _CACHE.clear()


def _bearer(authorization: str | None) -> str | None:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    return authorization[len("Bearer "):]


def _resolve_company(api_key: str | None, x_company: str | None) -> str | None:
    """VULNERABLE: a client-supplied X-Company header, if present,
    overrides the company the caller's own credential is bound to."""
    if api_key not in API_KEYS:
        return None
    if x_company:
        return x_company
    return API_KEYS[api_key]


def hop_is_trustworthy(
    expected_hostname: str,
    presented_hostname: str,
    cert_trusted_ca: bool | None,
    tls_version: str,
) -> bool:
    """VULNERABLE: treats "the certificate chains to a trusted CA" as the
    whole property -- the exact "TLS is on" fallacy this module names as a
    misconception. It never compares the certificate's hostname to the
    hostname this hop actually meant to reach, and never checks the
    negotiated protocol version at all."""
    return cert_trusted_ca is True


def create_app() -> FastAPI:
    app = FastAPI()

    @app.put("/notes/{note_id}")
    def put_note(
        note_id: str,
        payload: dict,
        authorization: str | None = Header(default=None),
    ) -> dict:
        api_key = _bearer(authorization)
        company = _resolve_company(api_key, None)
        if company is None:
            raise HTTPException(status_code=401, detail="unknown api key")
        _ORIGIN_STORE[(note_id, company)] = str(payload.get("body", ""))
        return {"stored": True}

    @app.get("/notes/{note_id}")
    def get_note(
        note_id: str,
        authorization: str | None = Header(default=None),
        x_company: str | None = Header(default=None, alias="X-Company"),
    ) -> dict:
        api_key = _bearer(authorization)
        company = _resolve_company(api_key, x_company)
        if company is None:
            raise HTTPException(status_code=401, detail="unknown api key")
        cached = _CACHE.get(note_id)
        if cached is not None:
            return {"body": cached, "source": "cache"}
        text = _ORIGIN_STORE.get((note_id, company))
        if text is None:
            raise HTTPException(status_code=404, detail="not found")
        _CACHE[note_id] = text
        return {"body": text, "source": "origin"}

    @app.post("/internal/relay")
    def relay(payload: dict, request: Request) -> dict:
        trustworthy = hop_is_trustworthy(
            payload["expected_hostname"],
            payload["presented_hostname"],
            payload.get("cert_trusted_ca"),
            payload["tls_version"],
        )
        if not trustworthy:
            raise HTTPException(status_code=502, detail="upstream hop not trustworthy")
        return {"relayed": True}

    return app
