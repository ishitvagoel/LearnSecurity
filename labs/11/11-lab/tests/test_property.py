def test_revoked_share_cannot_read(impl):
    impl.revoke("n1", "B")
    assert impl.read("n1", "B") is None


def test_owner_may_still_read_after_revoke(impl):
    impl.revoke("n1", "B")
    assert impl.read("n1", "A") == "secret"


def test_share_may_read_before_revoke(impl):
    assert impl.read("n1", "B") == "secret"
