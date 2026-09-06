# Lab 5.2 — encoding is not encryption

**Module:** `5.2`
**Authorized scope:** this directory only. Local course fixture. No live KMS.
**Invariant:** `protect("secret")` must not be reversible as Base64 of the plaintext. Encoding is not confidentiality.
**Root cause class:** mechanism-name confusion (encoding labeled encryption)
**Non-goals:** rolling a cipher, live ciphertext attacks, real note bodies.

The fixed `aesgcm:` prefix is a **teaching flag**, not an AES-GCM implementation.

## Reset

Re-run pytest. Optional: `git checkout -- labs/5.2/5.2-lab`.

## Vulnerable behavior (local only)

`protect` returns Base64 of the plaintext. Forbidden outcome: `protect()` is reversible as Base64 to `secret`.

## Structural fix

Refuse encoding as the confidentiality mechanism. The lab stand-in marks AEAD-shaped output; real keys wait for 5.3.

## Verify

```
python3 -m pytest labs/5.2/5.2-lab/tests --impl vulnerable
python3 -m pytest labs/5.2/5.2-lab/tests --impl fixed
```

The first command must fail on the encoding test. The second must pass.

## Operate

CI check: known-plaintext must not round-trip as Base64. Treat a hit as a leak; rotate keys (5.3).

## Transfer

Clinic SSN column labeled encrypted that is Base64. Prompt only.
