def test_active_account_analytics_present(impl) -> None:
    assert impl.body_retained("alice") == "secret"


def test_deleted_account_leaves_no_analytics_body(impl) -> None:
    impl.delete_account("alice")
    assert impl.body_retained("alice") is None


def test_deleted_account_leaves_no_search_copy(impl) -> None:
    impl.delete_account("alice")
    assert impl.search_retained("alice") is None
