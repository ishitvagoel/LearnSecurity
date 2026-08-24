# 2.1 — Bytes, encodings, parsers, and interpreter boundaries (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.

## Property (start here)

If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.

## Attacker capabilities and trust assumptions

- **Attacker:** A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.
- **Trust:** One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.
Reject duplicate keys or compare acl_tenant == stored_tenant.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: duplicate tenant keys are rejected so both interpreters share one meaning."""

from __future__ import annotations

import json
import re


def _first_tenant(text: str) -> str:
    match = re.search(r'"tenant"\s*:\s*"([^"]*)"', text)
    return match.group(1) if match else ""


def _last_tenant(text: str) -> str:
    data = json.loads(text)
    return str(data.get("tenant", ""))


def ingest_note(text: str) -> dict:
    acl = _first_tenant(text)
    stored = _last_tenant(text)
    if not acl or acl != stored:
        return {"accepted": False, "acl_tenant": acl, "stored_tenant": stored, "body": None}
    data = json.loads(text)
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": data.get("body")}
```

## Why this restores the cell

Reject duplicate keys; pass one parse tree everywhere.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Pydantic v2 defaults are not “duplicate keys impossible.” stdlib json keeps the last key.

A WAF string filter for “tenant twice” fails on whitespace and Unicode escapes.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

GraphQL and REST both ingest the same note — two grammars.

## Residual risk

Honest unique-key JSON still needs 1.2 mediation.
