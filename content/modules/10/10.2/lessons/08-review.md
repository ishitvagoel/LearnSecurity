# 10.2 — Source control, CI/CD, and software supply chain (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
Review `labs/10.2/10.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/10.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): install_ok True on hash mismatch
- Seeded smell (label it yourself): Unpinned action
- Seeded smell (label it yourself): Secrets in PR from forks
- Seeded smell (label it yourself): SBOM generated but never used

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Lockfile without verify is integrity
- Private npm is safe
- SLSA badge is the app’s 1.2

## Practice

Write three review notes. Do not open the keys file.

## Transfer

GitHub Actions third-party action@v1.
