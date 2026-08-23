# 3.4 — Business logic and abuse-resistant design (4 Build)

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** ASVS 5.0.0 V2 business logic (chapter-level). Top 10 is not the outline.

## Property (start here)

A note share grant cannot be applied twice to exceed the product rule (max 5 members). Abuse is a **logic** invariant, not a new CWE name.

## Attacker capabilities and trust assumptions

Member who retries share (2.4) or parallel tabs. Trust: local counter only.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

State the structural fix (not a denylist of one user).

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
