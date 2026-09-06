def test_fourth_export_is_denied(impl):
    assert impl.allow(4) is False


def test_third_export_is_allowed(impl):
    assert impl.allow(3) is True


def test_first_export_is_allowed(impl):
    assert impl.allow(1) is True
