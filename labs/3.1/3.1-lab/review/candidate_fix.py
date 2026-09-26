"""Seeded review fixture -- NOT wired into pytest, NOT the shipped fix.

This is a snapshot of a hypothetical pull request against `fixed/app.py`,
written to be read and reviewed, per lessons/08-review.md. A teammate
describes it as: "Added an audit-export sink for the compliance team's
retention system, reusing our existing classification setup." It is
deliberately NOT `fixed/app.py`: it seeds several issues at differing
severity, plus one detail a reviewer might flag that is not actually a
defect for this module's property. Do not import or run this file; it
exists for lessons/08-review.md's reading exercise only.
"""
from __future__ import annotations

CLASSIFICATION: dict[str, str] = {
    "note_body": "confidential",
    "session_token": "confidential",
    "note_id": "internal",
    "company_id": "internal",
    "event": "internal",
}

SINK_POLICY: dict[str, set[str]] = {
    "application_log": {"internal"},
    "error_dump": {"internal"},
    "audit_export": {"internal", "confidential"},
}

_LOG_LINES: list[str] = []
_AUDIT_EXPORTS: list[dict] = []


def _redact(context: dict, sink: str = "application_log") -> dict:
    allowed = SINK_POLICY.get(sink, set())
    out: dict = {}
    for key, value in context.items():
        level = CLASSIFICATION.get(key, "internal")
        out[key] = value if level in allowed else f"[redacted-{level}]"
    return out


def log_event(event: str, context: dict) -> None:
    safe = _redact(context, "application_log")
    rendered = " ".join(f"{k}={v}" for k, v in safe.items())
    _LOG_LINES.append(f"{event}: {rendered}")


def write_audit_export(context: dict) -> None:
    """Full audit trail for the compliance team's retention system."""
    _AUDIT_EXPORTS.append(dict(context))


def note_read_handler(note_id: str, context: dict) -> None:
    if note_id in ("note_a", "note_b"):
        write_audit_export(context)
    log_event("note_read", context)
