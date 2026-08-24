# 3.3 — Secure architecture patterns (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
can_select('app', 'tB', 'tA') is False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def can_select(role: str, tenant: str, note_tenant: str) -> bool:
    if role != "app":
        return False
    return tenant == note_tenant
```

## Why this restores the cell

Least-privilege role; RLS as extra layer (5.5).

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

SQLAlchemy session is not a tenant scope.

RLS bypassed by table owners and SECURITY DEFINER (E5).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Serverless function with a shared “admin” connection string.

## Residual risk

Stolen migrator role — separate credential, shorter life.
