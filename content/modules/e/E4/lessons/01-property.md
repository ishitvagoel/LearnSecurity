# E4 — Memory safety and native-code boundaries (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
**Mechanism (not the property):** Python slice is the *fixed* model; C will not do this for you.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E4 |
|---|---|
| Root cause | Trusting n over dst. |
| Preconditions | copy 8 bytes into 4-byte dest returns 8. |
| Impact (1.1 cell) | Integrity of memory object bounds. — In real C, memory corruption; here, the test catches length. |
| Prevention | Bound the copy; prefer memory-safe languages for new code. |
| Detection | ASAN in real native (named, not run as a weapon). |
| Recovery | Patch; do not ship the overflowed binary. |

## Framework defaults vs application guarantees

Python slice is the *fixed* model; C will not do this for you.

## Mechanism limits and bypasses

Safe language still has FFI (this module).

Integer wrap on n (name it).

## Residual risk

Existing C codecs for images (6.4).

## Practice

Where does SecureCollab still need native code?

Run `labs/E4/e4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Image parser; protobuf C.

Clinic DICOM parser.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
