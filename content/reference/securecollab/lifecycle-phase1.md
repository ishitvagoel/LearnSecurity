# SecureCollab Phase 1 — account lifecycle

Design stub for Module 4.1. Not a production IdP.

## Freeze

- Local `SESSIONS` / `DELETED` maps. Synthetic user `alice`.
- No live SSO.

## Artifact must die

`delete_user` is a use-case: mark deleted **and** invalidate sessions. A leftover cookie is a 1.2 cell over time.

## Tests

`session_valid` after delete is the evidence. Profile DELETE is not.
