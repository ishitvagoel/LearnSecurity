"""Fixed: duplicate tenant keys are rejected so every reader shares one meaning.

The structural fix has two parts, not one, and the second is the quieter
of the two:

1. Refuse on disagreement rather than guess which key "the user meant" --
   last-wins and first-wins are both guesses, and neither is a security
   decision.
2. Check EVERY occurrence of the tenant key against every other one, not
   only the first against the last. Comparing only the endpoints has a
   real gap: a three-key object whose first and last values happen to
   coincide (`tA ... tC ... tA`) passes a first-vs-last check even though
   a middle value plainly disagreed. The disagreement was never resolved;
   it was silently dropped because neither reader looked at it. Checking
   the full set of occurrences is what actually enforces C1.
"""

from __future__ import annotations

import json
import re

TENANT_RE = re.compile(r'"tenant"\s*:\s*"([^"]*)"')


def _all_tenant_occurrences(text: str) -> list[str]:
    """Every 'tenant' value, in the order the bytes actually contain them --
    not only the first (a regex scan) or the last (CPython's json.loads)."""
    return TENANT_RE.findall(text)


def _last_tenant(text: str) -> str:
    data = json.loads(text)
    return str(data.get("tenant", ""))


def ingest_note(text: str) -> dict:
    occurrences = _all_tenant_occurrences(text)
    acl = occurrences[0] if occurrences else ""
    stored = _last_tenant(text)
    one_meaning = bool(occurrences) and len(set(occurrences)) == 1 and acl == stored
    if not one_meaning:
        return {"accepted": False, "acl_tenant": acl, "stored_tenant": stored, "body": None}
    data = json.loads(text)
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": data.get("body")}
