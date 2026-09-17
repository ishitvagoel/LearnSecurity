"""Vulnerable: ACL parser (first tenant key) disagrees with store parser (JSON last key).

C1: the same request bytes must yield one company meaning for both the
who-is-allowed check and the stored row. This fixture's two readers are
two different technologies that happen to both look at "tenant" -- a
regex-based first-key scan, and CPython's own last-key-wins JSON parser --
and `ingest_note` never checks whether they agree.
"""

from __future__ import annotations

import json
import re

TENANT_RE = re.compile(r'"tenant"\s*:\s*"([^"]*)"')


def _first_tenant(text: str) -> str:
    match = TENANT_RE.search(text)
    return match.group(1) if match else ""


def _last_tenant(text: str) -> str:
    data = json.loads(text)
    value = data.get("tenant", "")
    return str(value)


def ingest_note(text: str) -> dict:
    # Malformed JSON syntax is a different axis from the security property
    # this fixture is naive about (whether two readers of well-formed JSON
    # agree). Even a naive implementation should not crash its caller with
    # an unhandled exception on garbage input -- that is ordinary exception
    # hygiene, not the fix this module teaches.
    try:
        acl = _first_tenant(text)
        stored = _last_tenant(text)
        body = json.loads(text).get("body")
    except json.JSONDecodeError:
        return {"accepted": False, "acl_tenant": "", "stored_tenant": "", "body": None}
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": body}
