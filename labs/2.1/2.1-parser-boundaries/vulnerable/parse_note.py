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
