def test_protect_is_not_mere_encoding(impl):
    out = impl.protect('secret')
    import base64
    try:
        raw = base64.b64decode(out.encode(), validate=True).decode()
    except Exception:
        raw = None
    assert raw != 'secret'
    assert impl.looks_encrypted(out)
