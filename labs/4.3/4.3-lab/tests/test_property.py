def test_query_string_token_is_rejected(impl) -> None:
    got = impl.session_from_request({"access_token": "secret"}, {}, None)
    assert got is None
