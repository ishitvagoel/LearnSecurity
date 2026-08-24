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


def read_note(user_id: str, note_id: str) -> dict | None:
    """Vulnerable: login (ambient current_user) is treated as authorization."""
    if not is_authenticated(user_id):
        return None
    return NOTES.get(note_id)
