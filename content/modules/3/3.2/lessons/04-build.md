# 3.2 — Threat modeling (4 Build)

**Kind:** design-exercise
**Loop step:** 4 Build
**Standards:** OWASP Threat Modeling (maintained, final guidance) Four Questions; not a single tool.

## Property (start here)

A green scanner does **not** mean 'no threats.' SecureCollab threat model must still list a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

Modeler who substitutes scanner output for Shostack questions. Trust: none in the scanner as TCB.

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
