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
