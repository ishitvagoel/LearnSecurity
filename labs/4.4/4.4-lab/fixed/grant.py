GRANTS = {("bob", "n1"): True}

def reset():
    GRANTS.clear(); GRANTS[("bob", "n1")] = True

def can_read(user: str, note_id: str) -> bool:
    return bool(GRANTS.get((user, note_id)))
