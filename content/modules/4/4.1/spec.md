# 4.1 — Digital identity and account lifecycle

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.1
- **slug:** digital-identity-and-account-lifecycle
- **title:** Digital identity and account lifecycle
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–3.4 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce an **account-lifecycle state machine and recovery threat model** for SecureCollab Phase 1 (enrolled → active → disabled/deleted; leftover artifacts).
2. Name attacker capabilities (stolen cookie after offboard; delayed worker) and trust assumptions (login disabled is not revocation).
3. Transfer: clinic departing clinician.

## Prerequisite concepts

1.2 complete mediation over time; 2.4 leftover workers; 4.3/4.5 tokens later.

## Misconceptions

- Disable login is enough.
- SSO magically revokes.
- Deleted means gone from backups.

## Concept map

Authority (1.2) → this module’s states and leftover sessions → 4.2 recovery / 4.3 tokens / 5.1 backups / 8.2 mobile.

## Invariant prompts

- What must remain true after delete if a cookie is presented?
- What fails if only the profile row is removed?

## Threat-model prompts

- What can go wrong with a copied cookie after HR offboarding?
- What residual remains in backups and mobile caches?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.1/4.1-lab`. Forbidden: leftover session still authenticates after `delete_user`. No live IdPs.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST SP 800-63-4 (final) identity lifecycle.
- OWASP ASVS 5.0.0 (final): `v5.0.0-7.4.2`, `v5.0.0-7.4.1`; `v5.0.0-6.5.6` **Level 3, labeled advanced**.

## Review triggers

New token type, worker identity, mobile cache, or IdP; superseding 800-63.

## Time budget and SecureCollab

Evidence: lifecycle state machine, recovery threat model. Blueprint §9.1. Feeds M1.

## Operational considerations

`session_after_delete`; mass revoke; backups remain (5.1).

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: leftover-session models; ASVS 7.4.2 |
