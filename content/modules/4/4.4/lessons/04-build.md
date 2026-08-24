# 4.4 — Authorization and tenant isolation (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
can_read('bob','n2') False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
GRANTS = {("bob", "n1"): True}

def reset():
    GRANTS.clear(); GRANTS[("bob", "n1")] = True

def can_read(user: str, note_id: str) -> bool:
    return bool(GRANTS.get((user, note_id)))
```

## Why this restores the cell

Grant keyed by note id; deny default.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Depends(get_user) is not Depends(can_read_note).

UUID obscurity is not a grant.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Property-level: bob can read title but not body (7.2).

## Residual risk

Honest grant on n1 still reveals n1 — that’s the product.
