# E4 — Memory safety and native-code boundaries (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | ASAN in real native (named, not run as a weapon). |
| Signal (no bodies) | overlong_copy_denied. |
| Revoke / recover | Patch; do not ship the overflowed binary. |
| Residual | Existing C codecs for images (6.4). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E4/e4-lab`.

## Transfer

Image parser; protobuf C.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
