"""Fixed: HttpOnly session is not readable to script; XSS is not 'solved' — this is one cell."""


def js_read_session(cookies: dict) -> str | None:
    session = cookies.get("sc_session")
    if not session:
        return None
    if session.get("httponly"):
        return None
    return session["value"]
