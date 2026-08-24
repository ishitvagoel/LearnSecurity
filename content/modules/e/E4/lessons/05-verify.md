# E4 — Memory safety and native-code boundaries (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Copy returns more bytes than the destination length |
| Failure | Fail closed: Bound the copy; prefer memory-safe languages for new code |

Lab tests: `test_property.py` under `labs/E4/e4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Copy returns more bytes than the destination length`
- `--impl fixed`: **pass**

copy does not exceed buffer.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Image parser; protobuf C.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
