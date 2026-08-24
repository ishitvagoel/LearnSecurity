# 8.1 — Hostile-client and mobile platform model (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | hostile APK, server |
| Objects | export, integrity claim |
| Actions | allow_export |
| Channels | JSON body |
| TCB | Server-side attestation/token — lab uses server_attest string. |
| Untrusted | Any client field, local ifs. |
| State / time | Runtime after Play integrity check cached on device. |
| 1.1 cell | Authorization — server decides. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| APK | integrity field | authorize | deny |
| server | attest fail | export | deny |
| server | attest+user 1.2 | export | allow |
| rooted honest | export | policy | residual |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/8.1/8.1-lab` file `client.py`.

## Transfer

Feature flags in the APK; premium=true.

## Residual risk

Honest users on rooted devices — product policy.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
