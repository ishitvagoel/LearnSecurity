from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}


def target_is_authorized(url: str) -> bool:
    """Fixed: a URL is in scope only if its hostname is exactly one of the
    three named local lab hosts. Everything else is denied, including a
    URL that cannot be parsed at all.

    Two properties matter here, not one:

    1. Membership is exact-string equality against ALLOWED_HOSTS, never a
       prefix, suffix, or substring test. "evillab.securecollab.test" ends
       with "lab.securecollab.test" and "lab.securecollab.test.evil.com"
       starts with it; neither is a member of the set, and neither may be
       authorized by a version of this check that compares differently.
    2. A parse failure denies rather than raising. urlparse() can raise
       ValueError on a malformed authority (for example an unmatched IPv6
       bracket) and can raise other exceptions on non-string input; a
       caller that cannot get a verdict from this function must not be left
       to assume one. "If the URL cannot be parsed, deny" (see
       lessons/04-build.md) is enforced here, not merely stated there.
    """
    try:
        host = (urlparse(url).hostname or "").lower()
    except (ValueError, AttributeError, TypeError):
        return False
    return host in ALLOWED_HOSTS
