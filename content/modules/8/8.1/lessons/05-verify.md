# 8.1 — Hostile-client and mobile platform model (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Client integrity claim authorizes export |
| Failure | Fail closed: Ignore client integrity for authorization; server attest/session 1 |

Lab tests: `test_property.py` under `labs/8.1/8.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Client integrity claim authorizes export`
- `--impl fixed`: **pass**

client integrity is not authorization.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Feature flags in the APK; premium=true.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
