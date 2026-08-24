"""SecureCollab Phase 1 note store (synthetic)."""

from __future__ import annotations

USERS = {
    "alice": {"tenant": "tA", "role": "member"},
    "bob": {"tenant": "tB", "role": "member"},
    "adminA": {"tenant": "tA", "role": "admin"},
}

NOTES = {
    "n1": {"tenant": "tA", "body": "tenant-A-note"},
    "n2": {"tenant": "tB", "body": "tenant-B-note"},
}


def is_authenticated(user_id: str) -> bool:
    return user_id in USERS


def _same_tenant(user_id: str, note: dict) -> bool:
    return USERS[user_id]["tenant"] == note["tenant"]


def read_note(user_id: str, note_id: str) -> dict | None:
    """Fixed: object-level tenant check; unknown note denies (fail-safe)."""
    if not is_authenticated(user_id):
        return None
    note = NOTES.get(note_id)
    if note is None:
        return None
    if not _same_tenant(user_id, note):
        return None
    return note
