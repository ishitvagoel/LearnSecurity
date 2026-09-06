import base64


def test_protect_does_not_return_plaintext(impl) -> None:
    assert impl.protect("secret") != "secret"


def test_protect_is_not_mere_encoding(impl) -> None:
    out = impl.protect("secret")
    try:
        raw = base64.b64decode(out.encode(), validate=True).decode()
    except Exception:
        raw = None
    assert raw != "secret"
    assert impl.looks_encrypted(out)
