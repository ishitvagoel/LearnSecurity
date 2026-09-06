def test_cannot_close_without_recovery(impl):
    assert impl.close_incident({"recovery": "todo", "logs": "ok"}) is False


def test_cannot_close_when_logs_contain_note_body(impl):
    assert impl.close_incident({"recovery": "done", "logs": "note_body leaked"}) is False


def test_close_with_recovery_and_safe_logs_may_succeed(impl):
    assert impl.close_incident({"recovery": "done", "logs": "ok"}) is True
