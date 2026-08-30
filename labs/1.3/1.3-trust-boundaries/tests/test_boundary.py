"""Property tests for the local Module 1.3 trust-boundary fixture."""

from __future__ import annotations

import ast


def _ids(outcome: dict) -> set[str]:
    return {item["id"] for item in outcome["summaries"]}


def test_exact_scoped_worker_export_succeeds(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is True
    assert _ids(outcome) == {"nA1", "nA2"}


def test_ordinary_public_request_cannot_export(surface) -> None:
    outcome = surface.public_export({}, "tA", ["nA1", "nA2"], now=100)
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_service_label_without_internal_marker_is_not_provenance(surface) -> None:
    outcome = surface.public_export(
        {"X-SecureCollab-Service": "export-worker-1"},
        "tA",
        ["nA1", "nA2"],
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_public_metadata_cannot_construct_worker_provenance(surface) -> None:
    outcome = surface.public_export(
        {
            "X-SecureCollab-Internal": "worker",
            "X-SecureCollab-Service": "export-worker-1",
            "X-SecureCollab-Grant": "grant-a-exact",
        },
        "tA",
        ["nA1", "nA2"],
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == [], "public metadata is not worker provenance"


def test_unknown_worker_registration_denies(surface) -> None:
    outcome = surface.worker_export(
        "missing-registration",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_unknown_grant_denies(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "missing-grant",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_grant_is_bound_to_worker_identity(surface) -> None:
    outcome = surface.worker_export(
        "registration-b",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_grant_cannot_cross_tenant(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tB",
        ["nB1"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_grant_cannot_widen_same_tenant_object_scope(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2", "nA3"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_grant_cannot_change_action(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_body",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_expired_grant_denies(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-expired",
        "tA",
        ["nA1"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_grant_denies_at_exact_expiry_instant(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-expired",
        "tA",
        ["nA1"],
        action="export_summary",
        now=50,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_successful_grant_cannot_be_replayed(surface) -> None:
    first = surface.worker_export(
        "registration-a",
        "grant-a-single",
        "tA",
        ["nA1"],
        action="export_summary",
        now=100,
    )
    second = surface.worker_export(
        "registration-a",
        "grant-a-single",
        "tA",
        ["nA1"],
        action="export_summary",
        now=101,
    )
    assert first["allowed"] is True
    assert second["allowed"] is False
    assert second["summaries"] == []


def test_evidence_failure_denies_high_impact_effect(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-single",
        "tA",
        ["nA1"],
        action="export_summary",
        now=100,
        evidence_available=False,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []
    assert surface.GRANTS["grant-a-single"]["used"] is False


def test_duplicate_object_identifiers_are_malformed(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-single",
        "tA",
        ["nA1", "nA1"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is False
    assert outcome["summaries"] == []


def test_non_collection_object_scope_is_malformed(surface) -> None:
    for malformed_scope in (None, "nA1"):
        outcome = surface.worker_export(
            "registration-a",
            "grant-a-single",
            "tA",
            malformed_scope,
            action="export_summary",
            now=100,
        )
        assert outcome["allowed"] is False
        assert outcome["summaries"] == []


def test_allowed_output_projects_summaries_not_bodies(surface) -> None:
    outcome = surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    assert outcome["allowed"] is True
    assert all(set(item) == {"id", "summary"} for item in outcome["summaries"])
    assert "synthetic tenant A body" not in repr(outcome)


def test_decision_evidence_excludes_protected_and_bearer_values(surface) -> None:
    surface.worker_export(
        "registration-a",
        "grant-a-exact",
        "tA",
        ["nA1", "nA2"],
        action="export_summary",
        now=100,
    )
    serialized = repr(surface.EVENTS)
    assert "synthetic tenant A body" not in serialized
    assert "X-SecureCollab-Grant" not in serialized
    assert "grant-a-exact" not in serialized
    assert "raw-token" not in serialized
    assert all("object_count" in event for event in surface.EVENTS)


def test_control_independence_claim_names_shared_failures(surface) -> None:
    analysis = surface.control_dependencies()
    assert analysis["classification"] in {"correlated", "partially-independent"}
    assert set(analysis["shared"]) >= {"runtime", "operator"}
    assert analysis["edge_input"] != analysis["authority_input"]


def test_fixture_implementation_has_no_network_file_or_process_path(
    surface_source: str,
) -> None:
    tree = ast.parse(surface_source)
    imported_roots: set[str] = set()
    direct_calls: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".", 1)[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            direct_calls.add(node.func.id)

    assert imported_roots <= {"__future__", "typing"}
    assert direct_calls.isdisjoint(
        {"open", "exec", "eval", "compile", "__import__", "breakpoint"}
    )
