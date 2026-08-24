# 0.2 — Diagnostic and adaptive bridge (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Quiz score used as authorization to skip 1.2/Gate 1 |
| Failure | Fail closed: Skip only missing *tooling* units; never skip mediation labs |

Lab tests: `test_diagnostic.py` under `labs/0.2/0.2-bridge`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Quiz score used as authorization to skip 1.2/Gate 1`
- `--impl fixed`: **pass**

100 does not skip; missing Git still recommends a bridge unit.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
