# 9.5 — Authorized assessment, reporting, and remediation

Pass A specification. Lesson prose lives in `lessons/`. Scope stays the local lab. A PDF is not a retest.

## Identity

- **id:** 9.5
- **slug:** authorized-assessment-reporting-and-remediation
- **title:** Authorized assessment, reporting, and remediation
- **phase / track / difficulty:** 9 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 9.3 test shape; lab-safety policy (blueprint §9.4).
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 9

## Objective hierarchy

1. Produce a **close predicate** so a finding cannot close without a passing retest of the same forbidden outcome.
2. Name attacker capabilities (paper-compliance; ignored variants) and trust assumptions (local `close_finding({retest})`).
3. Transfer: KEV vs internal-only; clinic pentest PDF shelf — without live-target language.

## Prerequisite concepts

9.3 forbidden-outcome tests; WSTG 4.2 / MASTG 2.0 as catalogues of *what* to retest; CVSS 4.0 as *input*; CISA KEV as exploitation *context*. Authorized local/official scope only.

## Misconceptions

- A PDF report is remediation.
- CVSS 9.8 is the close decision.
- KEV listing authorizes scanning public systems.
- Retesting a different endpoint closes this cell.
- Jira Done is a retest.

## Concept map

Scanner signals (9.4) → authorized assessment of a *named cell* (this module) → same-cell retest → variant hunt. Residual unknown variants.

## Invariant prompts

- What must remain true for `close_finding({retest: None})`?
- What fails if CVSS is the only priority input?

## Threat-model prompts

- What can go wrong when findings close on intent?
- What residual remains after a passing retest of one endpoint?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/9.5/9.5-lab`. Forbidden: finding closed without retest. No live-target pentest instructions.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP WSTG 4.2 (final): catalogue of *what* to retest. WSTG 5.0 is **draft** if cited.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1` as the example cell. `v5.0.0-8.3.2` is **Level 3, labeled advanced** (retest after role change, not a different URL).
- FIRST CVSS 4.0 (final): severity *input*, not the close predicate.
- CISA KEV (awareness): exploitation context, not authorization to scan public systems.
- NIST SSDF 1.1 RV.1 / RV.2. SSDF 1.2 IPD is **draft**.

## Review triggers

Close without retest; CVSS-only priority; live-target language; no variant search.

## Time budget and SecureCollab

Evidence: three-line report (cause, impact, retest cmd) + close predicate. Feeds Gate 9 (not-attempted).

## Operational considerations

`finding_closed_without_retest`. Reopen. Hunt variants of the same root cause.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: report-is-not-retest; CVSS as input; KEV as context; local scope |
