"""Tests for the Phase 3 CI threat-model gate. Run with

    python3 -m pytest labs/3.2/3.2-lab/tests --impl vulnerable
    python3 -m pytest labs/3.2/3.2-lab/tests --impl fixed

The first command must fail on most of these; the second must pass all of
them. Every payload below is synthetic fixture data — fake threat ids, fake
owners, fake flow names — not a scan of any real system.
"""

from __future__ import annotations

import copy

COMPLETE_MODEL = {
    "threats": [
        {
            "id": "cross-tenant-read",
            "owner": "authz",
            "trigger": "new-share-path",
            "priority": 1,
            "mitigation": (
                "deny-by-default company check in 4.4's can_read matrix "
                "before any note body leaves the API"
            ),
            "revisited_after": [],
        },
        {
            "id": "hostile-browser",
            "owner": "web",
            "trigger": "new-client-surface",
            "priority": 2,
            "mitigation": (
                "server derives company from the session lookup; client-"
                "supplied fields are never trusted for identity"
            ),
            "revisited_after": [],
        },
        {
            "id": "stolen-worker",
            "owner": "platform",
            "trigger": "new-worker-identity",
            "priority": 3,
            "mitigation": (
                "worker adapter issues a short-lived, scoped grant; "
                "redelivery re-checks grant state before acting"
            ),
            "revisited_after": [],
        },
    ],
    "declared_flows": [
        "browser-share-request",
        "member-note-read",
        "worker-share-redelivery",
    ],
    "trigger_events": [],
}


def _model() -> dict:
    return copy.deepcopy(COMPLETE_MODEL)


def _gate(client, model: dict, scanner_green: bool, scanner_findings: list[str] | None = None) -> dict:
    client.put("/threat-model", json=model)
    resp = client.post(
        "/ci/gate",
        json={"scanner_green": scanner_green, "scanner_findings": scanner_findings or []},
    )
    assert resp.status_code == 200
    return resp.json()


def test_complete_model_passes_on_green_scan(client) -> None:
    """Normal case: a model with all three always-name threats, every
    required flow traced, and no fired trigger passes even though the
    scanner is green — because it would also pass with the scanner red."""
    result = _gate(client, _model(), scanner_green=True)
    assert result["gate"] == "pass"
    assert result["reasons"] == []


def test_green_scanner_missing_cross_tenant_read_fails(client) -> None:
    """Forbidden outcome: a green scan must not let a model that omits
    cross-tenant-read pass. This is the module's core property."""
    model = _model()
    model["threats"] = [t for t in model["threats"] if t["id"] != "cross-tenant-read"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("cross-tenant-read" in reason for reason in result["reasons"])


def test_mandatory_threat_without_owner_fails(client) -> None:
    """Malformed/failure case: an id with no owner is not a checkable row,
    whatever the scanner says."""
    model = _model()
    model["threats"][0]["owner"] = ""
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("no owner" in reason for reason in result["reasons"])


def test_untraced_worker_flow_fails_even_with_all_ids_present(client) -> None:
    """Boundary case: every always-name id can be present by string alone
    while the diagram still never traces the path that makes
    stolen-worker meaningful. An incomplete trust-boundary diagram is the
    failure this checks — not a missing id, a missing traced path."""
    model = _model()
    model["declared_flows"] = ["browser-share-request", "member-note-read"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("worker-share-redelivery" in reason for reason in result["reasons"])


def test_scanner_findings_are_additive_not_replacing(client) -> None:
    """Normal case: extra scanner findings are reported alongside the
    always-name set; they never substitute for it and are never dropped."""
    result = _gate(client, _model(), scanner_green=True, scanner_findings=["cve-extra"])
    assert result["gate"] == "pass"
    assert "cve-extra" in result["scanner_extra_findings"]


def test_top_priority_threat_without_real_mitigation_fails(client) -> None:
    """The highest-priority mandatory threat must resolve to a real
    mitigation, not a placeholder. Priority with nothing to prioritize
    toward is not prioritization."""
    model = _model()
    model["threats"][0]["mitigation"] = "TBD"
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("no real mitigation" in reason for reason in result["reasons"])


def test_missing_priority_field_fails(client) -> None:
    """Malformed/failure case: a threat with no priority at all cannot be
    ranked, so the gate must reject it rather than silently ignoring the
    field."""
    model = _model()
    del model["threats"][1]["priority"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("priority" in reason for reason in result["reasons"])


def test_fired_trigger_without_revisit_fails(client) -> None:
    """A named review trigger firing (a new share path shipped) demands a
    recorded re-review of the threat it names, not silence. This is the
    'notice a missing update, do not back-date' property."""
    model = _model()
    model["trigger_events"] = ["new-share-path"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any("not revisited" in reason for reason in result["reasons"])


def test_anti_fake_revisit_is_checked_per_threat_not_globally(client) -> None:
    """Anti-fake test. A fake fix might check only 'does *some* threat
    sharing this trigger name carry it in revisited_after', which passes
    as soon as any one row is updated. Add a second threat with the same
    trigger, revisit only the second one, and require the gate to still
    fail on the first — cross-tenant-read — because each row's own
    revisit state is independent."""
    model = _model()
    model["threats"].append(
        {
            "id": "share-grant-replay",
            "owner": "authz",
            "trigger": "new-share-path",
            "priority": 4,
            "mitigation": "single-use grant consumed at redelivery; replay denied",
            "revisited_after": ["new-share-path"],
        }
    )
    model["trigger_events"] = ["new-share-path"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any(
        "cross-tenant-read" in reason and "not revisited" in reason for reason in result["reasons"]
    )


def test_anti_fake_revisit_must_name_the_fired_trigger_not_merely_be_nonempty(client) -> None:
    """Anti-fake test, a second and distinct shape for the same claim. A
    fake fix might check only 'is revisited_after non-empty', which
    passes as soon as a threat carries any past revisit record at all —
    even one left over from a previous, unrelated trigger. Give
    cross-tenant-read a non-empty revisited_after that names a DIFFERENT,
    already-fired trigger ('new-client-surface'), fire 'new-share-path'
    (the trigger cross-tenant-read actually declares), and require the
    gate to still fail: a stale record of a past, different re-review is
    not evidence this trigger was ever revisited."""
    model = _model()
    model["threats"][0]["revisited_after"] = ["new-client-surface"]
    model["trigger_events"] = ["new-share-path"]
    result = _gate(client, model, scanner_green=True)
    assert result["gate"] == "fail"
    assert any(
        "cross-tenant-read" in reason and "not revisited" in reason for reason in result["reasons"]
    )
