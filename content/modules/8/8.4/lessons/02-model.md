# 8.4 — Build, distribution, attestation, resilience (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | debug build, prod API |
| Objects | export endpoint |
| Actions | api_allowed |
| Channels | TLS to prod |
| TCB | Server rejects debug client ids / non-prod signatures. |
| Untrusted | Client attest string, obfuscation |
| State / time | CI artifact mis-tagged. |
| 1.1 cell | Integrity of the release channel. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| debug APK | prod export | call | deny |
| release APK | prod export | call | allow-if-1.2-attest |
| stolen sign key | store | publish | 5.3 incident |
| R8 | strings | hide | not-authz |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/8.4/8.4-lab` file `build.py`.

## Transfer

SBOM of the APK (10.2).

## Residual risk

Attestation farms.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
