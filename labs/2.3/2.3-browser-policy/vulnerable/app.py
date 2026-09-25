"""Vulnerable: SecureCollab's login/notes surface for module 2.3.

Three independent browser-policy defects live here, staged separately so
each can be reasoned about on its own.

1. Cookie (C1). ``/login`` sets the ``sc_session`` cookie without
   ``HttpOnly`` and without ``Secure``. Page script in the origin can read
   the value through ``document.cookie``, and the cookie can be sent over a
   plaintext connection. This is the same script-readability failure the
   module's cookie-jar model teaches, now on a real ``Set-Cookie`` response
   header instead of a modeled dict.

2. CORS (C2, C3). ``/notes`` reflects whatever ``Origin`` request header a
   caller sends back as ``Access-Control-Allow-Origin``, and always sets
   ``Access-Control-Allow-Credentials: true``. Reflecting the caller's own
   claim about who it is -- instead of checking it against a fixed set of
   trusted origins -- means any origin, not only
   ``https://app.securecollab.example``, can issue a credentialed
   ``fetch()`` to ``/notes`` from a signed-in member's browser and read the
   response. The browser decides whether to hand the response to the
   calling script by reading these two headers; it does not check whether
   the value the server sent back is true.

3. CSP (C4). The app sends ``Content-Security-Policy-Report-Only`` and
   never a blocking ``Content-Security-Policy``. Report-Only asks the
   browser to send a violation report to ``/csp-report``; it does not ask
   the browser to refuse to load or execute anything.
"""

from __future__ import annotations

from fastapi import FastAPI, Request, Response

app = FastAPI()

NOTES = ("Q3 planning notes", "Incident retro draft")


@app.post("/login")
def login(response: Response) -> dict:
    # No httponly, no secure: script in the origin can read this value, and
    # the cookie is not marked as HTTPS-only either.
    response.set_cookie("sc_session", "synthetic-session")
    return {"ok": True}


@app.get("/notes")
def notes(request: Request, response: Response) -> dict:
    origin = request.headers.get("origin")
    if origin:
        # Reflects the caller's claimed origin unconditionally, and always
        # pairs it with credentials: true. A caller does not have to guess
        # a trusted origin string -- whatever it sends back to itself as
        # Origin is what comes back as the allow header.
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Content-Security-Policy-Report-Only"] = (
        "default-src 'self'; report-uri /csp-report"
    )
    session = request.cookies.get("sc_session")
    if not session:
        return {"notes": []}
    return {"notes": list(NOTES)}
