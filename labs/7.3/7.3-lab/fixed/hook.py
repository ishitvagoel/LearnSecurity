import hmac, hashlib
def accept(sig, body, secret):
    expect=hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(sig, expect)
