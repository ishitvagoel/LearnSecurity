# 6.4 — Files, paths, uploads, archives, XML, deserialization (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
**Forbidden outcome:** Resolved path escapes the lab root

**Authorized scope:** `labs/6.4/6.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable path.py concatenates.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: resolve('../etc/passwd') escapes root.

## Vulnerable fixture (local)

```python
from pathlib import Path
ROOT=Path('/tmp/sc-lab')
def resolve(name):
    return str(ROOT / name)
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Path grammar mixed with data; no canonicalization. |
| Impact | Read/write outside the note store. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/6.4/6.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

XML entity expansion; pickle; YAML load.

## Non-goals

No live-target instructions. Synthetic data only.
