def test_green_scanner_is_not_an_empty_threat_model(impl) -> None:
    threats = impl.threats_from_scan(True)
    assert "cross-tenant-read" in threats


def test_mandatory_threats_have_owners_and_triggers(impl) -> None:
    model = impl.assemble_threat_model(True)
    by_id = {row["id"]: row for row in model["threats"]}
    for threat_id in ("cross-tenant-read", "hostile-browser", "stolen-worker"):
        row = by_id[threat_id]
        assert row.get("owner")
        assert row.get("trigger")


def test_scanner_findings_are_additive(impl) -> None:
    threats = impl.threats_from_scan(True, ["cve-extra"])
    assert "cross-tenant-read" in threats
    assert "cve-extra" in threats
