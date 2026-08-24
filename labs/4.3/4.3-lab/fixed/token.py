def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    if query.get("access_token"):
        return None
    return cookie.get("sc_session") or header
