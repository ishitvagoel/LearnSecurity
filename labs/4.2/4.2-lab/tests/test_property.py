def test_password_is_not_phishing_resistant(impl) -> None:
    assert impl.phishing_resistant("password", "https://evil.example", "https://app.securecollab.test") is False

def test_webauthn_wrong_origin_fails(impl) -> None:
    assert impl.phishing_resistant("webauthn", "https://evil.example", "https://app.securecollab.test") is False
