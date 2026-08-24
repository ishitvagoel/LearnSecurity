# 8.2 — Local data, keys, biometrics, offline, leakage (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** iOS Keychain vs Android Keystore; desktop Electron.

**Product sketch:** Clinic offline chart cache.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | EncryptedSharedPreferences defaults are not automatic for every file you write.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/8.2/8.2-lab` stays the only running system you may break.
