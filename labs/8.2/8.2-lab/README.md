# Lab 8.2 — private app dir is not encryption

**Module:** `8.2`
**Authorized scope:** this directory only. Local course fixture. No personal-phone imaging.
**Invariant:** after `save_note("secret")`, `plaintext_on_disk()` is false.
**Root cause class:** bodies written as text files
**Non-goals:** live backups, claiming the `aead:` prefix is AES-GCM.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/8.2/8.2-lab`, then run `git restore --source=HEAD -- labs/8.2/8.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`save_note` stores the body as-is. Forbidden outcome: plaintext cache.

## Structural fix

Store a ciphertext **stand-in** (`aead:` + length), not the body. Production would use Keystore-wrapped AEAD (5.2).

## Verify

```
python3 -m pytest labs/8.2/8.2-lab/tests --impl vulnerable
python3 -m pytest labs/8.2/8.2-lab/tests --impl fixed
```

The first command must fail on plaintext `'secret'`. The second must pass. Honest `'other'` saves may pass on both.

## Operate

Signal: `logout_wipes_cache`. Do not log bodies.

## Transfer

Clinic offline chart cache. Prompt only.
