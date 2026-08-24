# 5.2 — Cryptographic properties and safe use (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app, disk observer |
| Objects | plaintext, stored blob |
| Actions | protect |
| Channels | file/db column |
| TCB | A real AEAD or KDF appropriate to the threat — lab may stub as non-b64. |
| Untrusted | Base64, rot13, homegrown XOR with a constant |
| State / time | Stolen backup years later (crypto agility 5.3). |
| 1.1 cell | Confidentiality of the stored secret vs honest storage observers. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| disk observer | b64 field | read | must-not-be-plaintext |
| app | AEAD | decrypt-with-key | allow |
| app | password KDF | note body | wrong-tool |
| backup | blob | steal | 5.3 key residual |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/5.2/5.2-lab` file `crypto.py`.

## Transfer

Password hashing vs field encryption vs backup encryption.

## Residual risk

Memory dumps; authorized operators.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
