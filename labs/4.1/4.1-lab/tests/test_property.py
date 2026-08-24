def test_deleted_user_session_is_dead(impl) -> None:
    impl.delete_user("alice")
    assert impl.session_valid("alice") is False
