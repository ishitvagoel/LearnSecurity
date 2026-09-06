def test_debug_build_cannot_call_prod_export(impl):
    assert impl.api_allowed("debug", "ok") is False


def test_release_with_attest_may_call_prod(impl):
    assert impl.api_allowed("release", "ok") is True


def test_release_without_attest_is_denied(impl):
    assert impl.api_allowed("release", "fail") is False
