# 3.4 — Business logic and abuse-resistant design (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
add_share stops at 5.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
_n = 0
MAX = 5

def reset():
    global _n
    _n = 0

def add_share() -> int:
    global _n
    if _n >= MAX:
        return _n
    _n += 1
    return _n
```

## Why this restores the cell

Check count in the write path; reject 6th.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

HTML max=5 is not enforcement.

Cap on /share but not on /import or GraphQL.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Invite tokens (6.6) and export quotas (6.7).

## Residual risk

Legitimate teams >5 need an owned exception (E6).
