# 0.1 — Security engineering orientation

Pass A specification. Lesson prose lives in `lessons/`. A public URL is out of scope even if TCP connects. WSTG is a method catalogue, not a scanning licence. Do not mark Gate 0 complete from this orientation alone without the rest of Phase 0–1 evidence.

## Identity

- **id:** 0.1
- **slug:** security-engineering-orientation
- **title:** Security engineering orientation
- **phase / track / difficulty:** 0 / core / foundation
- **estimatedMinutes:** 240
- **prerequisites:** None; this module opens the course.
- **routeTags:** complete, web-api
- **releaseMilestone:** none
- **masteryGate:** 0

## Objective hierarchy

1. Produce a **scope predicate** so `target_is_authorized("https://example.com/")` is false and named local lab hosts may be true.
2. Name attacker capabilities (tired learner with a proxy) and trust assumptions (this repo’s lab trees; official training apps named in a README).
3. Transfer: contractor asked to “quickly test our customer’s WordPress” — without hitting that host.

## Prerequisite concepts

None. This module teaches the vocabulary the rest of the course uses: vulnerability, threat, risk, control, assurance, compliance, privacy, safety, resilience — and **authorization of the tester**.

## Misconceptions

- If it has a login page it is a lab.
- WSTG chapter titles are the syllabus.
- Defensive learning requires attacking strangers.
- Burp existing is authorization.

## Concept map

Reachability (break) → written host allow-list (this module) → official Juice Shop on your machine OK. Residual: hosts-file aliases; redirects off localhost.

## Invariant prompts

- What must remain true for `https://example.com/`?
- What fails if a redirect leaves 127.0.0.1?

## Threat-model prompts

- What can a tired learner paste into a proxy?
- What written artifact would make a company staging URL in-scope?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/0.1/0.1-orientation`. Forbidden: public host treated as authorized. Do not fetch example.com.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST CSF 2.0 (final) GV/ID: governance language, not a pentest permit.
- OWASP WSTG 4.2 (final): lab **method** catalogue; WSTG 5.0 if cited is **draft**.
- NIST SP 800-181r1 NICE Framework (final, 2020-11); Components v2.2.0 (2026-04-28) are living role language, not a scanning licence.
- WCAG 2.2: scope/stop UI must be keyboard-operable.

## Review triggers

Any URL in-scope; no stop on redirect; live-target language; quiz as scan permission.

## Time budget and SecureCollab

Orientation. Python host allow-list stand-in only.

## Operational considerations

`out_of_scope`. Never store denied-host bodies. Stop and notify instructor.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: reachability is not authorization |
