def accept_token(claims: dict, expected_aud: str) -> bool:
    return "sub" in claims
