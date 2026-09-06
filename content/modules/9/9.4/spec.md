# 9.4 — Automated analysis and tool orchestration

Pass A specification. Lesson prose lives in `lessons/`. Tools are signals, not Gate 9.

## Identity

- **id:** 9.4
- **slug:** automated-analysis-and-tool-orchestration
- **title:** Automated analysis and tool orchestration
- **phase / track / difficulty:** 9 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 9.1 coverage; 9.2 review; 9.3 test shape.
- **routeTags:** complete, web-api
- **releaseMilestone:** None
- **masteryGate:** 9

## Objective hierarchy

1. Produce a **ship predicate** so an unmapped HIGH cannot ship.
2. Name attacker capabilities (alert fatigue; dashboard theater) and trust assumptions (local `ship_ok(findings, map)`).
3. Transfer: SCA CVE vs actually called function; clinic 50 unmapped HIGHs — without treating a scanner as 1.2.

## Prerequisite concepts

9.1 mapping; 9.2 human context; 9.3 forbidden-outcome tests. NIST SSDF 1.1 PW.7/PW.8; OWASP SAMM 2.0 as measurement vocabulary; OpenSSF as project posture. SSDF 1.2 IPD **draft**.

## Misconceptions

- Zero findings means secure.
- Tool X replaces ASVS.
- Reachability is optional theater.
- GitHub code scanning default is the ship policy.
- A SAMM score is Gate 9.

## Concept map

Coverage (9.1) → review (9.2) → tests (9.3) → scanner *signals* (this module) → pentest/retest (9.5). Blind spots remain for authz logic.

## Invariant prompts

- What must remain true for `ship_ok([HIGH], {})`?
- What fails if a suppression has no owner?

## Threat-model prompts

- What can go wrong when HIGH findings are unmapped?
- What residual remains after every HIGH is mapped?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/9.4/9.4-lab`. Forbidden: unmapped HIGH finding allows ship. No live GitHub Advanced Security tenants.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-15.2.1` component update timeframes as an SCA *signal*. `v5.0.0-15.2.4` dependency confusion is **Level 3, labeled advanced**.
- NIST SSDF 1.1 (final) PW.7 / PW.8 / RV.1. SSDF 1.2 IPD is **draft**.
- OWASP SAMM 2.0 (final): measurement vocabulary, not a ship sticker.
- OpenSSF OSPS Baseline 2026-08-28 (final): project posture, not `ship_ok`.

## Review triggers

Unmapped HIGH ships; suppressions without owner; SAST offered as Gate 9; no blind-spot note for IDOR.

## Time budget and SecureCollab

Evidence: CI signal design + one mapped/unmapped pair. Feeds Gate 9 (not-attempted).

## Operational considerations

`unmapped_high_blocks`. Do not suppress silently. Authz logic remains a 9.2/9.3 blind spot.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: scanner-is-signal; unmapped HIGH; SAMM as vocabulary |
