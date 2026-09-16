"""Fixed: duplicate tenant keys are rejected so every reader shares one meaning.

The first attempt at this fix collected every occurrence of the tenant key
with a second regex (`re.findall`), the same technology the ACL-side reader
already used, just applied more thoroughly. That was itself a real bug, not
a hypothetical one: a regex matching `"tenant"\\s*:\\s*"([^"]*)"` only
recognizes a *string-typed* value in quotes, so `{"tenant":1,"tenant":"tA"}`
has one occurrence the regex cannot see at all -- the integer `1` -- and the
"collect every occurrence" logic silently believed there was only one
occurrence to check. A regex is always an approximation of a grammar; it can
never be a substitute for actually running the grammar's own parser.

The structural fix is to stop approximating JSON with a second, fallible
reader, and instead ask CPython's own `json` module for every occurrence,
using its `object_pairs_hook` -- a standard, documented mechanism that
receives every key/value pair in an object literal, in source order, before
the last-wins collapsing that a plain `json.loads(text)` call would perform.
This is Lesson 04's Candidate B done correctly: one authoritative reader,
consulted for the full truth about every occurrence, rather than two
readers whose agreement is checked by comparing summaries each one has
already collapsed.
"""

from __future__ import annotations

import json


def _tenant_occurrences(text: str) -> list[object]:
    """Every value ever assigned to a top-level "tenant" key, in the order
    the bytes contain them, exactly as the real JSON parser sees them --
    including non-string values and keys written with an escape sequence,
    neither of which a regex over the raw text can reliably recognize."""
    occurrences: list[object] = []

    def collect(pairs: list[tuple[str, object]]) -> dict:
        occurrences.extend(value for key, value in pairs if key == "tenant")
        return dict(pairs)

    json.loads(text, object_pairs_hook=collect)
    return occurrences


def ingest_note(text: str) -> dict:
    try:
        occurrences = _tenant_occurrences(text)
    except json.JSONDecodeError:
        # Malformed JSON syntax is not a duplicate-key disagreement, but it
        # is exactly as much "no single meaning was established" as a
        # disagreement is, and it must fail closed for the same reason.
        return {"accepted": False, "acl_tenant": "", "stored_tenant": "", "body": None}

    # Compare the actual values, not a stringified form -- 1 and "1" are
    # different JSON values, and treating them as the same after both get
    # converted to the string "1" would be a new, quieter version of the
    # exact mistake this fix exists to close.
    one_meaning = bool(occurrences) and all(v == occurrences[0] for v in occurrences[1:])
    reported = str(occurrences[0]) if occurrences else ""
    if not one_meaning:
        return {"accepted": False, "acl_tenant": reported, "stored_tenant": reported, "body": None}

    data = json.loads(text)
    return {"accepted": True, "acl_tenant": reported, "stored_tenant": reported, "body": data.get("body")}
