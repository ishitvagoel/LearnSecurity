def test_prod_debug_must_not_boot(impl):
    assert impl.boot_ok("prod", True) is False


def test_prod_without_debug_may_boot(impl):
    assert impl.boot_ok("prod", False) is True
