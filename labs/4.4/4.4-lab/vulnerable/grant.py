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
    if any(u == user for (u, _n) in GRANTS):
        return True
    role = USERS.get(user, {}).get("role")
    return role in ("owner", "admin")
