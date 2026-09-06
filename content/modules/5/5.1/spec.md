# 5.1 — Data lifecycle and privacy engineering

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 5.1
- **slug:** data-lifecycle-and-privacy-engineering
- **title:** Data lifecycle and privacy engineering
- **phase / track / difficulty:** 5 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.5 authored. 3.1 classified the body; 4.1 deleted the subject.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 5

## Objective hierarchy

1. Produce a **data-flow inventory, retention/deletion matrix, and privacy review** for SecureCollab Phase 1 (notes, analytics, search).
2. Name attacker capabilities (warehouse insider; “de-identified” export) and trust assumptions (Postgres DELETE is not warehouse DELETE).
3. Transfer: clinic appointment card with leftover notes.

## Prerequisite concepts

3.1 field × sink; 4.1 subject delete; 5.5 backups later; 8.2 mobile cache later.

## Misconceptions

- Encryption makes retention OK.
- Privacy equals confidentiality.
- GDPR text in footer is the invariant.

## Concept map

Classification (3.1) → this module’s deletion graph → 5.5 backups / 8.2 mobile.

## Invariant prompts

- What must remain true of analytics after `delete_account`?
- What fails if only the notes row is removed?

## Threat-model prompts

- What can go wrong with a secondary copy after the person left?
- What residual remains in backups and tickets?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/5.1/5.1-lab`. Forbidden: analytics or search still holds the body after delete. No live warehouses.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST Privacy Framework 1.0 (final). Privacy Framework 1.1 IPD **draft**.
- OWASP ASVS 5.0.0 (final): `v5.0.0-14.1.1`, `v5.0.0-14.1.2`, `v5.0.0-14.2.3`, `v5.0.0-14.2.4`; `v5.0.0-14.2.7` **Level 3, labeled advanced**.
- MASVS-PRIVACY named for later mobile; India DPDP **awareness**.

## Review triggers

New copy (warehouse, search, ticket, mobile); superseding Privacy Framework.

## Time budget and SecureCollab

Evidence: inventory, retention/deletion matrix, privacy review. Feeds Gate 5.

## Operational considerations

`deleted_user_body_hits`; warehouse purge SLA; never log bodies.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: deletion-graph mental models; ASVS v5.0.0-14.2.4; v5.0.0-14.2.7 labeled Level 3 advanced; PF 1.1 draft |
