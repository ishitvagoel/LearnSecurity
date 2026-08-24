# E4 — Memory safety and native-code boundaries (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.

## Property (start here)

A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.

## Attacker capabilities and trust assumptions

- **Attacker:** Hostile filename/size field; FFI caller.
- **Trust:** Local copy_into(dst_len, src, n).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Image parser; protobuf C.

**Product sketch:** Clinic DICOM parser.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Python slice is the *fixed* model; C will not do this for you.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/E4/e4-lab` stays the only running system you may break.
