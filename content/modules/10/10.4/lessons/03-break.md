# 10.4 — Deployment and configuration hardening (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
**Forbidden outcome:** Production process boots with debug enabled

**Authorized scope:** `labs/10.4/10.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable cfg.py boots anyway.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: boot_ok('prod', True) True.

## Vulnerable fixture (local)

```python
def boot_ok(env, debug):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Fail-open defaults. |
| Impact | Stack traces, interactive debugger, secret leak. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/10.4/10.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Feature flag that disables authz.

## Non-goals

No live-target instructions. Synthetic data only.
