"""Intentionally vulnerable local boundary model for Module 1.3."""

from __future__ import annotations

from typing import Mapping, Sequence


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

GRANTS = {
    "grant-a-exact": {
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1", "nA2"),
        "expires_at": 200,
        "used": False,
    },
    "grant-a-single": {
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1",),
        "expires_at": 200,
        "used": False,
    },
    "grant-a-expired": {
        "worker_id": "export-worker-1",
        "tenant_id": "tA",
        "action": "export_summary",
        "note_ids": ("nA1",),
        "expires_at": 50,
        "used": False,
    },
}

EVENTS: list[dict] = []


def _outcome(allowed: bool, reason: str, summaries: list[dict]) -> dict:
    return {"allowed": allowed, "reason": reason, "summaries": summaries}


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
) -> None:
    EVENTS.append(
        {
            "event": "export-boundary-decision",
            "model_version": "1.3-vulnerable",
            "caller_kind": caller_kind,
            "principal_id": principal_id,
            "action": action,
            "tenant_id": tenant_id,
            "object_count": object_count,
            "allowed": allowed,
            "reason": reason,
            "enforcement_point": "shared-export-helper",
            "now": now,
        }
    )


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


def _summaries(tenant_id: str, note_ids: Sequence[str]) -> list[dict]:
    return [
        {"id": note["id"], "summary": note["summary"]}
        for note_id in note_ids
        if (note := NOTES.get(note_id)) is not None and note["tenant"] == tenant_id
    ]


def public_export(
    headers: Mapping[str, str],
    tenant_id: str,
    note_ids: object,
    *,
    now: int,
    evidence_available: bool = True,
) -> dict:
    """Wrongly lets two correlated reads of public metadata establish provenance."""

    edge_allows = headers.get("X-SecureCollab-Internal") == "worker"
    application_allows = headers.get("X-SecureCollab-Internal") == "worker"
    principal_id = headers.get("X-SecureCollab-Service", "public")

    if not edge_allows or not application_allows or principal_id not in WORKER_REGISTRY.values():
        if evidence_available:
            _emit(
                caller_kind="public",
                principal_id="public",
                action="export_summary",
                tenant_id=tenant_id,
                object_count=_object_count(note_ids),
                allowed=False,
                reason="not_internal",
                now=now,
            )
        return _outcome(False, "not_internal", [])

    if not _well_formed(tenant_id, note_ids, "export_summary"):
        return _outcome(False, "malformed_scope", [])

    summaries = _summaries(tenant_id, note_ids)
    if evidence_available:
        _emit(
            caller_kind="worker",
            principal_id=principal_id,
            action="export_summary",
            tenant_id=tenant_id,
            object_count=_object_count(note_ids),
            allowed=True,
            reason="two_header_checks_passed",
            now=now,
        )
    return _outcome(True, "two_header_checks_passed", summaries)


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
    """Wrongly treats registration plus any known grant as ambient export ability."""

    principal_id = WORKER_REGISTRY.get(registration_handle)
    if principal_id is None:
        return _outcome(False, "unknown_worker", [])
    if grant_id not in GRANTS:
        return _outcome(False, "unknown_grant", [])
    if not _well_formed(tenant_id, note_ids, action):
        return _outcome(False, "malformed_scope", [])

    summaries = _summaries(tenant_id, note_ids)
    if evidence_available:
        _emit(
            caller_kind="worker",
            principal_id=principal_id,
            action=action,
            tenant_id=tenant_id,
            object_count=_object_count(note_ids),
            allowed=True,
            reason="registered_worker_has_known_grant",
            now=now,
        )
    return _outcome(True, "registered_worker_has_known_grant", summaries)


def control_dependencies() -> dict:
    """The deliberately false independence claim exposed for review."""

    return {
        "edge_input": "request:X-SecureCollab-Internal",
        "authority_input": "request:X-SecureCollab-Internal",
        "shared": ["request-parser", "routing-configuration", "runtime", "operator"],
        "classification": "independent",
    }
