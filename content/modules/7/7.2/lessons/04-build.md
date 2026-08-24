# 7.2 — Object, property, and function security (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
member × secret_internal False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def resolve(role, field):
    if field=='secret_internal':
        return role=='service'
    return True
```

## Why this restores the cell

Allow-list fields by role; never bind authz to the id format.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

SQLAlchemy to_dict() is not a policy.

Hiding fields in UI only.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Bulk update; search highlighting leaking snippets.

## Residual risk

Admin sees secret_internal — audited.
