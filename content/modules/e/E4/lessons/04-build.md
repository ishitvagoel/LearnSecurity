# E4 — Memory safety and native-code boundaries (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
len(out) <= 4.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def copy_into(bufsize, src, declared_len):
    n = min(bufsize, declared_len, len(src))
    return src[:n]
```

## Why this restores the cell

Bound the copy; prefer memory-safe languages for new code.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Python slice is the *fixed* model; C will not do this for you.

Safe language still has FFI (this module).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Image parser; protobuf C.

## Residual risk

Existing C codecs for images (6.4).
