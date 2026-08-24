# 0.2 — Diagnostic and adaptive bridge (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
**Forbidden outcome:** Quiz score used as authorization to skip 1.2/Gate 1

**Authorized scope:** `labs/0.2/0.2-bridge` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable diagnostic returns True at score 100.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Quiz exists; skip() consulted the number.

## Vulnerable fixture (local)

```python
def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Vulnerable: a diagnostic percentage is treated as 1.2 authorization."""
    return score >= 80
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | A number was treated as a capability (ambient “you’re advanced”). |
| Impact | Learner reaches 4.4/6.x without a matrix; false assurance in reviews. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/0.2/0.2-bridge/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

## Non-goals

No live-target instructions. Synthetic data only.
