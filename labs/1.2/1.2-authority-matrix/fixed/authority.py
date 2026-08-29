"""Structurally fixed SecureCollab authority fixture.

This local module is course material. It uses synthetic data and performs no I/O.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

POLICY_VERSION = "authority-phase1-v2"

USERS: dict[str, dict[str, Any]] = {
    "alice": {"tenant": "tA", "role": "member", "active": True},
    "bob": {"tenant": "tB", "role": "member", "active": True},
    "adminA": {"tenant": "tA", "role": "admin", "active": True},
    "adminA2": {"tenant": "tA", "role": "admin", "active": True},
    "adminB": {"tenant": "tB", "role": "admin", "active": True},
    "adminB2": {"tenant": "tB", "role": "admin", "active": True},
    "revokedA": {"tenant": "tA", "role": "member", "active": False},
    "retiredAdminA": {"tenant": "tA", "role": "admin", "active": False},
}

NOTES: dict[str, dict[str, str]] = {
    "nA1": {
        "id": "nA1",
        "tenant": "tA",
        "title": "A planning note",
        "body": "synthetic tenant A body",
    },
    "nA2": {
        "id": "nA2",
        "tenant": "tA",
        "title": "A review note",
        "body": "second synthetic tenant A body",
    },
    "nB1": {
        "id": "nB1",
        "tenant": "tB",
        "title": "B planning note",
        "body": "synthetic tenant B body",
    },
}


def _decision(
    allowed: bool,
    reason: str,
    user_id: str,
    action: str,
    object_id: str | None,
) -> dict[str, Any]:
    return {
        "allowed": allowed,
        "reason": reason,
        "subject_id": user_id,
        "action": action,
        "object_id": object_id,
        "policy_version": POLICY_VERSION,
    }


def _active_user(user_id: str) -> dict[str, Any] | None:
    user = USERS.get(user_id)
    if user is None or user["active"] is not True:
        return None
    return user


def _active_admin(user_id: str, tenant: str) -> bool:
    user = _active_user(user_id)
    return bool(user and user["role"] == "admin" and user["tenant"] == tenant)


def is_authenticated(user_id: str) -> bool:
    """Identity evidence is distinct from current authorization state."""

    return user_id in USERS


def authorize(
    user_id: str,
    action: str,
    object_id: str | None = None,
    *,
    target_tenant: str | None = None,
    approver_ids: Iterable[str] = (),
) -> dict[str, Any]:
    """Resolve current server-side facts and allow only explicit policy cells."""

    user = _active_user(user_id)
    if user is None:
        return _decision(False, "subject_not_active", user_id, action, object_id)

    if action == "note:list-summary":
        return _decision(True, "active_tenant_member", user_id, action, user["tenant"])

    if action in {"note:read-body", "note:delete"}:
        note = NOTES.get(object_id or "")
        if note is None:
            return _decision(False, "object_not_found", user_id, action, object_id)
        if note["tenant"] != user["tenant"]:
            return _decision(False, "tenant_mismatch", user_id, action, object_id)
        if action == "note:delete" and user["role"] != "admin":
            return _decision(False, "action_not_granted", user_id, action, object_id)
        return _decision(True, "explicit_same_tenant_rule", user_id, action, object_id)

    if action == "tenant:bulk-export":
        if target_tenant is None or target_tenant != user["tenant"]:
            return _decision(False, "tenant_mismatch", user_id, action, target_tenant)
        if user["role"] != "admin":
            return _decision(False, "action_not_granted", user_id, action, target_tenant)

        distinct_approvers = set(approver_ids)
        if len(distinct_approvers) < 2:
            return _decision(False, "two_distinct_approvals_required", user_id, action, target_tenant)
        if not all(_active_admin(approver_id, target_tenant) for approver_id in distinct_approvers):
            return _decision(False, "approver_not_current_or_scoped", user_id, action, target_tenant)
        return _decision(True, "two_current_scoped_approvals", user_id, action, target_tenant)

    return _decision(False, "unknown_action", user_id, action, object_id)


def read_note(user_id: str, note_id: str) -> dict[str, str] | None:
    decision = authorize(user_id, "note:read-body", note_id)
    if not decision["allowed"]:
        return None
    return dict(NOTES[note_id])


def list_notes(user_id: str) -> list[dict[str, str]]:
    decision = authorize(user_id, "note:list-summary")
    if not decision["allowed"]:
        return []
    tenant = str(decision["object_id"])
    return [
        {"id": note["id"], "tenant": note["tenant"], "title": note["title"]}
        for note in NOTES.values()
        if note["tenant"] == tenant
    ]


def delete_note(user_id: str, note_id: str) -> bool:
    decision = authorize(user_id, "note:delete", note_id)
    if not decision["allowed"]:
        return False
    del NOTES[note_id]
    return True


def export_decision(
    user_id: str,
    target_tenant: str,
    approver_ids: Iterable[str],
) -> dict[str, Any]:
    return authorize(
        user_id,
        "tenant:bulk-export",
        target_tenant=target_tenant,
        approver_ids=approver_ids,
    )
