# 6.7 — Resource abuse, automation, and availability (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
**Forbidden outcome:** Unbounded exports (4th allowed in the lab window)

**Authorized scope:** `labs/6.7/6.7-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable limit.py unbounded.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: allow(4) True.

## Vulnerable fixture (local)

```python
def allow(n_calls):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | No resource account. |
| Impact | Cost/DoS; extra CSV copies of bodies. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.7/6.7-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Notification fan-out; search complexity.

## Non-goals

No live-target instructions. Synthetic data only.
