def test_note_body_is_not_logged(impl) -> None:
    line = impl.log_event("note_read", "tenant-A-secret-body")
    assert "tenant-A-secret-body" not in line
    assert "redacted" in line.lower() or "confidential" in line.lower()
