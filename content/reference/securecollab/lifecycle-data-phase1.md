# SecureCollab Phase 1 — data lifecycle and deletion graph

Design stub for Module 5.1. Not a production warehouse.

## Freeze

- Local `NOTES` / `ANALYTICS` / `SEARCH` maps. Synthetic user `alice` and body `secret`.
- No live analytics, no real PII.

## Every copy is in the graph

`delete_account` is a use-case: pop notes **and** analytics **and** search. Encryption of a kept warehouse row is not deletion. Privacy Framework 1.0 is the final pin; 1.1 IPD is draft.

## Tests

`body_retained` and `search_retained` after delete are the evidence. Notes-row DELETE is not.
