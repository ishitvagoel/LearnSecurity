# 8.2 — Local data, keys, biometrics, offline, leakage (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
plaintext_on_disk False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
DISK={}
def reset():
    DISK.clear()
def save_note(body):
    DISK['note']='aead:'+str(len(body))
def plaintext_on_disk():
    return DISK.get('note')=='secret'
```

## Why this restores the cell

Encrypt cache; expire; wipe on logout/revoke; no body in notifications.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

EncryptedSharedPreferences defaults are not automatic for every file you write.

Biometrics gate UI, not key extraction on a compromised OS.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

## Residual risk

Physical + extracted keys — honest.
