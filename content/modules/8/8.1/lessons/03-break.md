# 8.1 — Hostile-client and mobile platform model (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.

## Property (start here)

A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).

## Attacker capabilities and trust assumptions

- **Attacker:** Modified APK; Frida; stolen “integrity ok” boolean.
- **Trust:** Local allow_export(client_claim, server_attest).
**Forbidden outcome:** Client integrity claim authorizes export

**Authorized scope:** `labs/8.1/8.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable client.py trusts JSON integrity.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: allow_export({integrity:ok}, 'fail') True.

## Vulnerable fixture (local)

```python
def allow_export(client_claims, server_attest):
    return client_claims.get('integrity') == 'ok'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Policy evaluated on the attacker’s CPU. |
| Impact | Export without server authority. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/8.1/8.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Feature flags in the APK; premium=true.

## Non-goals

No live-target instructions. Synthetic data only.
