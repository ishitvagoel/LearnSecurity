# 5.2 — Cryptographic properties and safe use (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.

## Property (start here)

protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator who can read the stored field; stolen disk of the lab dict.
- **Trust:** Local protect()/looks_encrypted(). Real AEAD keys are 5.3.
**Forbidden outcome:** Stored secret is mere encoding of plaintext

**Authorized scope:** `labs/5.2/5.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable crypto.py encodes rather than encrypts.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: protect returns b64(secret).

## Vulnerable fixture (local)

```python
import base64
def protect(p):
    return base64.b64encode(p.encode()).decode()
def looks_encrypted(t):
    return t != 'secret'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Mechanism name “encrypted” applied to encoding. |
| Impact | Any reader of the column gets the secret. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/5.2/5.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Password hashing vs field encryption vs backup encryption.

## Non-goals

No live-target instructions. Synthetic data only.
