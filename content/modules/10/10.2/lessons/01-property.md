# 10.2 — Source control, CI/CD, and software supply chain (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
**Mechanism (not the property):** npm audit is 9.4 signal, not this cell.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 10.2 |
|---|---|
| Root cause | Name-only install. |
| Preconditions | install_ok('aaa','bbb') True. |
| Impact (1.1 cell) | Integrity of the artifact you will run. — Malicious code in the TCB. |
| Prevention | Hash pin; deny scripts; provenance. |
| Detection | mismatch fail the job. |
| Recovery | Pin known-good; rotate secrets in CI (5.3). |

## Framework defaults vs application guarantees

npm audit is 9.4 signal, not this cell.

## Mechanism limits and bypasses

Pinning a malicious 1.2.3 still installs malware — review + provenance.

Git dependency to a moving branch; compromised runner.

## Residual risk

Build cache poisoning.

## Practice

Name lockfiles and who can change them.

Run `labs/10.2/10.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

GitHub Actions third-party action@v1.

Clinic: npm install in prod pod.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
