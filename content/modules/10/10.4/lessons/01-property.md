# 10.4 — Deployment and configuration hardening (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
**Mechanism (not the property):** Next.js NODE_ENV=development in prod compose files.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 10.4 |
|---|---|
| Root cause | Fail-open defaults. |
| Preconditions | boot_ok('prod', True) True. |
| Impact (1.1 cell) | Least privilege of the running config + confidentiality of traces. — Stack traces, interactive debugger, secret leak. |
| Prevention | Refuse boot; config review; no debug routes registered. |
| Detection | prod_debug_boot denied metric; drift. |
| Recovery | Kill; rotate secrets that appeared in traces. |

## Framework defaults vs application guarantees

Next.js NODE_ENV=development in prod compose files.

## Mechanism limits and bypasses

debug=False still has other flags (feature, migration).

Sidecar debug container.

## Residual risk

Emergency debug with E6 timebox.

## Practice

Production-readiness list: flags, admin, migrations, rollback.

Run `labs/10.4/10.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Feature flag that disables authz.

Clinic: Django DEBUG=True.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
