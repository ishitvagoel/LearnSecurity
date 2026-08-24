# 8.4 — Build, distribution, attestation, resilience (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.

## Property (start here)

A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.

## Attacker capabilities and trust assumptions

- **Attacker:** Leaked debug APK; student build pointed at prod.
- **Trust:** Local api_allowed(build, attest).
debug + attest ok => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def api_allowed(build_type, attest):
    return build_type == 'release' and attest == 'ok'
```

## Why this restores the cell

Separate client ids; server checks; signing keys in HSM; no prod in debug manifests.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

minifyEnabled is not this property.

R8/obfuscation does not authorize. Root detection is bypassable.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

SBOM of the APK (10.2).

## Residual risk

Attestation farms.
