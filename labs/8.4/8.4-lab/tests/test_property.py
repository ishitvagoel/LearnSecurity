def test_debug_build_cannot_call_prod_export(impl):
    assert impl.api_allowed('debug', 'ok') is False
