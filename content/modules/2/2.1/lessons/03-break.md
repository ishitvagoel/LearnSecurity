# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
**Forbidden outcome:** Parser differential: ACL tenant disagrees with stored tenant

**Authorized scope:** `labs/2.1/2.1-parser-boundaries` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable parse_note.py splits ACL vs storage on duplicate tenant.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Duplicate tenant keys in one object; split parse.

## Vulnerable fixture (local)

```python
"""Vulnerable: ACL parser (first tenant key) disagrees with store parser (JSON last key)."""

from __future__ import annotations

import json
import re


def _first_tenant(text: str) -> str:
    match = re.search(r'"tenant"\s*:\s*"([^"]*)"', text)
    return match.group(1) if match else ""


def _last_tenant(text: str) -> str:
    data = json.loads(text)
    value = data.get("tenant", "")
    return str(value)


def ingest_note(text: str) -> dict:
    acl = _first_tenant(text)
    stored = _last_tenant(text)
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": json.loads(text).get("body")}
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Two interpreters, two meanings of the same bytes. |
| Impact | tB body stored as tA or ACL sees tA while disk sees tB. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/2.1/2.1-parser-boundaries/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

GraphQL and REST both ingest the same note — two grammars.

## Non-goals

No live-target instructions. Synthetic data only.
