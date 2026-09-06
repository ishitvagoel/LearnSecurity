def test_query_string_token_is_rejected(impl) -> None:
    got = impl.session_from_request({"access_token": "secret"}, {}, None)
    assert got is None


def test_cookie_session_still_works(impl) -> None:
    got = impl.session_from_request({}, {"sc_session": "cookie-tok"}, None)
    assert got == "cookie-tok"


def test_authorization_header_still_works(impl) -> None:
    got = impl.session_from_request({}, {}, "header-tok")
    assert got == "header-tok"
