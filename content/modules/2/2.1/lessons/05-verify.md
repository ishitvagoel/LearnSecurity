# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Parser differential: ACL tenant disagrees with stored tenant |
| Failure | Fail closed: Reject duplicate keys; pass one parse tree everywhere |

Lab tests: `test_parser.py` under `labs/2.1/2.1-parser-boundaries`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Parser differential: ACL tenant disagrees with stored tenant`
- `--impl fixed`: **pass**

CLEAN accepted with tA; AMBIGUOUS rejected or consistent.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

GraphQL and REST both ingest the same note — two grammars.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
