# 5.2 — Cryptographic properties and safe use (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
Review `labs/5.2/5.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/5.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): protect = base64
- Seeded smell (label it yourself): AES-ECB “because we need it deterministic”
- Seeded smell (label it yourself): JWT as encryption
- Seeded smell (label it yourself): No looks_encrypted test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HTTPS means data at rest is encrypted
- Base64 is hashing
- Stronger algorithm fixes a bad key story

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Password hashing vs field encryption vs backup encryption.
