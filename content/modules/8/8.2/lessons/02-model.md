# 8.2 — Local data, keys, biometrics, offline, leakage (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | thief, backup service, app |
| Objects | cache file |
| Actions | save_note, plaintext_on_disk |
| Channels | disk, backup, notifications (8.5 related) |
| TCB | Keystore-backed encryption; server remains source of truth. |
| Untrusted | App private dir on a rooted device as “enough” |
| State / time | Offline cache after revoke (4.1). |
| 1.1 cell | Confidentiality of bodies at rest on a hostile device. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| thief | cache file | read | deny-plaintext |
| user | offline read | own notes | allow-until-revoke |
| backup | app data | cloud | no-bodies-or-encrypted |
| server | revoke | cache | wipe |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/8.2/8.2-lab` file `disk.py`.

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

## Residual risk

Physical + extracted keys — honest.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
