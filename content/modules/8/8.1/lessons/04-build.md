# 8.1 — Hostile-client and mobile platform model (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
client ok + server fail => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def allow_export(client_claims, server_attest):
    return server_attest == 'play_integrity_pass'
```

## Why this restores the cell

Ignore client integrity for authorization; server attest/session 1.2.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Play Integrity is a signal, not 1.2.

Attestation raises cost, does not establish trust of the client binary.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Feature flags in the APK; premium=true.

## Residual risk

Honest users on rooted devices — product policy.
