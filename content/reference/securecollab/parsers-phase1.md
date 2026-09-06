# SecureCollab Phase 1 — parser boundaries

Design stub for Module 2.1. Not a production parser.

## Freeze

- Local JSON ingest fixture with CLEAN unique-key objects and AMBIGUOUS duplicate `"tenant"` keys.
- No live API, no public JSON bombs, no real patient identifiers.

## One meaning

The same request bytes yield one parse result used for both the 1.2 tenant decision and the stored row. Disagreement is a confidentiality failure.

## Interpreters on the path

Client encoder (hostile) → optional proxy re-encode (2.2) → agreed parse (TCB) → ACL and persist. PostgreSQL `jsonb` and a later worker re-parse are additional interpreters until proven identical.

## Four words

Validation, canonicalization, sanitization, and encoding answer different questions. Duplicate-key rejection is canonicalization plus fail-safe ingest, not HTML sanitization and not output encoding.
