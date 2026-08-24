# 0.2 — Diagnostic and adaptive bridge (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
Review `labs/0.2/0.2-bridge/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/0.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): if score >= 80: skip_phase(1)
- Seeded smell (label it yourself): No link from diagnostic to 1.2 evidence
- Seeded smell (label it yourself): Badge screenshot as Gate 1
- Seeded smell (label it yourself): Adaptive path hides 1.4 accessibility residual

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Placement is a security clearance
- Fast learners skip invariants
- Tool fluency is threat modeling

## Practice

Write three review notes. Do not open the keys file.

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

## HITL / WCAG 2.2

Diagnostic UI must not be color-only “green = skip Phase 1” (WCAG 2.2 1.4.1).
