# 10.1 — Secure software lifecycle and security culture

Pass A specification. Lesson prose lives in `lessons/`. Culture is the merge gate, not a poster. Do not mark M4 or Gate 10 complete.

## Identity

- **id:** 10.1
- **slug:** secure-software-lifecycle-and-security-culture
- **title:** Secure software lifecycle and security culture
- **phase / track / difficulty:** 10 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 3.2 threat modeling; 9.1 coverage; E6 exceptions.
- **routeTags:** complete, web-api
- **releaseMilestone:** M4
- **masteryGate:** 10

## Objective hierarchy

1. Produce a **merge predicate** so a PR cannot merge without a threat-model identifier for the changed surface.
2. Name attacker capabilities (schedule pressure) and trust assumptions (local `merge_ok({})`).
3. Transfer: clinic “HIPAA training complete” as merge; exception path (E6) — without treating CODEOWNERS as a threat model.

## Prerequisite concepts

3.2 threat model; 9.1 living matrix; NIST SSDF 1.1 PW.1; OWASP SAMM 2.0 as maturity vocabulary; CISA Secure by Design as **unverified** manufacturer-ownership guidance. SSDF 1.2 IPD **draft**.

## Misconceptions

- CODEOWNERS is a threat model.
- A security-champion poster is the merge gate.
- Vuln-count KPIs are outcome metrics.
- HIPAA training complete authorizes merge.
- SAMM score is `merge_ok`.

## Concept map

Threat model (3.2) → merge trigger (this module) → tests (9.3) → exceptions (E6) → supply chain (10.2).

## Invariant prompts

- What must remain true for `merge_ok({})`?
- What fails if the tm-id is a rubber stamp?

## Threat-model prompts

- What can go wrong when security is a later phase?
- What residual remains if every PR has a stale tm-id?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/10.1/10.1-lab`. Forbidden: merge without a threat-model identifier.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST SSDF 1.1 (final) PW.1 (design). SSDF 1.2 IPD is **draft**.
- OWASP SAMM 2.0 (final): culture/process measurement, not `merge_ok`.
- CISA Secure by Design: **unverified** living guidance (403s on fetch); manufacturer ownership, not the lab oracle.
- OWASP ASVS 5.0.0 (final): `v5.0.0-15.1.5` documenting dangerous functionality is **Level 3, labeled advanced** — a merge *trigger*, not the predicate.

## Review triggers

Merge without tm; champion optional forever; vanity vuln-count KPI; no change-trigger matrix.

## Time budget and SecureCollab

Evidence: lightweight SSDLC + change-trigger matrix + merge predicate. Feeds Gate 10 / M4 (not-attempted).

## Operational considerations

`merge_blocked_no_tm`. Open a TM, then merge. Count TMs that have tests, not posters.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: culture-is-merge-gate; CODEOWNERS is not TM; SSDF PW.1 |
