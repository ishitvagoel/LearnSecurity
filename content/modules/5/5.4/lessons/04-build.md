# 5.4 — Secure communication and channel binding (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
header https + socket http => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def channel_is_https(headers, server_scheme):
    return server_scheme == 'https'
```

## Why this restores the cell

Ignore client proto unless the immediate peer is a trusted proxy with a bound identity.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

uvicorn --proxy-headers without a trusted proxy IP is this bug.

Correct TLS to the LB is not e2e if you needed e2e (messaging).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

mTLS service identity vs this header.

## Residual risk

Pinning mobile apps (8.x) vs operational breakage — document, don’t mandate.
