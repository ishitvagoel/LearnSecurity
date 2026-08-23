# 3.3 — Secure architecture patterns (7 Generalize)

**Kind:** transfer-challenge
**Loop step:** 7 Generalize
**Standards:** ASVS 5.0.0 V15 architecture (chapter-level); Saltzer least privilege (1975, seminal).

## Property (start here)

Tenant isolation is not 'one Postgres role for the whole app.' A stolen app role must not SELECT other tenants without 1.2 mediation.

## Attacker capabilities and trust assumptions

Stolen application DB credential. Trust: DB is in TCB only with per-tenant enforcement (5.5 residual if app-only).

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Change one actor or channel; which 1.x/2.x artifacts are invalid?

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
