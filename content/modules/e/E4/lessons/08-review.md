# E4 — Memory safety and native-code boundaries (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
Review `labs/E4/e4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): copy returns full src
- Seeded smell (label it yourself): No dest length check
- Seeded smell (label it yourself): unsafe FFI in Kotlin
- Seeded smell (label it yourself): “Python so we are memory safe” with a C wheel

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Memory safety is only C
- Fuzzing without ASAN is enough
- This lab is an exploit tutorial

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Image parser; protobuf C.
