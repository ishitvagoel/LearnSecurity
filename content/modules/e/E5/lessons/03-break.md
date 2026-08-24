# E5 — Large-scale authorization and multi-tenant SaaS (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.

## Property (start here)

A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).

## Attacker capabilities and trust assumptions

- **Attacker:** Member of A sending tenant B in GraphQL/JSON.
- **Trust:** Local tenant_for(session, body).
**Forbidden outcome:** JSON body switches the bound tenant

**Authorized scope:** `labs/E5/e5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable rls.py trusts body.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: tenant_for({A},{B}) == B.

## Vulnerable fixture (local)

```python
def tenant_for(session, body):
    return body.get('tenant', session['tenant'])
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Client-chosen tenant. |
| Impact | Cross-tenant read/write at scale. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E5/e5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Zanzibar tuple vs this binding.

## Non-goals

No live-target instructions. Synthetic data only.
