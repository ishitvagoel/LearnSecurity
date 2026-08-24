# 9.3 — Security-focused tests (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
**Forbidden outcome:** HTTP 200-only test counted as a security test

**Authorized scope:** `labs/9.3/9.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable stest.py treats 200 as security.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: is_security_test({status_asserted: True}) True.

## Vulnerable fixture (local)

```python
def is_security_test(t):
    return bool(t.get('status_asserted'))
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Happy path as assurance. |
| Impact | 4.4 holes with green CI. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/9.3/9.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Fuzzing without an oracle.

## Non-goals

No live-target instructions. Synthetic data only.
