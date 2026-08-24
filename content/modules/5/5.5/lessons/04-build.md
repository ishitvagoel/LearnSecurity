# 5.5 — Database and persistence security (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
fetch_sql returns bound structure not a concat string.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def fetch_sql(tenant, note_id):
    return ("SELECT body FROM notes WHERE tenant=%s AND id=%s", (tenant, note_id))
def is_bound(q):
    return isinstance(q, tuple) and len(q[1])==2
```

## Why this restores the cell

Parameters; identifier allow-lists for ORDER BY.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

SQLAlchemy text() with f-strings is still concat. ORM defaults can still interpolate.

Bound ids plus missing 1.2 still leak via legitimate queries.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

NoSQL operators, GraphQL args (7.1).

## Residual risk

DB superuser tools; replicas.
