def test_report_only_is_not_enforcement(impl):
    h = {'Content-Security-Policy-Report-Only': "default-src 'none'"}
    assert impl.isolation_enforced(h) is False
