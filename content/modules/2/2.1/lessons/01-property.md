# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
**Mechanism (not the property):** Pydantic v2 defaults are not “duplicate keys impossible.” stdlib json keeps the last key.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 2.1 |
|---|---|
| Root cause | Two interpreters, two meanings of the same bytes. |
| Preconditions | Duplicate tenant keys in one object; split parse. |
| Impact (1.1 cell) | Confidentiality (cross-tenant) caused by *disagreement*, not by missing login. — tB body stored as tA or ACL sees tA while disk sees tB. |
| Prevention | Reject duplicate keys; pass one parse tree everywhere. |
| Detection | Parse-error metric; differential test corpus in CI. |
| Recovery | Quarantine ambiguous rows; do not “repair” by guessing. |

## Framework defaults vs application guarantees

Pydantic v2 defaults are not “duplicate keys impossible.” stdlib json keeps the last key.

## Mechanism limits and bypasses

A WAF string filter for “tenant twice” fails on whitespace and Unicode escapes.

UTF-16 body, YAML, multipart, GraphQL variables.

## Residual risk

Honest unique-key JSON still needs 1.2 mediation.

## Practice

Write the two-parser diagram for ACL vs storage on the lab’s AMBIGUOUS blob.

Run `labs/2.1/2.1-parser-boundaries` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

GraphQL and REST both ingest the same note — two grammars.

Clinic booking: duplicate patient_id keys.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
