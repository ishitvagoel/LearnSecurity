# Lab 5.2 — encoding is not encryption

**Module:** `5.2`
**Authorized scope:** this directory only. Local course fixture. No live KMS.
**Invariant:** `protect("secret")` must provide authenticated confidentiality for the stored value; it must not be reversible as Base64 of the plaintext, and tampering must be rejected. Encoding is not confidentiality.
**Root cause class:** mechanism-name confusion (encoding labeled encryption)
**Non-goals:** rolling a cipher, live ciphertext attacks, real note bodies.

The fixed fixture uses the vetted `cryptography` library's AES-GCM implementation with a fresh nonce, authenticated associated data, and a disposable in-memory key. It is a primitive-level teaching fixture, not a production key-management design.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/5.2/5.2-lab`, then run `git restore --source=HEAD -- labs/5.2/5.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`protect` returns Base64 of the plaintext. Forbidden outcome: `protect()` is reversible as Base64 to `secret`.

## Structural fix

Refuse encoding as the confidentiality mechanism. The fixed helper performs AES-GCM encryption, creates a fresh 96-bit nonce for every call, authenticates the ciphertext, rejects tampering, and refuses malformed or unauthenticated values. Key storage, rotation, recovery, and deployment separation remain Module 5.3 concerns.

## Verify

From the repository root, install the pinned local test dependencies in a
disposable virtual environment:

    python3 -m pip install -r labs/5.2/5.2-lab/requirements.txt

Then run:

```
python3 -m pytest labs/5.2/5.2-lab/tests --impl vulnerable
python3 -m pytest labs/5.2/5.2-lab/tests --impl fixed
```

The first command must fail on the encoding test. The second must pass.

The fixed suite also checks that the value decrypts, repeated plaintext receives different nonces, tampering raises an authentication error, and malformed values are not treated as encrypted.

## Operate

CI checks: known-plaintext must not round-trip as Base64, valid ciphertext must authenticate, and tampering must fail closed. Treat a Base64 hit as a leak; contain the affected path, re-protect the data, and perform the key-management response from 5.3.

## Transfer

Clinic SSN column labeled encrypted that is Base64. The transfer must distinguish the AEAD primitive from key lifecycle, access policy, backups, and operator access. Prompt only.
