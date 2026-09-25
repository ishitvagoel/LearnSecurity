"""Fixed: honor HttpOnly/Secure on the session cookie, validate ``Origin``
against a fixed allow-list of exact origins before ever reflecting it, never
pair ``Access-Control-Allow-Credentials: true`` with an origin that was not
on that list, and send a real, blocking ``Content-Security-Policy`` -- not
only ``Report-Only``.

The allow-list check is exact-string set membership against
``ALLOWED_ORIGINS``, not a hostname suffix or substring test. A subdomain, a
different scheme, or a different port is a different *origin* even when it
shares the same registrable domain -- the same string a person would read
aloud as "the site" -- and that distinction is the whole reason to check
origin here at all: the browser's same-origin policy, and the
``Access-Control-Allow-Origin`` header that relaxes it, both operate on the
exact scheme+host+port tuple, never on the domain name a person recognizes.
A "smarter-looking" check such as ``origin.endswith(".securecollab.example")``
would still be wrong for this fixture: it would trust every present and
future subdomain of ``securecollab.example`` with credentialed access to
member notes, when only ``https://app.securecollab.example`` -- the one
origin that actually serves the SecureCollab web client -- is meant to have
it.
"""

from __future__ import annotations

from fastapi import FastAPI, Request, Response

app = FastAPI()

NOTES = ("Q3 planning notes", "Incident retro draft")

ALLOWED_ORIGINS = frozenset({"https://app.securecollab.example"})

CSP = (
    "default-src 'self'; object-src 'none'; base-uri 'none'; "
    "frame-ancestors 'none'; script-src 'self'; report-uri /csp-report"
)


@app.post("/login")
def login(response: Response) -> dict:
    response.set_cookie(
        "sc_session",
        "synthetic-session",
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return {"ok": True}


@app.get("/notes")
def notes(request: Request, response: Response) -> dict:
    origin = request.headers.get("origin")
    if origin is not None and origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
    # No else branch. An origin that is not exactly in ALLOWED_ORIGINS gets
    # no Access-Control-Allow-Origin header at all -- a deny, not a
    # narrower allow. The response body below is still computed and
    # returned either way (a real server commonly cannot tell whether the
    # caller is a browser enforcing CORS or curl ignoring it); the header
    # is the only signal a real browser will consult before handing the
    # body to a cross-origin script. See lessons/05-verify.md for what that
    # means this test file can and cannot prove.
    response.headers["Content-Security-Policy"] = CSP
    session = request.cookies.get("sc_session")
    if not session:
        return {"notes": []}
    return {"notes": list(NOTES)}
