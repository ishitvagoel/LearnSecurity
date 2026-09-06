from urllib.parse import urlparse

ALLOW = {"lab.securecollab.test"}
BLOCK_HOSTS = {"169.254.169.254", "127.0.0.1", "localhost"}


def allowed(url):
    u = urlparse(url)
    host = (u.hostname or "").lower()
    if host in BLOCK_HOSTS:
        return False
    return u.scheme == "https" and host in ALLOW
