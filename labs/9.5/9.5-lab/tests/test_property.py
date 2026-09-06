def test_cannot_close_without_retest(impl):
    assert impl.close_finding({"retest": None}) is False


def test_passing_retest_may_close(impl):
    assert impl.close_finding({"retest": "pass"}) is True
