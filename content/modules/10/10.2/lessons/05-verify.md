# 10.2 — Source control, CI/CD, and software supply chain (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Dependency installed when digest mismatches lockfile |
| Failure | Fail closed: Hash pin; deny scripts; provenance |

Lab tests: `test_property.py` under `labs/10.2/10.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Dependency installed when digest mismatches lockfile`
- `--impl fixed`: **pass**

mismatch refuses install.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

GitHub Actions third-party action@v1.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
