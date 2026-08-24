def test_fourth_export_is_denied(impl):
    assert impl.allow(4) is False
