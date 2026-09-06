NOTES = {"alice": "secret"}
ANALYTICS = {"alice": "secret"}
SEARCH = {"alice": "secret"}


def reset() -> None:
    NOTES.clear()
    NOTES["alice"] = "secret"
    ANALYTICS.clear()
    ANALYTICS["alice"] = "secret"
    SEARCH.clear()
    SEARCH["alice"] = "secret"


def delete_account(user: str) -> None:
    NOTES.pop(user, None)
    ANALYTICS.pop(user, None)
    SEARCH.pop(user, None)


def body_retained(user: str):
    return ANALYTICS.get(user)


def search_retained(user: str):
    return SEARCH.get(user)
