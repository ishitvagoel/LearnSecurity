import hashlib
import hmac


def accept(sig, body, secret):
    if not sig:
        return False
    expect = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()
    if len(sig) != len(expect):
        return False
    return hmac.compare_digest(sig, expect)
