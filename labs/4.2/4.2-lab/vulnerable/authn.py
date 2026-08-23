def phishing_resistant(method: str, origin: str, expected: str) -> bool:
    return method in {"password", "otp", "webauthn"}
