# 2.4 — State, time, concurrency, and distributed failure (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
Review `labs/2.4/2.4-state-time/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/2.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): INSERT share on every POST
- Seeded smell (label it yourself): Idempotency key in a log comment only
- Seeded smell (label it yourself): Test only happy-path single click
- Seeded smell (label it yourself): Fail-open on idempotency store timeout

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Retries are a client bug not ours
- 200 means once
- Databases are automatically idempotent

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

## HITL / WCAG 2.2

Disable-on-submit is not the property (users retry). Accessible “still working” status (WCAG 4.1.3) must not encourage extra POSTs with new keys.
