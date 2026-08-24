# E4 — Memory safety and native-code boundaries (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Python stand-in for a C helper |
| Objects | 4-byte buffer |
| Actions | copy_into |
| Channels | FFI |
| TCB | min(n, dst_len) copy. |
| Untrusted | n, src length |
| State / time | One copy. |
| 1.1 cell | Integrity of memory object bounds. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| caller | n=4 dst=4 | copy | allow |
| caller | n=8 dst=4 | copy | clamp-or-deny |
| ASAN | real C | ci | named-tool |
| lesson | PoC | weaponize | forbid |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E4/e4-lab` file `copy.py`.

## Transfer

Image parser; protobuf C.

## Residual risk

Existing C codecs for images (6.4).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
