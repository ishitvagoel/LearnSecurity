# 10.2 — Source control, CI/CD, dependencies, and software supply chain

Pass A specification. Lesson prose lives in `lessons/`. Digest match is the cell — not Dependabot. Do not mark M4 or Gate 10 complete.

## Identity

- **id:** 10.2
- **slug:** source-control-ci-cd-dependencies-and-software-supply-chain
- **title:** Source control, CI/CD, dependencies, and software supply chain
- **phase / track / difficulty:** 10 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.3 secrets; 9.4 scanners as signals; 8.4 APK SBOM named.
- **routeTags:** complete, web-api
- **releaseMilestone:** M4
- **masteryGate:** 10

## Objective hierarchy

1. Produce an **install predicate** so a digest that does not match the lockfile cannot install.
2. Name attacker capabilities (typosquat; compromised maintainer; poisoned fork PR) and trust assumptions (local `install_ok(expected, got)`).
3. Transfer: GitHub Actions `action@v1`; clinic `npm install` in a prod pod — without treating an SBOM or SLSA badge as the hash check.

## Prerequisite concepts

5.3 secrets in CI; 9.4 SCA as signal. SLSA 1.2 provenance; OpenSSF OSPS 2026-08-28; CISA 2026 SBOM minimum elements; NIST SP 800-161r1-upd1. ASVS `v5.0.0-15.1.2` / `v5.0.0-13.3.1`.

## Misconceptions

- Lockfile without verify is integrity.
- Private npm is safe.
- SLSA badge is the app’s 1.2.
- Dependabot is this cell.
- Generating an SBOM verifies installs.

## Concept map

Name-only install (break) → digest pin (this module) → provenance (SLSA) → SBOM inventory (CISA 2026) → secrets in CI (5.3). Residual: pinning malware; cache poisoning.

## Invariant prompts

- What must remain true for `install_ok("aaa", "bbb")`?
- What fails if the SBOM exists but the lockfile is not checked?

## Threat-model prompts

- What can go wrong on a name-only install?
- What residual remains if the pinned digest is already malicious?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/10.2/10.2-lab`. Forbidden: dependency installed when digest mismatches lockfile. No live registry attacks.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- SLSA 1.2 (final): provenance vocabulary; badge is not `install_ok`.
- OpenSSF OSPS Baseline 2026-08-28 (final): project posture.
- CISA 2026 SBOM minimum elements (final): inventory fields, not hash verify.
- NIST SP 800-161r1-upd1 (final): org-level C-SCRM, not the lab oracle.
- OWASP ASVS 5.0.0 (final): `v5.0.0-15.1.2` SBOM inventory (Level 2); `v5.0.0-13.3.1` secrets not in artifacts; `v5.0.0-15.2.4` dependency confusion is **Level 3, labeled advanced**.

## Review triggers

Hash mismatch installs; unpinned action; secrets in fork PRs; SBOM generated but never used.

## Time budget and SecureCollab

Evidence: lockfile verify + SBOM named as inventory. Feeds Gate 10 / M4 (not-attempted).

## Operational considerations

`hash_mismatch_denied`. Pin known-good; rotate CI secrets (5.3). Build cache poisoning remains.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: name-is-not-digest; SBOM inventory; SLSA not 1.2 |
