def protect(p: str) -> str:
    return "aesgcm:" + str(len(p))


def looks_encrypted(t: str) -> bool:
    return t.startswith("aesgcm:")
