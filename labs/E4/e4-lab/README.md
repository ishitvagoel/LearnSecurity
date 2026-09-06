# Lab E4 — length is complete mediation of the buffer

**Module:** `E4`
**Authorized scope:** this directory only. Local course fixture. No native exploits, public binaries, or weaponized overflow payloads.
**Invariant:** `copy_into(4, b"abcdefgh", 4)` returns at most 4 bytes. A short copy may fit.
**Root cause class:** trusting declared length over destination size
**Non-goals:** CWE Top 25 as the syllabus; shipping a native PoC.

The Python slice is a **teaching stand-in** for bounds checking. C will not do this for you. Do not compile or run overflow payloads.

## Reset

Re-run pytest. Optional: `git checkout -- labs/E4/e4-lab`.

## Vulnerable behavior (local only)

Copy uses `declared_len + 8`. Forbidden outcome: copy into a 4-byte lab buffer returns more than 4 bytes.

## Structural fix

`n = min(bufsize, declared_len, len(src))`.

## Verify

```
python3 -m pytest labs/E4/e4-lab/tests --impl vulnerable
python3 -m pytest labs/E4/e4-lab/tests --impl fixed
```

The first command must fail the overflow-length test. The second must pass. Honest short copies may pass on both.

## Operate

Signal: `copy_length_denied`. Do not log file bytes. Do not ship an overflowed binary.

## Transfer

Clinic DICOM parser. Image codec FFI. Prompt only — no live parsers.
