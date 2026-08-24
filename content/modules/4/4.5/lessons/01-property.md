# 4.5 — OAuth, OpenID Connect, browser apps, and native apps (1 Property)

**Kind:** concept-model
**Loop step:** 1 Property
**Standards:** OAuth 2.1 (I-D, not final); OIDC Core (final). Do not present 2.1 as RFC.

## Property (start here)

An access token is accepted only if **aud** is this API. A token minted for another audience is not a SecureCollab session. OAuth 2.1 remains an **Internet-Draft** — label it.

## Attacker capabilities and trust assumptions

Token from another API replayed here. Trust: local claim dict, not a real JWT crypto lab.

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
