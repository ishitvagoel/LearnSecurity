# E3 — Payments and other high-assurance systems (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | payer, ledger |
| Objects | capture key k1 |
| Actions | capture, charge_count |
| Channels | payment API stand-in |
| TCB | Idempotent capture store. |
| Untrusted | Client retries, webhook duplicates (7.3) |
| State / time | Two captures. |
| 1.1 cell | Integrity of money-like state. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| payer | k1 first | capture | allow |
| payer | k1 retry | capture | no-second-charge |
| webhook | k1 | capture | same |
| logs | PAN | store | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E3/e3-lab` file `pay.py`.

## Transfer

Health record append-only audit.

## Residual risk

Webhook vs capture race (7.3+2.4).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
