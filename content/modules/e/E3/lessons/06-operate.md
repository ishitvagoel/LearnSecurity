# E3 — Payments and other high-assurance systems (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.

## Property (start here)

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.

## Attacker capabilities and trust assumptions

- **Attacker:** Retry after 504; client double-click.
- **Trust:** Local capture(key); synthetic amounts.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | charge_count vs unique keys. |
| Signal (no bodies) | duplicate_capture_denied. |
| Revoke / recover | Credit the extra (runbook); still fail the test first. |
| Residual | Webhook vs capture race (7.3+2.4). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E3/e3-lab`.

## Transfer

Health record append-only audit.

## Usability

Payment confirmations must be accessible; trapped users retry (this bug).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
