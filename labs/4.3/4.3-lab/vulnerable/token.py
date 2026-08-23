def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    return query.get("access_token") or cookie.get("sc_session") or header
