# 3.1 — Assets, data classification, and security requirements (Review)

**Kind:** code-review
**Loop step:** Review
**Standards:** NIST CSF 2.0 (final) Identify; ASVS 5.0.0 V14 data protection (chapter-level).

## Property (start here)

Note **bodies** are Confidential; they must not appear in application logs. Classification is a property of the field, not a spreadsheet label.

## Attacker capabilities and trust assumptions

Operator who can read logs; another tenant's admin; a support engineer. Trust: lab log sink is local.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Review the vulnerable tree; keys are not in this file.

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
