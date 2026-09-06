def accept_token(claims: dict, expected_aud: str) -> bool:
    if not expected_aud:
        return False
    aud = claims.get("aud")
    if isinstance(aud, list):
        return expected_aud in aud
    return aud == expected_aud
