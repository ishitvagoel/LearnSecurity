# SecureCollab Phase 1 — share product cap

Design stub for Module 3.4. Not a production rate limiter.

## Freeze

- Local `add_share` counter. Cap 5. Synthetic only.
- No live tenants.

## Write path, not UI

Eight `add_share` calls must leave count ≤ 5. HTML `max` is not the TCB. Rate limits (6.7) and same-key retry (2.4) are different cells.

## Tests

`last <= 5` after eight calls is the evidence. API4 as a sticker is not.
