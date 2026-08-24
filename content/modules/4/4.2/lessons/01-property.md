# 4.2 — Authentication, phishing resistance, and usable access (1 Property)

**Kind:** concept-model
**Loop step:** 1 Property
**Standards:** NIST SP 800-63-4 (final) phishing-resistant AAL; WebAuthn L3 remains **Candidate Recommendation** — label it.

## Property (start here)

Password + 'remember me' is **not** phishing-resistant. A phishing-resistant authenticator must fail a lookalike origin (WebAuthn-class). Passwords stay allowed only as a labeled residual.

## Attacker capabilities and trust assumptions

Lookalike origin. Trust: lab origin string only — no live IdP.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Name the SecureCollab invariant in one testable sentence.

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
