def accept_token(claims: dict, expected_aud: str) -> bool:
    aud = claims.get("aud")
    if isinstance(aud, list):
        return expected_aud in aud
    return aud == expected_aud
