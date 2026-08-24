# 8.2 — Local data, keys, biometrics, offline, leakage (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.

## Property (start here)

A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.

## Attacker capabilities and trust assumptions

- **Attacker:** USB backup; lost unlocked-cache device; cloud backup of app files.
- **Trust:** Local save_note / plaintext_on_disk.
**Forbidden outcome:** Note body cached as plaintext on disk

**Authorized scope:** `labs/8.2/8.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable disk.py stores plaintext.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: plaintext_on_disk True after save.

## Vulnerable fixture (local)

```python
DISK={}
def reset():
    DISK.clear()
def save_note(body):
    DISK['note']=body
def plaintext_on_disk():
    return DISK.get('note')=='secret'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Bodies written as text files. |
| Impact | Stolen device yields notes. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/8.2/8.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

iOS Keychain vs Android Keystore; desktop Electron.

## Non-goals

No live-target instructions. Synthetic data only.
