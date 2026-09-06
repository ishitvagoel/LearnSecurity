# E5 — Large-scale authorization and multi-tenant SaaS

Pass A specification. Lesson prose lives in `lessons/`. A JSON body tenant B must not switch bound tenant A. RLS and ReBAC products are extra layers, not 1.2. Do not mark Gate 7 complete.

## Identity

- **id:** E5
- **slug:** large-scale-authorization-and-multi-tenant-saas
- **title:** Large-scale authorization and multi-tenant SaaS
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 1.2 mediation; 4.4 isolation; 7.1 writable fields; 2.2 cache.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **tenant-binding predicate** so `tenant_for(session A, body B)` stays A.
2. Name attacker capabilities (member of A with a JSON/GraphQL field) and trust assumptions (session binding is TCB; body/RLS-from-body/subdomain are not).
3. Transfer: clinic group practice switching `org_id` in JSON; Zanzibar tuple vs this binding — without a live SaaS tenant.

## Prerequisite concepts

1.2 complete mediation; 4.4 object-and-tenant matrix; 7.1 mass assignment of writable fields; 2.2 cache keys; 5.1 copies.

## Misconceptions

- RLS replaces app mediation.
- Subdomain is an unforgeable tenant.
- Scale means IAM instead of 1.2.
- API1 is the definition of the property.

## Concept map

Client-chosen tenant (break) → session binding (this module) → RLS/ReBAC as extra → copies (search/cache/lake) still bound. Residual: honest super-admin (E6 + 3.3); silent impersonation.

## Invariant prompts

- What must remain true for `tenant_for({A},{B})`?
- What fails if RLS is `SET` from the body?

## Threat-model prompts

- What can a member of A do with tenant B in JSON?
- What residual remains in search indexes and data lakes?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E5/e5-lab`. Forbidden: JSON body switches the bound tenant.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1` / `v5.0.0-8.2.2` isolation; `v5.0.0-15.3.3` mass assignment of the tenant field (related); `v5.0.0-14.2.3` copies not sent as a second controller. `v5.0.0-8.3.2` immediate grant change is **Level 3, labeled advanced**.
- OWASP API Security Top 10 2023 API1 is **awareness after** the binding cause, not the syllabus.

## Review triggers

Body tenant overrides session; RLS from JSON; cache key without tenant; silent impersonation.

## Time budget and SecureCollab

Elective. Python session-binding stand-in only.

## Operational considerations

`body_tenant_mismatch`. Audit tenant B for A's actions.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: body is not the tenant; RLS is not 1.2 |
