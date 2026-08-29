"""Intentionally vulnerable SecureCollab authority fixture.

This local module is course material. It uses synthetic data and performs no I/O.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

POLICY_VERSION = "authority-phase1-vulnerable"

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


def is_authenticated(user_id: str) -> bool:
    """Vulnerable: existence is treated as current active authority."""

    return user_id in USERS


def authorize(
    user_id: str,
    action: str,
    object_id: str | None = None,
    *,
    target_tenant: str | None = None,
    approver_ids: Iterable[str] = (),
) -> dict[str, Any]:
    """Vulnerable policy with ambient, unscoped, stale, and fail-open rules."""

    if not is_authenticated(user_id):
        return _decision(False, "unknown_identity", user_id, action, object_id)

    user = USERS[user_id]

    if action in {"note:read-body", "note:list-summary"}:
        return _decision(True, "authenticated_user", user_id, action, object_id)

    if action == "note:delete":
        return _decision(
            user["role"] == "admin",
            "global_admin_role",
            user_id,
            action,
            object_id,
        )

    if action == "tenant:bulk-export":
        approvals = list(approver_ids)
        allowed = user["role"] == "admin" and bool(approvals)
        return _decision(allowed, "one_approval_is_enough", user_id, action, target_tenant)

    return _decision(True, "unknown_action_fail_open", user_id, action, object_id)


def read_note(user_id: str, note_id: str) -> dict[str, str] | None:
    decision = authorize(user_id, "note:read-body", note_id)
    if not decision["allowed"]:
        return None
    note = NOTES.get(note_id)
    return dict(note) if note is not None else None


def list_notes(user_id: str) -> list[dict[str, str]]:
    decision = authorize(user_id, "note:list-summary")
    if not decision["allowed"]:
        return []
    return [
        {"id": note["id"], "tenant": note["tenant"], "title": note["title"]}
        for note in NOTES.values()
    ]


def delete_note(user_id: str, note_id: str) -> bool:
    decision = authorize(user_id, "note:delete", note_id)
    if not decision["allowed"] or note_id not in NOTES:
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
