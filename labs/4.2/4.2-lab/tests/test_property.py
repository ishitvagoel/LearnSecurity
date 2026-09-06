REAL = "https://app.securecollab.test"
EVIL = "https://evil.example"


def test_password_is_not_phishing_resistant(impl) -> None:
    assert impl.phishing_resistant("password", EVIL, REAL) is False


def test_otp_is_not_phishing_resistant(impl) -> None:
    assert impl.phishing_resistant("otp", EVIL, REAL) is False


def test_webauthn_wrong_origin_fails(impl) -> None:
    assert impl.phishing_resistant("webauthn", EVIL, REAL) is False


def test_webauthn_matching_origin_is_resistant(impl) -> None:
    assert impl.phishing_resistant("webauthn", REAL, REAL) is True
