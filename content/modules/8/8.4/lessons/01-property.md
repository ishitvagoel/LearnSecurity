# 8.4 — Build, distribution, attestation, resilience (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
**Mechanism (not the property):** minifyEnabled is not this property.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 8.4 |
|---|---|
| Root cause | Prod API trusts a client claim of attest=ok from any build. |
| Preconditions | api_allowed('debug','ok') True. |
| Impact (1.1 cell) | Integrity of the release channel. — Debug keys, loggers, extra exports against prod data. |
| Prevention | Separate client ids; server checks; signing keys in HSM; no prod in debug manifests. |
| Detection | debug_client_to_prod. |
| Recovery | Revoke debug client id; rotate. |

## Framework defaults vs application guarantees

minifyEnabled is not this property.

## Mechanism limits and bypasses

R8/obfuscation does not authorize. Root detection is bypassable.

Repackaged release signature if keys leak (5.3).

## Residual risk

Attestation farms.

## Practice

Where are signing keys; who can push to the store.

Run `labs/8.4/8.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

SBOM of the APK (10.2).

Clinic: debug build against prod FHIR.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
