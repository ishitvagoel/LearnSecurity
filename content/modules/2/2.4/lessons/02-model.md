# 2.4 — State, time, concurrency, and distributed failure (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.

## Property (start here)

A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.

## Attacker capabilities and trust assumptions

- **Attacker:** A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).
- **Trust:** Local share store. Clocks may skew; do not rely on “user won’t retry.”
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Sharer, retrying client, share table |
| Objects | Share row, idempotency key, note n1 |
| Actions | share_note, retry |
| Channels | HTTP POST, queue redelivery |
| TCB | Idempotency store keyed by (actor, key) with the first outcome. |
| Untrusted | Client “I only clicked once”; load balancer retries |
| State / time | Two POSTs 200ms apart; worker redelivery tomorrow. |
| 1.1 cell | Integrity of authorization state over time. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| owner | n1 | share-once | allow |
| owner | n1 | share-retry-same-key | no-second-row |
| owner | n1 | share-new-key | policy-cap-3.4 |
| worker | n1 | redeliver | same-as-retry |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/2.4/2.4-state-time` file `share.py`.

## Transfer

Payment capture (E3) and invite tokens (6.6) are the same shape.

## Residual risk

Lost first response still needs a read-your-write path.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
