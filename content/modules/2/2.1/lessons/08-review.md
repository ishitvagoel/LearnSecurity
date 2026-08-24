# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
Review `labs/2.1/2.1-parser-boundaries/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/2.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): json.loads used twice; ACL on first, store on second
- Seeded smell (label it yourself): Comment “JSON can’t have duplicate keys” (RFC 8259 recommends but parsers differ)
- Seeded smell (label it yourself): No corpus test for duplicate keys
- Seeded smell (label it yourself): Normalizing display names as a substitute for tenant ids

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Encoding is a crypto problem
- One parser is as good as another
- Validation equals canonicalization

## Practice

Write three review notes. Do not open the keys file.

## Transfer

GraphQL and REST both ingest the same note — two grammars.
