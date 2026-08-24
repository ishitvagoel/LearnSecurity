def test_prod_debug_must_not_boot(impl):
    assert impl.boot_ok('prod', True) is False
