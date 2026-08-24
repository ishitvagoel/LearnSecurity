# 6.6 — Workflow, race, and exceptional-condition failures (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
second accept False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
_used=set()
def reset():
    _used.clear()
def accept(token):
    if token in _used:
        return False
    _used.add(token)
    return True
```

## Why this restores the cell

Single-use in a transaction; expire; bind to recipient.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

DB unique constraint helps but must be the actual consume.

Used flag without locking still races.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

## Residual risk

Email is a phishable channel (4.2).
