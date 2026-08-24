# 7.1 — API contracts, protocols, and inventory (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.

## Property (start here)

Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).

## Attacker capabilities and trust assumptions

- **Attacker:** Authenticated member sending extra JSON keys.
- **Trust:** Local apply(user, patch).
**Forbidden outcome:** Client PATCH sets is_admin

**Authorized scope:** `labs/7.1/7.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable patch.py copies is_admin.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: apply(..., {is_admin: True}) succeeds.

## Vulnerable fixture (local)

```python
def apply(user, body):
    user.update(body)
    return user
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Binder maps any key onto the entity. |
| Impact | Privilege lift. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/7.1/7.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

GraphQL mutation arguments; gRPC unknown fields.

## Non-goals

No live-target instructions. Synthetic data only.
