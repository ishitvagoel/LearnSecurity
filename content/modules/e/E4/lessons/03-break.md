# E4 — Memory safety and native-code boundaries (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
**Forbidden outcome:** Copy returns more bytes than the destination length

**Authorized scope:** `labs/E4/e4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable copy.py returns too many bytes.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: copy 8 bytes into 4-byte dest returns 8.

## Vulnerable fixture (local)

```python
def copy_into(bufsize, src, declared_len):
    return src[: declared_len + 8]
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Trusting n over dst. |
| Impact | In real C, memory corruption; here, the test catches length. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E4/e4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Image parser; protobuf C.

## Non-goals

No live-target instructions. Synthetic data only.
