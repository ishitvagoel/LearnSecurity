"""Structurally fixed local boundary model for Module 1.3."""

from __future__ import annotations

from typing import Mapping


NOTES = {
    "nA1": {
        "id": "nA1",
        "tenant": "tA",
        "summary": "synthetic A one",
        "body": "synthetic tenant A body one",
    },
    "nA2": {
        "id": "nA2",
        "tenant": "tA",
        "summary": "synthetic A two",
        "body": "synthetic tenant A body two",
    },
    "nA3": {
        "id": "nA3",
        "tenant": "tA",
        "summary": "synthetic A three",
        "body": "synthetic tenant A body three",
    },
    "nB1": {
        "id": "nB1",
        "tenant": "tB",
        "summary": "synthetic B one",
        "body": "synthetic tenant B body one",
    },
}

WORKER_REGISTRY = {
    "registration-a": "export-worker-1",
    "registration-b": "export-worker-2",
}

# Each audit_ref is a non-bearer server-held identifier; worker_export never accepts it.
GRANTS = {
    "grant-a-exact": {
        "audit_ref": "capability-ref-01",
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1", "nA2"),
        "expires_at": 200,
        "used": False,
    },
    "grant-a-single": {
        "audit_ref": "capability-ref-02",
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1",),
        "expires_at": 200,
        "used": False,
    },
    "grant-a-expired": {
        "audit_ref": "capability-ref-03",
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1",),
        "expires_at": 50,
        "used": False,
    },
}

EVENTS: list[dict] = []
_CORRELATION_SEQUENCE = 0


def _outcome(allowed: bool, reason: str, summaries: list[dict]) -> dict:
    return {"allowed": allowed, "reason": reason, "summaries": summaries}


def _next_correlation_id() -> str:
    """Create a local server-side decision identifier, never from request data."""

    global _CORRELATION_SEQUENCE
    _CORRELATION_SEQUENCE += 1
    return f"boundary-decision-{_CORRELATION_SEQUENCE:04d}"


def _emit(
    *,
    caller_kind: str,
    principal_id: str,
    action: str,
    tenant_id: str,
    object_count: int,
    allowed: bool,
    reason: str,
    now: int,
    capability_ref: str | None = None,
) -> None:
    EVENTS.append(
        {
            "event": "export-boundary-decision",
            "model_version": "1.3-fixed",
            "caller_kind": caller_kind,
            "principal_id": principal_id,
            "action": action,
            "tenant_id": tenant_id,
            "object_count": object_count,
            "allowed": allowed,
            "reason": reason,
            "enforcement_point": "scoped-export-effect",
            "capability_ref": capability_ref,
            "correlation_id": _next_correlation_id(),
            "now": now,
        }
    )


def _deny(
    reason: str,
    *,
    caller_kind: str,
    principal_id: str,
    action: str,
    tenant_id: str,
    object_count: int,
    now: int,
    evidence_available: bool,
    capability_ref: str | None = None,
) -> dict:
    if evidence_available:
        _emit(
            caller_kind=caller_kind,
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            allowed=False,
            reason=reason,
            now=now,
            capability_ref=capability_ref,
        )
    return _outcome(False, reason, [])


def _object_count(note_ids: object) -> int:
    return len(note_ids) if isinstance(note_ids, (list, tuple)) else 0


def _well_formed(tenant_id: str, note_ids: object, action: str) -> bool:
    return (
        isinstance(tenant_id, str)
        and bool(tenant_id)
        and isinstance(action, str)
        and bool(action)
        and isinstance(note_ids, (list, tuple))
        and bool(note_ids)
        and all(isinstance(note_id, str) and note_id for note_id in note_ids)
        and len(set(note_ids)) == len(note_ids)
    )


def public_export(
    headers: Mapping[str, str],
    tenant_id: str,
    note_ids: object,
    *,
    now: int,
    evidence_available: bool = True,
) -> dict:
    """Public data remains public data; this adapter cannot create worker context."""

    del headers
    return _deny(
        "worker_entry_required",
        caller_kind="public",
        principal_id="public",
        action="export_summary",
        tenant_id=tenant_id,
        object_count=_object_count(note_ids),
        now=now,
        evidence_available=evidence_available,
    )


def worker_export(
    registration_handle: str,
    grant_id: str,
    tenant_id: str,
    note_ids: object,
    *,
    action: str,
    now: int,
    evidence_available: bool = True,
) -> dict:
    """Trusted adapter plus current narrow grant mediates the summary effect."""

    principal_id = WORKER_REGISTRY.get(registration_handle)
    object_count = _object_count(note_ids)

    if principal_id is None:
        return _deny(
            "unknown_worker",
            caller_kind="worker",
            principal_id="unknown",
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=evidence_available,
        )
    if not evidence_available:
        return _outcome(False, "evidence_unavailable", [])
    grant = GRANTS.get(grant_id)
    capability_ref = grant["audit_ref"] if grant is not None else None

    if not _well_formed(tenant_id, note_ids, action):
        return _deny(
            "malformed_scope",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )

    if grant is None:
        return _deny(
            "unknown_grant",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
        )
    if grant["worker_id"] != principal_id:
        return _deny(
            "worker_mismatch",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )
    if grant["action"] != action:
        return _deny(
            "action_mismatch",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )
    if grant["tenant_id"] != tenant_id:
        return _deny(
            "tenant_mismatch",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )
    if set(grant["note_ids"]) != set(note_ids) or len(grant["note_ids"]) != len(note_ids):
        return _deny(
            "object_scope_mismatch",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )
    if grant["used"]:
        return _deny(
            "grant_consumed",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )
    if now >= grant["expires_at"]:
        return _deny(
            "grant_expired",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )

    notes = [NOTES.get(note_id) for note_id in note_ids]
    if any(note is None or note["tenant"] != tenant_id for note in notes):
        return _deny(
            "stored_scope_mismatch",
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=object_count,
            now=now,
            evidence_available=True,
            capability_ref=capability_ref,
        )

    summaries = [
        {"id": note["id"], "summary": note["summary"]}
        for note in notes
        if note is not None
    ]
    grant["used"] = True
    _emit(
        caller_kind="worker",
        principal_id=principal_id,
        action=action,
        tenant_id=tenant_id,
        object_count=object_count,
        allowed=True,
        reason="scoped_grant_consumed",
        now=now,
        capability_ref=capability_ref,
    )
    return _outcome(True, "scoped_grant_consumed", summaries)


def control_dependencies() -> dict:
    """Honest local dependency analysis; logical controls still share a process."""

    return {
        "edge_input": "public-adapter-caller-kind",
        "authority_input": "server-held-grant-state",
        "shared": ["runtime", "operator"],
        "classification": "partially-independent",
    }
