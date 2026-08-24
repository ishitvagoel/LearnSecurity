# 0.2-LO-06 — Diagnostic is not authorization (Operate)

**Kind:** loop-object  
**Loop step:** 6 Operate  
**Standards:** CISA Secure by Design (final public guidance); Saltzer (1975, seminal) where authority appears.

## Property (start here)

A placement quiz score does not skip 1.2 mediation or Gate 1 evidence. Adaptive path may skip **orientation prose**, never **invariants**.

## Attacker capabilities and trust assumptions

No attacker needed: the **product** (course) must not treat a score as a capability. Learner with 100% is still untrusted relative to tenant B’s notes.

## Root cause / impact / prevention / detection / recovery

Root cause: confusing assessment score with access matrix. Impact: skipped complete mediation teaching. Prevention: quiz never returns `grants_phase1_skip`. Detection: curriculum tests. Recovery: re-instate 1.2 lab.

## Framework defaults vs application guarantees

LMS ‘pass’ badges are not ASVS. SAMM scores are not product security.

## Practice

Operate: if a fork skips 1.2, that is a curriculum defect.

## Transfer

Same.

## Non-goals

Live targets, real PII, weaponized payloads. Mastery gates stay not-attempted.
