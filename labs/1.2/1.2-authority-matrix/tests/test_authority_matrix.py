"""Property tests for the local Module 1.2 authority fixture."""

from __future__ import annotations

import ast


def test_same_tenant_member_can_read_note_body(authority) -> None:
    note = authority.read_note("alice", "nA1")
    assert note is not None
    assert note["body"] == "synthetic tenant A body"


def test_cross_tenant_member_cannot_read_note_body(authority) -> None:
    note = authority.read_note("bob", "nA1")
    assert note is None, "authentication is not authority over another tenant's note"


def test_list_releases_only_same_tenant_summaries(authority) -> None:
    visible = authority.list_notes("alice")
    assert {note["id"] for note in visible} == {"nA1", "nA2"}
    assert all(note["tenant"] == "tA" for note in visible)
    assert all("body" not in note for note in visible)


def test_scoped_admin_can_delete_same_tenant_note(authority) -> None:
    assert authority.delete_note("adminA", "nA2") is True
    assert "nA2" not in authority.NOTES


def test_ordinary_member_cannot_delete_same_tenant_note(authority) -> None:
    before = dict(authority.NOTES["nA1"])
    assert authority.delete_note("alice", "nA1") is False
    assert authority.NOTES["nA1"] == before


def test_scoped_admin_cannot_delete_cross_tenant_note(authority) -> None:
    before = dict(authority.NOTES["nB1"])
    assert authority.delete_note("adminA", "nB1") is False
    assert authority.NOTES["nB1"] == before


def test_revoked_membership_removes_note_authority(authority) -> None:
    assert authority.is_authenticated("revokedA") is True
    assert authority.read_note("revokedA", "nA1") is None


def test_unknown_identity_and_object_deny(authority) -> None:
    assert authority.read_note("nobody", "nA1") is None
    assert authority.read_note("alice", "missing") is None
    decision = authority.authorize("alice", "note:read-body", "missing")
    assert decision["allowed"] is False


def test_unknown_action_fails_safe(authority) -> None:
    decision = authority.authorize("alice", "note:publish", "nA1")
    assert decision["allowed"] is False
    assert decision["reason"] != ""


def test_bulk_export_requires_two_distinct_current_scoped_approvals(authority) -> None:
    decision = authority.export_decision("adminA", "tA", ["adminA"])
    assert decision["allowed"] is False


def test_duplicate_approval_does_not_create_separation(authority) -> None:
    decision = authority.export_decision("adminA", "tA", ["adminA", "adminA"])
    assert decision["allowed"] is False


def test_cross_tenant_or_retired_approval_does_not_count(authority) -> None:
    cross_tenant = authority.export_decision("adminA", "tA", ["adminA", "adminB"])
    retired = authority.export_decision(
        "adminA", "tA", ["adminA", "retiredAdminA"]
    )
    assert cross_tenant["allowed"] is False
    assert retired["allowed"] is False


def test_two_distinct_current_scoped_admins_can_approve_export(authority) -> None:
    decision = authority.export_decision("adminA", "tA", ["adminA", "adminA2"])
    assert decision["allowed"] is True


def test_export_initiator_must_belong_to_target_tenant(authority) -> None:
    decision = authority.export_decision("adminA", "tB", ["adminB", "adminB2"])
    assert decision["allowed"] is False


def test_decision_evidence_does_not_copy_protected_values(authority) -> None:
    decision = authority.authorize("bob", "note:read-body", "nA1")
    serialized = repr(decision)
    assert "synthetic tenant A body" not in serialized
    assert "password" not in serialized.lower()
    assert "token" not in serialized.lower()


def test_fixture_has_no_network_or_process_execution_path(authority_source: str) -> None:
    tree = ast.parse(authority_source)
    imported_roots: set[str] = set()
    direct_calls: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".", 1)[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            direct_calls.add(node.func.id)

    assert imported_roots <= {"__future__", "collections", "typing"}
    assert direct_calls.isdisjoint(
        {"open", "exec", "eval", "compile", "__import__", "breakpoint"}
    )
