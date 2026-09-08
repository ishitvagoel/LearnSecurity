from __future__ import annotations

import base64
import binascii
import os

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


_PREFIX = "aesgcm:v1:"
_NONCE_BYTES = 12
_AAD = b"learnsecurity-lab-5.2-note-body-v1"

# The key is deliberately generated in memory for this disposable fixture. It
# demonstrates the primitive and authentication tag without pretending to
# teach key storage or rotation; those concerns belong to Module 5.3.
_KEY = AESGCM.generate_key(bit_length=128)


def _cipher() -> AESGCM:
    if not _KEY:
        raise RuntimeError("encryption key is unavailable; refuse the write")
    return AESGCM(_KEY)


def protect(p: str) -> str:
    """Encrypt synthetic plaintext with AES-GCM and a fresh nonce."""
    if not isinstance(p, str):
        raise TypeError("plaintext must be text")
    nonce = os.urandom(_NONCE_BYTES)
    ciphertext_and_tag = _cipher().encrypt(nonce, p.encode("utf-8"), _AAD)
    payload = nonce + ciphertext_and_tag
    encoded = base64.urlsafe_b64encode(payload).decode("ascii")
    return _PREFIX + encoded


def unprotect(t: str) -> str:
    """Decrypt and authenticate a value produced by :func:`protect`."""
    if not isinstance(t, str) or not t.startswith(_PREFIX):
        raise ValueError("unsupported protected value")
    encoded = t[len(_PREFIX) :]
    try:
        payload = base64.b64decode(encoded.encode("ascii"), altchars=b"-_", validate=True)
    except (UnicodeEncodeError, binascii.Error, ValueError) as exc:
        raise ValueError("malformed protected value") from exc
    if len(payload) <= _NONCE_BYTES:
        raise ValueError("protected value is too short")
    nonce = payload[:_NONCE_BYTES]
    ciphertext_and_tag = payload[_NONCE_BYTES:]
    try:
        plaintext = _cipher().decrypt(nonce, ciphertext_and_tag, _AAD)
    except InvalidTag as exc:
        raise ValueError("protected value failed authentication") from exc
    try:
        return plaintext.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("protected value is not UTF-8") from exc


def looks_encrypted(t: str) -> bool:
    """Return true only for a value this fixture can authenticate and decrypt."""
    try:
        unprotect(t)
    except (TypeError, ValueError, RuntimeError):
        return False
    return True
