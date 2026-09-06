def test_active_session_is_valid(impl) -> None:
    assert impl.session_valid("alice") is True


def test_deleted_user_session_is_dead(impl) -> None:
    impl.delete_user("alice")
    assert impl.session_valid("alice") is False


def test_deleted_denies_even_if_session_map_still_has_row(impl) -> None:
    impl.delete_user("alice")
    impl.SESSIONS["alice"] = True
    assert impl.session_valid("alice") is False
