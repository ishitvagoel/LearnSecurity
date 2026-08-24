# 10.2 — Source control, CI/CD, and software supply chain (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | mismatch fail the job. |
| Signal (no bodies) | hash_mismatch_denied. |
| Revoke / recover | Pin known-good; rotate secrets in CI (5.3). |
| Residual | Build cache poisoning. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/10.2/10.2-lab`.

## Transfer

GitHub Actions third-party action@v1.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
