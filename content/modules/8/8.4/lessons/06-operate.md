# 8.4 — Build, distribution, attestation, resilience (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | debug_client_to_prod. |
| Signal (no bodies) | debug_to_prod_denied. |
| Revoke / recover | Revoke debug client id; rotate. |
| Residual | Attestation farms. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/8.4/8.4-lab`.

## Transfer

SBOM of the APK (10.2).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
