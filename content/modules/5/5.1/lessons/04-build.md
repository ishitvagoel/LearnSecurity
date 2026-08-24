# 5.1 — Data lifecycle and privacy engineering (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
delete_account also ANALYTICS.pop.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
NOTES={'alice':'secret'}
ANALYTICS={'alice':'secret'}
def reset():
    NOTES.clear(); NOTES['alice']='secret'
    ANALYTICS.clear(); ANALYTICS['alice']='secret'
def delete_account(user):
    NOTES.pop(user, None)
    ANALYTICS.pop(user, None)
def body_retained(user):
    return ANALYTICS.get(user)
```

## Why this restores the cell

Inventory copies; delete or unlink bodies in each.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Postgres DELETE is not warehouse DELETE. Next.js does not erase S3 analytics.

Anonymize ids but keep bodies — still a body retention fail.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

CSV export to a partner; clinic-booking card PHI.

## Residual risk

Legal hold copies — named exception with owner (E6).
