# 10.4 — Deployment and configuration hardening (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
prod+debug => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def boot_ok(env, debug):
    return not (env == 'prod' and debug)
```

## Why this restores the cell

Refuse boot; config review; no debug routes registered.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Next.js NODE_ENV=development in prod compose files.

debug=False still has other flags (feature, migration).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Feature flag that disables authz.

## Residual risk

Emergency debug with E6 timebox.
