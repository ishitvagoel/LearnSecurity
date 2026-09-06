# 7.1 — API contracts, protocols, and inventory

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 7.1
- **slug:** api-contracts-protocols-and-inventory
- **title:** API contracts, protocols, and inventory
- **phase / track / difficulty:** 7 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.2 writable cells; 6.7 resource accounts (GraphQL cost is a *different* grain).
- **routeTags:** complete, web-api
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **writable-field allow-list** plus deny tests so extra JSON keys cannot set `is_admin`.
2. Name attacker capabilities (authenticated member with extra keys) and trust assumptions (local `apply(user, patch)`).
3. Transfer: clinic PATCH `{is_staff:true}`; GraphQL mutation arguments; gRPC unknown fields — without treating OpenAPI as the control.

## Prerequisite concepts

1.2 authority is a cell, not a costume; 4.4 object×tenant is a coarser grain than a field write; 5.1 extra copies; 6.7 query cost is not extra-key authorization.

## Misconceptions

- If it is not in Swagger it cannot be called.
- GraphQL is self-documenting therefore extra mutation args are safe.
- Versioning is a security control.
- A complete OpenAPI file proves extra keys are ignored.

## Concept map

Writable cells (1.2) → binder vs contract (this module) → field *read* grain (7.2) → GraphQL cost (4.3.1 / 6.7) → unused methods (4.1.4 residual).

## Invariant prompts

- What must remain true if the client document contains `is_admin`?
- What fails if the allow-list lives only in OpenAPI comments?

## Threat-model prompts

- What can go wrong when Pydantic/`dict.update` maps any key?
- What residual remains if REST is allow-listed but GraphQL mutations are not?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/7.1/7.1-lab`. Forbidden: PATCH sets `is_admin` True. No public API attacks.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-15.3.3` (mass assignment, Level 2); `v5.0.0-4.3.2` (GraphQL introspection off in production, Level 2); `v5.0.0-4.3.1` (GraphQL query cost/depth, Level 2 — **different grain** from extra mutation args); `v5.0.0-4.1.4` unused HTTP methods is **Level 3, labeled advanced**.
- OpenAPI Specification 3.1.1 (final): inventory of HTTP operations. Not a runtime allow-list.
- OWASP API Security Top 10:2023 API8/API9 as **awareness after** the cause.

## Review triggers

New PATCH/GraphQL mutation; OpenAPI generated from a different source than handlers; leftover `/v0`.

## Time budget and SecureCollab

Evidence: writable-field matrix, inventory of every protocol, `is_admin` tests. Feeds Gate 7 / M2 (milestone stays not-attempted).

## Operational considerations

`unknown_field_rejected`; `shadow_endpoint_scan`. Do not log the PATCH body. Honest `display_name` XSS is 6.2.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: binder-vs-contract mental models; ASVS v5.0.0-15.3.3; GraphQL 4.3.2/4.3.1; L3 4.1.4 labeled advanced |
