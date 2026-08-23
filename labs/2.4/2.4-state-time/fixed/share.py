"""Fixed: same idempotency key does not duplicate the share side effect."""

_SHARES: list[str] = []
_SEEN: set[str] = set()


def reset() -> None:
    _SHARES.clear()
    _SEEN.clear()


def share_count() -> int:
    return len(_SHARES)


def share_note(note_id: str, idempotency_key: str | None = None) -> None:
    if idempotency_key:
        if idempotency_key in _SEEN:
            return
        _SEEN.add(idempotency_key)
    _SHARES.append(note_id)
