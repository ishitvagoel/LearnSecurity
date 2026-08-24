# 0.2 — Diagnostic and adaptive bridge (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
**Mechanism (not the property):** The LMS mastery percentage is not a security property of SecureCollab.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 0.2 |
|---|---|
| Root cause | A number was treated as a capability (ambient “you’re advanced”). |
| Preconditions | Quiz exists; skip() consulted the number. |
| Impact (1.1 cell) | Integrity of the learning system: false competency is a safety defect for later labs. — Learner reaches 4.4/6.x without a matrix; false assurance in reviews. |
| Prevention | Skip only missing *tooling* units; never skip mediation labs. |
| Detection | Path log: skipped ids vs required 1.2/1.3/1.4. |
| Recovery | Re-open 1.2; do not back-date Gate 1. |

## Framework defaults vs application guarantees

The LMS mastery percentage is not a security property of SecureCollab.

## Mechanism limits and bypasses

A better quiz still cannot observe whether you can write a deny cell.

Memorizing 1.2 answers without running the lab.

## Residual risk

Bridge units still needed for Git/SQL/HTTP gaps — those skips are OK when diagnostics show skill.

## Practice

Name one thing a 100% quiz cannot prove about tenant isolation.

Run `labs/0.2/0.2-bridge` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

Onboarding at a clinic-booking SaaS.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Diagnostic UI must not be color-only “green = skip Phase 1” (WCAG 2.2 1.4.1).
