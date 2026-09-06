def test_hash_mismatch_refuses_install(impl):
    assert impl.install_ok("aaa", "bbb") is False


def test_matching_digest_may_install(impl):
    assert impl.install_ok("aaa", "aaa") is True
