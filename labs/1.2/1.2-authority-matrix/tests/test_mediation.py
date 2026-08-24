"""Forbidden outcome: authenticated user of tenant B reads tenant A's note."""


def test_same_tenant_member_can_read(notes) -> None:
    got = notes.read_note("alice", "n1")
    assert got is not None
    assert got["body"] == "tenant-A-note"


def test_cross_tenant_read_is_denied(notes) -> None:
    got = notes.read_note("bob", "n1")
    assert got is None, "complete mediation: login is not permission on another tenant's note"


def test_unknown_note_denies(notes) -> None:
    assert notes.read_note("alice", "missing") is None


def test_unauthenticated_denies(notes) -> None:
    assert notes.read_note("nobody", "n1") is None
