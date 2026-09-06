NOTES = {
    "n1": {"tenant": "acme", "owner": "alice"},
    "n2": {"tenant": "acme", "owner": "alice"},
    "n3": {"tenant": "clinic", "owner": "carol"},
}
USERS = {
    "bob": {"tenant": "acme", "role": "member"},
    "alice": {"tenant": "acme", "role": "owner"},
    "carol": {"tenant": "clinic", "role": "owner"},
    "eve": {"tenant": "clinic", "role": "admin"},
}
GRANTS = {("bob", "n1"): True}


def reset() -> None:
    GRANTS.clear()
    GRANTS[("bob", "n1")] = True


def can_read(user: str, note_id: str) -> bool:
    note = NOTES.get(note_id)
    principal = USERS.get(user)
    if not note or not principal:
        return False
    if principal["tenant"] != note["tenant"]:
        return False
    if note["owner"] == user:
        return True
    return bool(GRANTS.get((user, note_id)))
