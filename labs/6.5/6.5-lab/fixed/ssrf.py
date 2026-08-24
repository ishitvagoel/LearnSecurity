from urllib.parse import urlparse
ALLOW={'lab.securecollab.test'}
def allowed(url):
    u=urlparse(url)
    host=(u.hostname or '').lower()
    if host in {'169.254.169.254','127.0.0.1','localhost'}:
        return False
    return u.scheme=='https' and host in ALLOW
