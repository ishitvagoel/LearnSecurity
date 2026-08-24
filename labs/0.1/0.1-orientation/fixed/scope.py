from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}


def target_is_authorized(url: str) -> bool:
    """Fixed: only named local lab hosts; public hosts are out of scope."""
    host = (urlparse(url).hostname or "").lower()
    return host in ALLOWED_HOSTS
