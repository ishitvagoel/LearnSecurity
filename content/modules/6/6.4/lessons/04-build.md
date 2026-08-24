# 6.4 — Files, paths, uploads, archives, XML, deserialization (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
resolve either raises or stays under /tmp/sc-lab.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
from pathlib import Path
ROOT=Path('/tmp/sc-lab').resolve()
def resolve(name):
    p = (ROOT / name).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise ValueError('escape')
    return str(p)
```

## Why this restores the cell

Join + canonicalize + prefix; random stored names; never execute uploads.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Starlette UploadFile.filename is hostile.

Allow-list of .png still fails if the processor parses XML (XXE) — name it.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

XML entity expansion; pickle; YAML load.

## Residual risk

Image codecs (memory) — E4.
