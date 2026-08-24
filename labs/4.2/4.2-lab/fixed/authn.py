def phishing_resistant(method: str, origin: str, expected: str) -> bool:
    if method != "webauthn":
        return False
    return origin == expected
