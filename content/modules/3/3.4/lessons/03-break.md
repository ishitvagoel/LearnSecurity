# 3.4 — Business logic and abuse-resistant design (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
**Forbidden outcome:** Share grants exceed the product cap of 5

**Authorized scope:** `labs/3.4/3.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable share_limit.py has no cap.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: add_share without cap.

## Vulnerable fixture (local)

```python
_n = 0

def reset():
    global _n
    _n = 0

def add_share() -> int:
    global _n
    _n += 1
    return _n
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Policy only in the UI. |
| Impact | Unbounded readers; 1.2 matrix explodes. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/3.4/3.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Invite tokens (6.6) and export quotas (6.7).

## Non-goals

No live-target instructions. Synthetic data only.
