# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Poster (tB), ACL checker, storage writer, later reader |
| Objects | JSON bytes, ACL tenant, stored tenant, note body |
| Actions | ingest_note, parse, persist |
| Channels | HTTP body, worker re-parse, DB jsonb |
| TCB | A single parse result object used for both ACL and persist. |
| Untrusted | Duplicate keys, overlong UTF-8, NFC vs NFD names |
| State / time | The same bytes parsed tomorrow by a new library version. |
| 1.1 cell | Confidentiality (cross-tenant) caused by *disagreement*, not by missing login. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| poster tA | CLEAN json | ingest | allow |
| poster tB | duplicate tenant keys | ingest | deny |
| worker | re-parse stored bytes | must-match | allow-only-if-same |
| reader tA | stored body | read | 1.2 cell |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/2.1/2.1-parser-boundaries` file `parse_note.py`.

## Transfer

GraphQL and REST both ingest the same note — two grammars.

## Residual risk

Honest unique-key JSON still needs 1.2 mediation.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
