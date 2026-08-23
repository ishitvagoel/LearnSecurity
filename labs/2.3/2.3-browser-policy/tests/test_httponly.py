HTTPONLY_SESSION = {"sc_session": {"value": "synthetic-session", "httponly": True, "secure": True}}


def test_script_cannot_read_httponly_session(cookies) -> None:
    got = cookies.js_read_session(HTTPONLY_SESSION)
    assert got is None, "HttpOnly is a browser cell; it is not CSP and not Trusted Types"
