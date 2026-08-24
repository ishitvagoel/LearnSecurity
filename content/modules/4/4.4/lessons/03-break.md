# 4.4 — Authorization and tenant isolation (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
**Forbidden outcome:** Grant on n1 authorizes n2

**Authorized scope:** `labs/4.4/4.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable grant.py treats any grant as global.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: can_read(bob, n2) true because bob has n1.

## Vulnerable fixture (local)

```python
GRANTS = {("bob", "n1"): True}

def reset():
    GRANTS.clear(); GRANTS[("bob", "n1")] = True

def can_read(user: str, note_id: str) -> bool:
    return any(u == user for (u, _n) in GRANTS)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Collection-level “has any grant” flag. |
| Impact | Unauthorized read of n2 body. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/4.4/4.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Property-level: bob can read title but not body (7.2).

## Non-goals

No live-target instructions. Synthetic data only.
