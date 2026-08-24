"""Vulnerable: session cookie is readable to script in the origin (no HttpOnly)."""


def js_read_session(cookies: dict) -> str | None:
    session = cookies.get("sc_session")
    if not session:
        return None
    return session["value"]
