def test_client_integrity_claim_is_not_authorization(impl):
    assert impl.allow_export({"integrity": "ok"}, "fail") is False


def test_server_attest_may_allow_export(impl):
    assert impl.allow_export({"integrity": "ok"}, "play_integrity_pass") is True


def test_missing_client_claim_does_not_authorize(impl):
    assert impl.allow_export({}, "fail") is False
