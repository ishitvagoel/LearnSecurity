# 3.3 — Secure architecture patterns

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 3.3
- **slug:** secure-architecture-patterns
- **title:** Secure architecture patterns
- **phase / track / difficulty:** 3 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–3.2 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 3

## Objective hierarchy

1. Produce **architecture decision records with rejected alternatives** for SecureCollab Phase 1 (runtime DB role vs migrator vs superuser; why not one `DATABASE_URL`).
2. Name attacker capabilities (forgotten WHERE; stolen app password; SQLi later) and trust assumptions (ORM/VPC/microservices are not tenant isolation).
3. Transfer: serverless shared admin string and clinic billing replica — rewrite the invariant without using a Top 10 as the definition of security.

## Prerequisite concepts

1.2 complete mediation; 1.3 TCB vs untrusted; 3.2 change triggers; RLS later in 5.5.

## Misconceptions

- Microservices are automatically isolated.
- RLS replaces application authorization.
- A VPC or private subnet is tenant isolation.
- CISA Secure by Design or SSDF attestation is the GRANT.

## Concept map

Authority (1.2) → boundary (1.3) → this module’s second mediation (roles/planes) → 5.5 RLS.

## Invariant prompts

- What must remain true if the handler forgets a WHERE?
- What fails if the runtime connection is the migrator?

## Threat-model prompts

- What can go wrong if one role serves migrate and serve?
- What residual remains if the `app` password is stolen?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/3.3/3.3-lab`. Forbidden: app role can SELECT another tenant’s rows. No live databases.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- Saltzer and Schroeder 1975 (seminal): least privilege, complete mediation.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.4.1`, `v5.0.0-8.2.2`, `v5.0.0-8.3.1`; `v5.0.0-15.2.5` **Level 3, labeled advanced**.
- CISA Secure by Design: living page; this repo’s pin is **unverified** (403).
- NIST SSDF 1.1 (final); SSDF 1.2 / SP 800-218 Rev. 1 remains **draft**.

## Review triggers

New replica, pooler, worker DB user, or serverless secret; superseding final SSDF 1.2; ASVS revision of V8/V15.

## Time budget and SecureCollab

Evidence: ADRs with rejected alternatives. Blueprint §9.1.

## Operational considerations

`grant_drift` / wrong connection user; rotate; never log bodies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: two-gate and plane-separation models; ASVS 8.4.1; CISA unlabeled as unverified |
