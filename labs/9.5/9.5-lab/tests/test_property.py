def test_cannot_close_without_retest(impl):
    assert impl.close_finding({'retest': None}) is False
