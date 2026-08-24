"""Vulnerable: every share_note call performs the side effect (retry duplicates)."""

_SHARES: list[str] = []


def reset() -> None:
    _SHARES.clear()


def share_count() -> int:
    return len(_SHARES)


def share_note(note_id: str, idempotency_key: str | None = None) -> None:
    _SHARES.append(note_id)
