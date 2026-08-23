def test_app_role_cannot_read_other_tenant(impl) -> None:
    assert impl.can_select("app", "tB", "tA") is False
