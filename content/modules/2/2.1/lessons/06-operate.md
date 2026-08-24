# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Parse-error metric; differential test corpus in CI. |
| Signal (no bodies) | ingest_reject_duplicate_key count; never log raw ambiguous bodies. |
| Revoke / recover | Quarantine ambiguous rows; do not “repair” by guessing. |
| Residual | Honest unique-key JSON still needs 1.2 mediation. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/2.1/2.1-parser-boundaries`.

## Transfer

GraphQL and REST both ingest the same note — two grammars.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
