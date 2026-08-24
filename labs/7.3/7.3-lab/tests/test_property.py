def test_missing_signature_is_rejected(impl):
    assert impl.accept('', 'body', 'lab-secret') is False
