# 10.4 — Deployment and configuration hardening (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.

## Property (start here)

A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who finds /debug; error pages with traces.
- **Trust:** Local boot_ok('prod', True).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | prod_debug_boot denied metric; drift. |
| Signal (no bodies) | prod_debug_forbidden. |
| Revoke / recover | Kill; rotate secrets that appeared in traces. |
| Residual | Emergency debug with E6 timebox. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/10.4/10.4-lab`.

## Transfer

Feature flag that disables authz.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
