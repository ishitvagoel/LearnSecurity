# 8.2 — Local data, keys, biometrics, offline, leakage (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
**Mechanism (not the property):** EncryptedSharedPreferences defaults are not automatic for every file you write.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 8.2 |
|---|---|
| Root cause | Bodies written as text files. |
| Preconditions | plaintext_on_disk True after save. |
| Impact (1.1 cell) | Confidentiality of bodies at rest on a hostile device. — Stolen device yields notes. |
| Prevention | Encrypt cache; expire; wipe on logout/revoke; no body in notifications. |
| Detection | Device lost flow; remote wipe where the OS allows. |
| Recovery | Revoke sessions; rotate. |

## Framework defaults vs application guarantees

EncryptedSharedPreferences defaults are not automatic for every file you write.

## Mechanism limits and bypasses

Biometrics gate UI, not key extraction on a compromised OS.

Screenshots, logs, clipboard, auto backup.

## Residual risk

Physical + extracted keys — honest.

## Practice

Inventory every local store.

Run `labs/8.2/8.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

Clinic offline chart cache.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Unlock-with-biometrics fallback must remain accessible (device credential) without dumping plaintext to a debug overlay.
