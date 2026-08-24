# 10.2 — Source control, CI/CD, and software supply chain (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
aaa vs bbb => False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def install_ok(expected_hash, got_hash):
    return expected_hash == got_hash
```

## Why this restores the cell

Hash pin; deny scripts; provenance.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

npm audit is 9.4 signal, not this cell.

Pinning a malicious 1.2.3 still installs malware — review + provenance.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

GitHub Actions third-party action@v1.

## Residual risk

Build cache poisoning.
