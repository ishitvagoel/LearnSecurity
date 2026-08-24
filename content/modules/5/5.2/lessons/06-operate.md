# 5.2 — Cryptographic properties and safe use (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Scanner for b64-looking “ciphertext” of known plaintext in tests. |
| Signal (no bodies) | known-plaintext-b64 test in CI. |
| Revoke / recover | Rotate keys; re-encrypt; treat as leak. |
| Residual | Memory dumps; authorized operators. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/5.2/5.2-lab`.

## Transfer

Password hashing vs field encryption vs backup encryption.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
