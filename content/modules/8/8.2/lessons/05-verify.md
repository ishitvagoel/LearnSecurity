# The broken files must fail when the secret is in plaintext

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

EncryptedSharedPreferences on a different file does not hide the note. Internal storage is a folder. After `save_note("secret")`, `plaintext_on_disk()` has to be false. On `--impl vulnerable` DISK still holds `'secret'`. On `--impl fixed` it does not. Do not image phones.

## Picture: broken files must fail: plaintext secret

A passing-test tally can still hide that the cache still holds `'secret'`.

```mermaid
flowchart LR
  V["--impl vulnerable"] --> F["Must fail plaintext secret"]
  X["--impl fixed"] --> P["Must pass not plaintext"]
```

If both pass, you are not looking at the body on disk.

## Observations, even for a cache

| Mode | Must show for this topic |
|---|---|
| Wrong input / abuse | save `'secret'` → not plaintext; broken files must fail |
| Normal | save `'other'` → not reported as plaintext secret (may pass on both) |
| Not claimed | Real AES; backup exclusion; screenshot `FLAG_SECURE`; Keystore hardware |

The checks are in `labs/8.2/8.2-lab/tests/test_property.py`. `test_cached_note_is_not_plaintext_on_disk` is there so a text-file cache of `'secret'` still fails.

```text
python3 -m pytest labs/8.2/8.2-lab/tests --impl vulnerable
python3 -m pytest labs/8.2/8.2-lab/tests --impl fixed
```

Saving a non-secret `'other'` value may pass on both sides. You still have to keep the cached note off plaintext disk. If the broken files do not fail `test_cached_note_is_not_plaintext_on_disk`, the practice is miswired — fix the wiring, not the check.

## What the checks do not prove

- Keystore hardware backing
- Auto-backup exclusion
- Screenshot / notification channels
- iOS Data Protection (later mirror)
- That the lab `aead:` prefix is AES-GCM (it is a stand-in)
- 4.1 logout wipe of the store

## Practice

Do not treat a grep for `EncryptedSharedPreferences` as the check. Call `save_note("secret")` then `plaintext_on_disk()`. A setup error is not proof the rule holds.

## Use it somewhere new

Asserting Room `insert` succeeded is not this check. Do not image a personal phone.

## What this page is not doing

Do not treat a live backup screenshot as proof. Do not log note bodies. Answer keys are not on this site. Do not claim the lab prefix is AES.
