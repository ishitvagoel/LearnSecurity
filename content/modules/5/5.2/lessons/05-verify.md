# 5.2 — Cryptographic properties and safe use (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Stored secret is mere encoding of plaintext |
| Failure | Fail closed: Use a standard AEAD with a managed key; tests forbid b64 identity |

Lab tests: `test_property.py` under `labs/5.2/5.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Stored secret is mere encoding of plaintext`
- `--impl fixed`: **pass**

decode(protect(secret)) != secret.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Password hashing vs field encryption vs backup encryption.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
