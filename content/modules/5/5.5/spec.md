# 5.5 — Database and persistence security

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 5.5
- **slug:** database-and-persistence-security
- **title:** Database and persistence security
- **phase / track / difficulty:** 5 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.2 cells; 3.3 DB-role second gate; 5.1 deletion graph for backups/replicas.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 5

## Objective hierarchy

1. Produce a **schema / role / constraint map** plus bound-query tests for SecureCollab note fetch.
2. Name attacker capabilities (hostile `note_id` as SQL grammar) and trust assumptions (bound API; 3.3 role is a second gate).
3. Transfer: clinic search box; NoSQL/GraphQL args wait for 7.1.

## Prerequisite concepts

1.2 object-and-tenant grants; 3.3 `app` role must not SELECT another tenant; 5.1 copies on replicas; 6.1 same data-vs-grammar shape for shells.

## Misconceptions

- ORM means no injection.
- RLS replaces parameterization or 1.2.
- A denylist of quotes is complete mediation.

## Concept map

Grant cells (1.2) → interpreter isolation (this module) → DB-role second gate (3.3) → backups/replicas (5.1).

## Invariant prompts

- What must remain true if `note_id` contains SQL punctuation?
- What fails if 1.2 is correct but the query string is concatenated?

## Threat-model prompts

- What can go wrong when data and SQL grammar share one string?
- What residual remains if parameters are bound but ORDER BY is still concatenated?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/5.5/5.5-lab`. Forbidden: concatenated SQL; live database attacks. The test fragment is data, not a cookbook.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-1.2.4`, `v5.0.0-8.4.1`, `v5.0.0-13.2.2`; `v5.0.0-16.3.2` **Level 3 clause labeled advanced**.
- PostgreSQL row-security documentation as **platform**, not the property.

## Review triggers

New query builder, search DSL, replica, or migrator role; superseding **final** ASVS encoding chapter.

## Time budget and SecureCollab

Evidence: bound `fetch_sql`, role matrix, named backup/restore residual. Feeds Gate 5.

## Operational considerations

`sql_error_spike`; `grant_drift` from 3.3. Never log SQL with bound values that are note bodies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: data-vs-SQL-grammar and three-gate mental models; ASVS v5.0.0-1.2.4; L3 16.3.2 labeled advanced |
