# 7.3 — Webhooks, callbacks, and third-party APIs (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
empty signature False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
import hmac, hashlib
def accept(sig, body, secret):
    expect=hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(sig, expect)
```

## Why this restores the cell

Verify MAC; bind to secret per provider; timestamp.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Stripe SDK verify is not your custom HMAC if you reimplement poorly.

Correct signature still needs 1.2 on side effects.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

## Residual risk

Provider compromise — egress + least privilege on what a webhook may do.
