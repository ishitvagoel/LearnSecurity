# 9.1 — Verification requirements and traceability

Pass A specification. Lesson prose lives in `lessons/`. Do not mark Gate 9 complete.

## Identity

- **id:** 9.1
- **slug:** verification-requirements-and-traceability
- **title:** Verification requirements and traceability
- **phase / track / difficulty:** 9 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.2 isolation; 4.4 object grain; 8.2 MASVS-STORAGE as a mobile row.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 9

## Objective hierarchy

1. Produce a **coverage predicate** so `AUTHZ-1` is not “done” without an isolation assert.
2. Name attacker capabilities (optimistic status column; empty CI) and trust assumptions (local `covered(req, tests)`).
3. Transfer: MASVS-STORAGE for 8.2; clinic HIPAA “done” column — without treating a spreadsheet as coverage.

## Prerequisite concepts

1.2 / 4.4 isolation tests; ASVS 5.0.0 as the web/API backbone (Level 2 normal, selected Level 3 advanced); MASVS 2.1.0 + MASTG 2.0.0 profiles for mobile; SSDF 1.1 final; SSDF 1.2 IPD **draft**.

## Misconceptions

- ASVS certification exists as a sticker.
- Number of tests is coverage.
- Green build is Gate 9.
- Copied-wholesale ASVS is a tailored matrix.
- Exceptions without expiry are still coverage (see E6).

## Concept map

Threat → requirement → test → result (this module) → review (9.2) → test shape (9.3) → tools (9.4) → exceptions (E6).

## Invariant prompts

- What must remain true for `covered("AUTHZ-1", status_only_row)`?
- What fails if Level 3 is marked done without a cache-after-role-change test?

## Threat-model prompts

- What can go wrong when status=done has no isolation assert?
- What residual remains if every L2 row has a test but L3 is unnamed?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/9.1/9.1-lab`. Forbidden: status-only row counted as AUTHZ-1 coverage. No live ASVS “certification” portals.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): Level 2 is the normal web/API target. `v5.0.0-8.2.1` (function-level) and `v5.0.0-8.2.2` (object-level) are the AUTHZ-1 example. `v5.0.0-8.3.2` immediate grant change is **Level 3, labeled advanced** — still needs a test, not a “done” cell.
- OWASP MASVS 2.1.0 (final) + MASTG 2.0.0 (final): mobile backbone; STORAGE for 8.2. No MASVS L1/L2/R.
- NIST SSDF 1.1 (SP 800-218, final): PW.1 / PW.8 vocabulary. SSDF 1.2 (SP 800-218 Rev. 1 IPD) is **draft**.

## Review triggers

Status-only coverage; wholesale ASVS paste; exceptions without expiry; Gate 9 claimed from a spreadsheet.

## Time budget and SecureCollab

Evidence: living assurance case with one isolation-mapped row. Feeds Gate 9 (not-attempted).

## Operational considerations

`unmapped_req_blocks_release`. Do not backfill “done.”

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: coverage-predicate mental models; ASVS L2 vs L3; SSDF 1.2 labeled draft |
