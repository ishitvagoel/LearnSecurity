def test_green_scanner_is_not_an_empty_threat_model(impl) -> None:
    threats = impl.threats_from_scan(True)
    assert "cross-tenant-read" in threats
