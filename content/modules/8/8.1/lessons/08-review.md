# 8.1 — Hostile-client and mobile platform model (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
Review `labs/8.1/8.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/8.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): if body.integrity==ok: export
- Seeded smell (label it yourself): No server attest test
- Seeded smell (label it yourself): Secrets in the APK (8.4)
- Seeded smell (label it yourself): MASVS as a sticker

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Obfuscation is authorization
- If we use Kotlin we are safe
- Store listing = device trust

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Feature flags in the APK; premium=true.
