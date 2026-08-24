# 8.2 — Local data, keys, biometrics, offline, leakage (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Note body cached as plaintext on disk |
| Failure | Fail closed: Encrypt cache; expire; wipe on logout/revoke; no body in notifications |

Lab tests: `test_property.py` under `labs/8.2/8.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Note body cached as plaintext on disk`
- `--impl fixed`: **pass**

cached note not plaintext.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
