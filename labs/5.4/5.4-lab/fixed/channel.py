def channel_is_https(headers: dict, server_scheme: str) -> bool:
    return server_scheme == "https"
