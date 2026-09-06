# 11 — Integrating capstone — SecureCollab

Pass A specification. Lesson prose lives in `lessons/`. After revoke, tenant B must not read tenant A’s note — that is 1.2 over time, not a new product. Do not mark M5 or Gate 11 complete.

## Identity

- **id:** 11
- **slug:** integrating-capstone-securecollab
- **title:** Integrating capstone — SecureCollab
- **phase / track / difficulty:** 11 / capstone / capstone
- **estimatedMinutes:** 1200
- **prerequisites:** Blueprint §7; 1.2 mediation; 2.4 time; 4.1/4.4 revoke; 7.4 delayed worker; 9.1 coverage; 10.5 restore.
- **routeTags:** complete, web-api
- **releaseMilestone:** M5
- **masteryGate:** 11

## Objective hierarchy

1. Produce a **read-after-revoke predicate** so `read("n1", "B")` is `None` after `revoke("n1", "B")`.
2. Name attacker capabilities (former collaborator with a cached id; delayed worker 7.4) and trust assumptions (local share map).
3. Transfer: clinic revoke a guardian — without treating a green scanner or a YAML pack as Gate 11.

## Prerequisite concepts

1.2 complete mediation; 2.4 time/TOCTOU; 4.1 logout; 4.4 isolation; 5.1 copies already sent; 7.4 leftover sessions on workers; 8.2 device cache; 9.1 coverage vs spreadsheet; 9.5 retest vs PDF; 10.5 SIEM-green is not recover.

## Misconceptions

- Capstone is a new product.
- Milestones M0–M5 complete because lessons exist.
- Integration tests replace the portfolio.
- A green scanner is the evidence pack.

## Concept map

Always-true read (break) → consult grant on every read (this module) → caches/workers/mobile (2.4 / 7.4 / 8.2) → leftover copies (5.1) → tabletop + restore (10.5). Residual: email already received.

## Invariant prompts

- What must remain true for `read("n1", "B")` after `revoke("n1", "B")`?
- What fails if revoke is an event that never reaches the next read?

## Threat-model prompts

- What can a former collaborator do with a cached note id?
- What residual remains if B already exported the body?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/11/11-lab`. Forbidden: revoked share still reads the note. No live tenants.

## Assessment blueprint

See `module.yaml` assessmentBlueprint. The portable portfolio is blueprint §10.3 (invariants, threat models, ADRs, protocol models, tests, ASVS/MASVS traceability, review/pentest reports, SBOM/pipeline, detection/restore, architecture defense). A numbered “13-item YAML” is not that pack.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1` / `v5.0.0-8.2.2` authorization on every access (Level 2). `v5.0.0-8.3.2` immediate grant change is **Level 3, labeled advanced**.
- Prior pins apply as vocabulary (MASVS 2.1.0 profiles, NIST CSF 2.0 Recover, SLSA 1.2 as provenance not 1.2). No capstone-only standard.

## Review triggers

Read after revoke succeeds; scanner-green README; no cache invalidation; Gate 11 claimed without artifacts.

## Time budget and SecureCollab

Evidence: local revoke test + named portfolio. Feeds Gate 11 / M5 (not-attempted).

## Operational considerations

`revoked_share_read_denied`. Honest copies already made — policy + detect (5.1).

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: revoke is mediation not an event; scanner is not the portfolio |
