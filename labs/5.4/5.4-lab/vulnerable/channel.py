def channel_is_https(headers: dict, server_scheme: str) -> bool:
    return headers.get("X-Forwarded-Proto") == "https" or server_scheme == "https"
