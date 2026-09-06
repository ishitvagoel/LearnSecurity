# 4.4 — Authorization and tenant isolation

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.4
- **slug:** authorization-and-tenant-isolation
- **title:** Authorization and tenant isolation
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.3 authored. 1.2 named the cells; this module executes them. 3.3 is a second (DB-role) mediation, not a substitute.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce an **executable authorization matrix and cross-tenant tests** for SecureCollab Phase 1 (`can_read` keyed by subject, tenant, and note).
2. Name attacker capabilities (grant-holder who swaps `note_id`; admin role costume) and trust assumptions (login is not a grant; UUID is not a grant).
3. Transfer: clinic appointment A ≠ chart B.

## Prerequisite concepts

1.2 complete mediation; 3.3 DB-role second gate; 4.1 leftover sessions; 7.2 property-level later; 5.5 RLS later; 7.4 workers later.

## Misconceptions

- IDOR is a scanner finding not a missing cell.
- RBAC role replaces object grants.
- Signed ids are capabilities.

## Concept map

Authority (1.2) → this module’s object+tenant lookup → 3.3 DB role / 5.5 RLS as extra gates → 7.2 field-level / 7.4 workers.

## Invariant prompts

- What must remain true if bob holds a grant on n1 and requests n2?
- What fails if an admin role is treated as a cross-tenant capability?

## Threat-model prompts

- What can go wrong when the client supplies `note_id`?
- What residual remains on search, export, GraphQL, and workers?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.4/4.4-lab`. Forbidden: grant on n1 authorizes n2; owner/admin costumes that skip tenant or object keys. No live tenants.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- Saltzer and Schroeder (1975, seminal) complete mediation and fail-safe defaults.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.3.1`, `v5.0.0-8.4.1`; `v5.0.0-8.3.2` and `v5.0.0-8.3.3` **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API1/API3/API5 **awareness** after the matrix.

## Review triggers

New path (search, export, GraphQL, worker), new tenant model, or superseding ASVS.

## Time budget and SecureCollab

Evidence: executable matrix and cross-tenant tests. Blueprint §9.1. Feeds M1 / Gate 4.

## Operational considerations

`authz_deny`; grant-table drift; never log bodies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: object-keyed grant and tenant-key mental models; ASVS v5.0.0-8.2.2 / 8.4.1; L3 8.3.2 / 8.3.3 labeled advanced |
