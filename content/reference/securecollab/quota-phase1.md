# SecureCollab Phase 1 — export quota

Design stub for Module 6.7. Not a production rate limiter.

## Freeze

- Local `allow(n_calls)` with cap 3.
- No live traffic.

## Resource account

`allow(4)` is false. Per-IP nginx limits are shared-fate, not this predicate. Extra CSVs are 5.1 copies.

## Tests

Fourth denied is the evidence. A disabled SPA button is not.
