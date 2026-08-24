def test_grant_on_n1_is_not_grant_on_n2(impl) -> None:
    assert impl.can_read("bob", "n2") is False
