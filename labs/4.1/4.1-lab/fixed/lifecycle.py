SESSIONS = {"alice": True}
DELETED = set()

def reset():
    SESSIONS.clear(); SESSIONS["alice"] = True
    DELETED.clear()

def delete_user(user: str) -> None:
    DELETED.add(user)
    SESSIONS.pop(user, None)

def session_valid(user: str) -> bool:
    if user in DELETED:
        return False
    return bool(SESSIONS.get(user))
