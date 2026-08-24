# 6.3 — Cross-site and cross-context attacks (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
**Forbidden outcome:** Cross-origin state-changing POST authorized by cookie alone

**Authorized scope:** `labs/6.3/6.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable csrf.py allows foreign origin.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: allow_share(evil, app, token=None) True.

## Vulnerable fixture (local)

```python
def allow_share(origin, expected, token=None, session_cookie=True):
    return session_cookie
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Cookie authority used without site-bound intent. |
| Impact | Unwanted share grant. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.3/6.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

postMessage, clickjacking, CORS * with credentials.

## Non-goals

No live-target instructions. Synthetic data only.
