# SecureCollab Phase 1 — unfurl egress

Design stub for Module 6.5. Not a production crawler.

## Freeze

- Local `allowed(url)`.
- Tests call the predicate only. No live fetches.

## Authority, not a string

HTTPS to `lab.securecollab.test` may be true. Link-local and loopback are false. Scheme-only is not an allow-list.

## Tests

Link-local deny is the evidence. A cloud WAF sticker is not.
