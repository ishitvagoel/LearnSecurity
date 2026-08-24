# 8.4 — Build, distribution, attestation, resilience (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Debug build allowed to call production export |
| Failure | Fail closed: Separate client ids; server checks; signing keys in HSM; no prod in debug manifests |

Lab tests: `test_property.py` under `labs/8.4/8.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Debug build allowed to call production export`
- `--impl fixed`: **pass**

debug cannot call prod export.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

SBOM of the APK (10.2).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
