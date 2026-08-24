def target_is_authorized(url: str) -> bool:
    """Vulnerable: any URL is treated as in-scope."""
    return True
