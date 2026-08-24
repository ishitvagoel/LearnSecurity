# 8.4 — Build, distribution, attestation, resilience (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** SBOM of the APK (10.2).

**Product sketch:** Clinic: debug build against prod FHIR.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | minifyEnabled is not this property.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/8.4/8.4-lab` stays the only running system you may break.
