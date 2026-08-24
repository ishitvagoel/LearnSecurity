# 6.3 — Cross-site and cross-context attacks (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
evil origin + no token => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def allow_share(origin, expected, token=None, session_cookie=True):
    if not session_cookie:
        return False
    return origin == expected and token == 'lab-csrf'
```

## Why this restores the cell

Reject foreign Origin; require token for cookie sessions.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

SameSite=Lax is not complete (GET side effects, chrome exceptions).

Bearer tokens in Authorization are a different deputy model.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

postMessage, clickjacking, CORS * with credentials.

## Residual risk

User clicking “share” on a lookalike UI — 4.2 phishing.
