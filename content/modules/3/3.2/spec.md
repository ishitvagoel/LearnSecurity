# 3.2 — Threat modeling

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 3.2
- **slug:** threat-modeling
- **title:** Threat modeling
- **phase / track / difficulty:** 3 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–3.1 authored; Phase 1–2 Pass A already exists.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 3

## Objective hierarchy

1. Produce a **version-controlled threat model** for SecureCollab Phase 1 (assets, data flows, trust boundaries, named threats with owners and review triggers, decision history).
2. Name attacker capabilities (cross-tenant member; hostile Next.js client; future worker identity) and trust assumptions (scanner output is coverage, not the model).
3. Transfer: Clinic SMS reminders — rewrite the invariant for a new channel without using a Top 10 as the definition of security.

## Prerequisite concepts

Properties (1.1), authority cells (1.2), trust boundaries (1.3), residual risk (1.4), parsers (2.1), request path (2.2), browser (2.3), state/time (2.4), classification/sinks (3.1).

## Misconceptions

- A green scanner means there are no threats.
- Threat models are a pre-code ceremony; they do not live in git.
- STRIDE letters on a DFD are a model even without assets, owners, or invalidation conditions.
- OWASP Top 10 / CWE Top 25 are the threat list or a compliance baseline.
- ASVS 5.0 still has a numbered “do threat modeling” requirement (it does not).

## Concept map

Property (1.1) → authority (1.2) → boundary (1.3) → classification (3.1) → this module’s versioned model and change triggers.

## Invariant prompts

- What must remain true if every CVE scanner is green?
- What fails if this control is skipped on an indirect path (worker, webhook, SMS)?

## Threat-model prompts

- What can go wrong for Phase 1 notes, share grants, and session cookies?
- What residual remains if prevention fails, and who owns the trigger to revisit?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08, seven-step loop).

## Lab briefs

Authorized **local** `labs/3.2/3.2-lab` only. Forbidden outcome: a green scanner produces an empty SecureCollab threat model (missing `cross-tenant-read`). Forbidden: live targets, real PII, weaponized lesson payloads.

## Assessment blueprint

See `module.yaml` assessmentBlueprint. Mastery states: not-attempted | developing | competent | transfer-ready. No compensating averages.

## Standards references

- OWASP Threat Modeling Project (maintained guidance, live-checked 2026-09-06): Four Question Framework; methodology-neutral; STRIDE/LINDDUN/PASTA as options, not a single OWASP method.
- NIST SP 800-154 IPD (March 2016) remains **draft**; NIST 2025-01-23 note still plans to finalize. Informative data-centric modeling only.
- OWASP ASVS 5.0.0 (final): `v5.0.0-15.1.3` (Level 2 documented security decisions); `v5.0.0-15.1.5` **Level 3, labeled advanced** (dangerous-functionality documentation). ASVS 5.0 removed a numbered “do threat modeling” item; Appendix D recommends the process as awareness, not a verification ID. No ASVS 4.x. No MASVS L1/L2/R.

## Review triggers

New share path, worker identity, webhook, SMS/email channel, or client surface; superseding **final** SP 800-154; ASVS revision that restores or relocates architecture documentation requirements.

## Time budget and SecureCollab

Blueprint §9.1 phase evolution. Evidence: version-controlled threat model with open assumptions, owners, review triggers, and decision history.

## Operational considerations

Pair prevention with detection and recovery: `missing-mandatory-threat` CI; `model_age_days` after a trigger; do not back-date the model. Unknown unknowns remain; triggers exist for that.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: four-questions and scanner-is-coverage models; ASVS 5.0 Appendix D labeled awareness |
