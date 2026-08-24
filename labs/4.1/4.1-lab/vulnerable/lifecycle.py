SESSIONS = {"alice": True}
DELETED = set()

def reset():
    SESSIONS.clear(); SESSIONS["alice"] = True
    DELETED.clear()

def delete_user(user: str) -> None:
    DELETED.add(user)

def session_valid(user: str) -> bool:
    return bool(SESSIONS.get(user))
