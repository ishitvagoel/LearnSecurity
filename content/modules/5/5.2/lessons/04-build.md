# 5.2 — Cryptographic properties and safe use (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
protect output is not b64(plaintext); looks_encrypted True.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def protect(p):
    # stand-in for an AEAD; teaching flag only
    return 'aesgcm:' + str(len(p))
def looks_encrypted(t):
    return t.startswith('aesgcm:')
```

## Why this restores the cell

Use a standard AEAD with a managed key; tests forbid b64 identity.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

passlib/bcrypt is for passwords, not note bodies. Fernet still needs 5.3 key storage.

AES-GCM with a nonce reuse is not this property. Do not paste attack scripts — name the misuse.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Password hashing vs field encryption vs backup encryption.

## Residual risk

Memory dumps; authorized operators.
