# E6 — Product security leadership

Pass A specification. Lesson prose lives in `lessons/`. A risk exception cannot be accepted without owner, review date, and an accessibility check. SAMM/CSF/SSDF are vocabulary. CISA Secure by Design stays unverified. Do not mark Gate 7 complete.

## Identity

- **id:** E6
- **slug:** product-security-leadership
- **title:** Product security leadership
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 1.4 accessibility residual; 10.1 lifecycle; 9.5 retest.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce an **exception predicate** so incomplete records are refused.
2. Name attacker capabilities (calendar; silent exceptions; inaccessible recovery) and trust assumptions (the register schema is TCB; SAMM slides are not).
3. Transfer: clinic “HIPAA exception”; procurement questionnaire vs this record.

## Prerequisite concepts

1.4 accessible recovery; 10.1 SSDLC and exceptions; 9.5 retest vs PDF; 1.1 residual risk as a named cell.

## Misconceptions

- Leadership is soft skills, not invariants.
- Exceptions are failure (they are dated owned residuals).
- Users can always call support instead of accessible recovery.
- A SAMM score is the register row.

## Concept map

Oral acceptance (break) → owned dated record (this module) → roadmap / champions / PSIRT as operate. Residual: unread register; renamed “tech debt.”

## Invariant prompts

- What must remain true for `accept_exception({owner:'', review_by:None})`?
- What fails if WCAG is not in the schema?

## Threat-model prompts

- What happens if an exception is oral?
- What residual remains if recovery is inaccessible?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E6/e6-lab`. Forbidden: incomplete exception accepted.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP SAMM 2.0 (final): measurement vocabulary, not the row.
- NIST CSF 2.0 (final) GV: outcome labels, not the lab oracle.
- NIST SSDF 1.1 (final) PW.1: design-review vocabulary. SSDF 1.2 remains **draft**.
- CISA Secure by Design: **unverified** public guidance (403s historically); not Gate 7.
- ASVS 5.0.0 `v5.0.0-15.1.5` documenting dangerous functionality is **Level 3, labeled advanced**.
- WCAG 2.2 (final): residual inaccessible recovery is in the exception schema.

## Review triggers

Empty owner accepted; no review date; a11y missing; SAMM slide as the exception.

## Time budget and SecureCollab

Elective. Python register stand-in only.

## Operational considerations

`exception_incomplete_denied`. Expire or re-accept with fields.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: exception is a record; SAMM is not the row |
