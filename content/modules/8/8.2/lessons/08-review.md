# 8.2 — Local data, keys, biometrics, offline, leakage (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
Review `labs/8.2/8.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/8.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): write body to cache.txt
- Seeded smell (label it yourself): Backup allowed for the app
- Seeded smell (label it yourself): No wipe on logout
- Seeded smell (label it yourself): Note in notification text

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Private app dir is encryption
- Fingerprint is MFA to the server
- Offline means no policy

## Practice

Write three review notes. Do not open the keys file.

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

## HITL / WCAG 2.2

Unlock-with-biometrics fallback must remain accessible (device credential) without dumping plaintext to a debug overlay.
