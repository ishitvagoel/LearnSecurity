# 2.4 — State, time, concurrency, and distributed failure (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Duplicate-key metric; share_count anomaly. |
| Signal (no bodies) | share_count vs unique keys; never fail-open if the key store is down. |
| Revoke / recover | Revoke extra shares; notify owner. |
| Residual | Lost first response still needs a read-your-write path. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/2.4/2.4-state-time`.

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

## Usability

Disable-on-submit is not the property (users retry). Accessible “still working” status (WCAG 4.1.3) must not encourage extra POSTs with new keys.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
