# 4.4 — Authorization and tenant isolation (5 Verify)

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** ASVS 5.0.0 V8 (chapter-level); Saltzer complete mediation.

## Property (start here)

A share **grant** for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table.

## Attacker capabilities and trust assumptions

Member with a grant on n1 who swaps note_id. Trust: local grants dict.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Name the forbidden-outcome test.

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
