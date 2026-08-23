# 4.3 — Sessions, cookies, and tokens (3 Break)

**Kind:** mechanism-lab
**Loop step:** 3 Break
**Standards:** ASVS 5.0.0 V7 session (chapter-level); 2.3 HttpOnly cell.

## Property (start here)

A session token in the **query string** is not an acceptable session. Bearer belongs in Cookie (HttpOnly, 2.3) or Authorization, not logs and Referer.

## Attacker capabilities and trust assumptions

Referer leak, access logs. Trust: local request model.

## Root cause / impact / prevention / detection / recovery

Root cause is a missing or wrong **mechanism relative to the property**, not a missing scanner item.
Impact is a named 1.1 cell (confidentiality, integrity, authenticity, …).
Prevention is the smallest structural control in the lab.
Detection logs the attempt without storing secrets or note bodies.
Recovery revokes, rotates, or quarantines — fail-safe, not fail-open.

## Framework defaults vs application guarantees

FastAPI/Next.js/PostgreSQL defaults are not this invariant. The application must still enforce it.

## Practice

Run `labs/4.3/4.3-lab` with --impl vulnerable then fixed.

## Transfer

Apply the same property to a clinic-booking card or a new SecureCollab file object. Do not answer with a Top 10 name.

## Non-goals

Live targets, real PII, weaponized payloads. Gates 0–10 and M0–M5 stay not-attempted.
