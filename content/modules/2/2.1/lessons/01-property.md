# 2.1-LO-01 — Bytes are not characters; parsers are not the property

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** Unicode Standard (final, version as pinned); ASVS 5.0.0 (final) V5 input — chapter-level. Awareness lists are regression, not the outline.

## Property (start here)

For SecureCollab note ingest: **two parsers that see the same bytes must agree on `tenant`**, or the request is denied. “JSON.parse succeeded” is a mechanism.

## Attacker capabilities and trust assumptions

- **Attacker:** a member who can POST note JSON to the local lab API; they may send duplicate keys or mixed encodings.
- **Trust:** CPython `json.loads` is in the TCB only if it is the **only** parser. A second scanner (regex, JS `JSON.parse`, jq) is another interpreter.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | This module |
|---|---|
| Root cause | Two grammars on one byte string (duplicate keys, UTF-8 vs Latin-1) |
| Preconditions | Local fixture; synthetic JSON |
| Impact | 1.2 cell uses tenant A while storage uses tenant B (1.1 confidentiality) |
| Prevention | One canonical parser; reject ambiguity |
| Detection | Log parse rejects without bodies |
| Recovery | Quarantine ambiguous notes; do not “best effort” store |

## Framework defaults vs application guarantees

FastAPI will parse JSON for you. That default is **not** “no parser differential with the Next.js client.”

## Practice

Write one invariant sentence a test could fail.

## Transfer

CSV for bulk invite: two CSV libraries on commas-in-quotes — 6.4 territory, same property family.
