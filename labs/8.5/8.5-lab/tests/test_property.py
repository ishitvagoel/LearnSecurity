def test_crash_report_omits_note_body(impl):
    rep = impl.crash_report('secret')
    assert 'secret' not in str(rep)
