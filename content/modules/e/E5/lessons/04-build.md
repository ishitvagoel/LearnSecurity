# E5 — Large-scale authorization and multi-tenant SaaS (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
session A + body B => A.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def tenant_for(session, body):
    return session['tenant']
```

## Why this restores the cell

Ignore body tenant; bind from session; RLS extra.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Postgres RLS with a SET tenant from the body is this bug.

Search indexes, caches (2.2), data lakes — every copy.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Zanzibar tuple vs this binding.

## Residual risk

Honest super-admin — E6 + 3.3.
