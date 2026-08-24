# 0.2 — Diagnostic and adaptive bridge (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
quiz_score_grants_phase1_skip always False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Fixed: diagnostics never grant 1.2 cells or skip Gate 1 evidence."""
    return False
```

## Why this restores the cell

Skip only missing *tooling* units; never skip mediation labs.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

The LMS mastery percentage is not a security property of SecureCollab.

A better quiz still cannot observe whether you can write a deny cell.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

## Residual risk

Bridge units still needed for Git/SQL/HTTP gaps — those skips are OK when diagnostics show skill.
