def test_revoked_share_cannot_read(impl):
    impl.revoke('n1', 'B')
    assert impl.read('n1', 'B') is None
