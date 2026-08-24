# 8.1 — Hostile-client and mobile platform model (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | client_claim_ignored; attest_fail. |
| Signal (no bodies) | attest_fail_export_denied. |
| Revoke / recover | Revoke app tokens. |
| Residual | Honest users on rooted devices — product policy. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/8.1/8.1-lab`.

## Transfer

Feature flags in the APK; premium=true.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
