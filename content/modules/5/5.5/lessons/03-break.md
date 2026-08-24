# 5.5 — Database and persistence security (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
**Forbidden outcome:** Query built by concatenating untrusted strings into SQL

**Authorized scope:** `labs/5.5/5.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable query.py concatenates.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: fetch_sql returns a concatenated str.

## Vulnerable fixture (local)

```python
def fetch_sql(tenant, note_id):
    return f"SELECT body FROM notes WHERE tenant='{tenant}' AND id='{note_id}'"
def is_bound(sql):
    return '%s' in sql or '?' in sql
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Data and program mixed in one string. |
| Impact | Interpreter reads other tenants / mutates rows. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/5.5/5.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

NoSQL operators, GraphQL args (7.1).

## Non-goals

No live-target instructions. Synthetic data only.
