# 5.2 — Cryptographic properties and safe use (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
**Mechanism (not the property):** passlib/bcrypt is for passwords, not note bodies. Fernet still needs 5.3 key storage.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 5.2 |
|---|---|
| Root cause | Mechanism name “encrypted” applied to encoding. |
| Preconditions | protect returns b64(secret). |
| Impact (1.1 cell) | Confidentiality of the stored secret vs honest storage observers. — Any reader of the column gets the secret. |
| Prevention | Use a standard AEAD with a managed key; tests forbid b64 identity. |
| Detection | Scanner for b64-looking “ciphertext” of known plaintext in tests. |
| Recovery | Rotate keys; re-encrypt; treat as leak. |

## Framework defaults vs application guarantees

passlib/bcrypt is for passwords, not note bodies. Fernet still needs 5.3 key storage.

## Mechanism limits and bypasses

AES-GCM with a nonce reuse is not this property. Do not paste attack scripts — name the misuse.

Key in the same row; client-side only “encryption” with key in the bundle (8.1).

## Residual risk

Memory dumps; authorized operators.

## Practice

Table: property vs algorithm vs what it is *not* for.

Run `labs/5.2/5.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Password hashing vs field encryption vs backup encryption.

Clinic: SSN column labeled “encrypted” that is b64.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
