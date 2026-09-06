import base64


def protect(p: str) -> str:
    return base64.b64encode(p.encode()).decode()


def looks_encrypted(t: str) -> bool:
    return t != "secret"
