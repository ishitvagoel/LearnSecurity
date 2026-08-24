# 8.2 — Local data, keys, biometrics, offline, leakage (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Device lost flow; remote wipe where the OS allows. |
| Signal (no bodies) | logout_wipes_cache; backup_flag. |
| Revoke / recover | Revoke sessions; rotate. |
| Residual | Physical + extracted keys — honest. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/8.2/8.2-lab`.

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

## Usability

Unlock-with-biometrics fallback must remain accessible (device credential) without dumping plaintext to a debug overlay.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
