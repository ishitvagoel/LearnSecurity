def test_http_200_only_is_not_a_security_test(impl):
    assert impl.is_security_test({'status_asserted': True}) is False
