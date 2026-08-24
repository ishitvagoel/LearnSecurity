def test_deleted_account_leaves_no_analytics_body(impl):
    impl.delete_account('alice')
    assert impl.body_retained('alice') is None
