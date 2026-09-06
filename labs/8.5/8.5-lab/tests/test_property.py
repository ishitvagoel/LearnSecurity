def test_crash_report_omits_note_body(impl):
    rep = impl.crash_report("secret")
    assert "secret" not in str(rep)


def test_honest_crash_still_includes_stack(impl):
    rep = impl.crash_report("ok-note")
    assert "stack" in rep
    assert rep["stack"]
