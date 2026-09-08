import base64

import pytest


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


def test_protected_value_round_trips_through_authenticated_decryption(impl) -> None:
    out = impl.protect("secret")
    assert impl.unprotect(out) == "secret"


def test_protect_uses_a_fresh_nonce_for_repeated_plaintext(impl) -> None:
    first = impl.protect("secret")
    second = impl.protect("secret")
    assert first != second
    assert impl.unprotect(first) == "secret"
    assert impl.unprotect(second) == "secret"


def test_tampering_is_rejected(impl) -> None:
    out = impl.protect("secret")
    raw = base64.b64decode(out.split(":", 2)[-1].encode(), altchars=b"-_", validate=True)
    tampered = raw[:-1] + bytes([raw[-1] ^ 1])
    token = "aesgcm:v1:" + base64.urlsafe_b64encode(tampered).decode("ascii")
    with pytest.raises(ValueError, match="authentication"):
        impl.unprotect(token)


def test_malformed_value_is_not_reported_as_encrypted(impl) -> None:
    assert not impl.looks_encrypted("aesgcm:v1:not-a-valid-ciphertext")
