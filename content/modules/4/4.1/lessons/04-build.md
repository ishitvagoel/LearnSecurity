# 4.1 — Identity lifecycle (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
delete_user sets session_valid False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
SESSIONS = {"alice": True}
DELETED = set()

def reset():
    SESSIONS.clear(); SESSIONS["alice"] = True
    DELETED.clear()

def delete_user(user: str) -> None:
    DELETED.add(user)
    SESSIONS.pop(user, None)

def session_valid(user: str) -> bool:
    if user in DELETED:
        return False
    return bool(SESSIONS.get(user))
```

## Why this restores the cell

Invalidate sessions (and tokens, workers) in the same use-case.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Starlette SessionMiddleware does not know HR offboarding.

Email “you’re deleted” is not revocation.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Contractor access end-date; support impersonation tickets.

## Residual risk

Backups still contain the user row — 5.1.
