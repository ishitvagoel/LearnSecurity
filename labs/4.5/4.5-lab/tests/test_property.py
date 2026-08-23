def test_wrong_audience_is_rejected(impl) -> None:
    assert impl.accept_token({"sub": "alice", "aud": "other-api"}, "securecollab-api") is False

def test_expected_audience_is_accepted(impl) -> None:
    assert impl.accept_token({"sub": "alice", "aud": "securecollab-api"}, "securecollab-api") is True
