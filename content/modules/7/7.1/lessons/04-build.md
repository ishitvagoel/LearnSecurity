# 7.1 — API contracts, protocols, and inventory (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
is_admin stays False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
ALLOWED={'display_name'}
def apply(user, body):
    for k,v in body.items():
        if k in ALLOWED:
            user[k]=v
    return user
```

## Why this restores the cell

Explicit writable set; ignore/reject unknown privileged fields.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Pydantic extra=allow is this bug. FastAPI will happily take extra if your model does.

Allow-list must track every protocol (REST, GraphQL, gRPC).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

## Residual risk

Honest display_name XSS (6.2) is another cell.
