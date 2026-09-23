"""SecureCollab's Phase 2 request path (FIXED), as a local fixture.

Structural repair, and nothing else, relative to `vulnerable/app.py`:

1. `_resolve_company` (C2) never reads `x_company` at all. The parameter
   stays in the signature so both variants keep an identical call shape,
   but no code path in this function can return a value that did not come
   from `API_KEYS[api_key]` -- the caller's own credential is the only
   source of company identity, exactly as it was for `PUT` in both
   variants already.

2. `_CACHE` (C1) is keyed on `(note_id, company)`. A cache entry filled
   while resolving company A's request cannot answer company B's request
   for the same path, because the key itself records which company filled
   the slot.

3. `hop_is_trustworthy` (C3) requires all three of: the certificate chains
   to a trusted CA, the certificate's hostname is *exactly* the hostname
   this hop meant to reach, and the negotiated protocol is a currently
   accepted TLS version. Any missing, unknown, or mismatched input fails
   closed -- a TLS handshake succeeding is not the same claim as "this
   hop's peer is who this hop's policy assumes it is."

Nothing else changed. Do not read a passing `fixed/` run as license to
relax the cache-control or forwarded-header hardening this file assumes
sits in front of it in a real deployment; this fixture is the origin's own
decision, not a CDN configuration.
"""

from __future__ import annotations

from fastapi import FastAPI, Header, HTTPException, Request

API_KEYS: dict[str, str] = {
    "key-A": "companyA",
    "key-B": "companyB",
    "key-Z": "companyZ",
    "key-Q": "companyQ",
}

_ORIGIN_STORE: dict[tuple[str, str], str] = {}
_CACHE: dict[tuple[str, str], str] = {}  # FIXED: keyed on (note_id, company)

_ACCEPTED_TLS_VERSIONS = {"1.2", "1.3"}


def reset() -> None:
    _ORIGIN_STORE.clear()
    _CACHE.clear()


def _bearer(authorization: str | None) -> str | None:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    return authorization[len("Bearer "):]


def _resolve_company(api_key: str | None, x_company: str | None) -> str | None:
    """FIXED: x_company is accepted as a parameter for call-shape
    symmetry with the vulnerable file, but no branch here ever reads it.
    The bound company always comes from the caller's own credential."""
    if api_key not in API_KEYS:
        return None
    return API_KEYS[api_key]


def hop_is_trustworthy(
    expected_hostname: str,
    presented_hostname: str,
    cert_trusted_ca: bool | None,
    tls_version: str,
) -> bool:
    """FIXED: all three checks must hold, and an unrecognized trust state
    or version fails closed rather than being read as trusted."""
    if cert_trusted_ca is not True:
        return False
    if tls_version not in _ACCEPTED_TLS_VERSIONS:
        return False
    return presented_hostname == expected_hostname


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
        cached = _CACHE.get((note_id, company))
        if cached is not None:
            return {"body": cached, "source": "cache"}
        text = _ORIGIN_STORE.get((note_id, company))
        if text is None:
            raise HTTPException(status_code=404, detail="not found")
        _CACHE[(note_id, company)] = text
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
