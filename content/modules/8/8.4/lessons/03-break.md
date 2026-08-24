# 8.4 — Build, distribution, attestation, resilience (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
**Forbidden outcome:** Debug build allowed to call production export

**Authorized scope:** `labs/8.4/8.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable build.py allows debug to prod.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: api_allowed('debug','ok') True.

## Vulnerable fixture (local)

```python
def api_allowed(build_type, attest):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Prod API trusts a client claim of attest=ok from any build. |
| Impact | Debug keys, loggers, extra exports against prod data. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/8.4/8.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

SBOM of the APK (10.2).

## Non-goals

No live-target instructions. Synthetic data only.
