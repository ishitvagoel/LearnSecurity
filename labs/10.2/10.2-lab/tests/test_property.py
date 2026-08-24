def test_hash_mismatch_refuses_install(impl):
    assert impl.install_ok('aaa', 'bbb') is False
