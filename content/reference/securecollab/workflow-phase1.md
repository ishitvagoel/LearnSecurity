# SecureCollab Phase 1 — invite consume

Design stub for Module 6.6. Not a production mailer.

## Freeze

- Local `accept(token)` / `reset()`.
- Synthetic tokens `t1` / `t2`.

## Consume-once

First accept may succeed. Second accept of the same token is denied. Distinct tokens are independent. Fail-open on store errors is forbidden in production (`v5.0.0-16.5.3`).

## Tests

Second `t1` false is the evidence. HTTP 400 is not.
