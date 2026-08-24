# 4.1 — Digital identity and account lifecycle (3 Break)

**Kind:** mechanism-lab
**Loop step:** 3 Break
**Standards:** NIST SP 800-63-4 (final) lifecycle/CX; not a password-complexity checklist.

## Property (start here)

A **deleted** SecureCollab user must not read notes with a leftover session. Lifecycle is part of 1.2 mediation over time.

## Attacker capabilities and trust assumptions

Stolen cookie after self-delete or admin disable. Trust: lab session store.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Run `labs/4.1/4.1-lab` with --impl vulnerable then fixed.

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
