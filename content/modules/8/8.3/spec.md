# 8.3 — Network, deep links, WebViews, and inter-app communication

Pass A specification (map-complete). Expand lesson-quality in a later revision. No exploit walkthroughs.

## Identity

- **id:** 8.3
- **slug:** network-deep-links-webviews-and-inter-app-communication
- **title:** Network, deep links, WebViews, and inter-app communication
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; Phase 1–2 Pass A already exists.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce **Malicious-app/link harness and IPC review** for SecureCollab (or the elective system).
2. Name attacker capabilities, trust assumptions, and a local authorized lab brief.
3. Transfer: a materially changed case without using a Top 10 as the definition of security.

## Prerequisite concepts

Prior modules on the §7 graph.

## Misconceptions

- This topic is a vulnerability-name list.
- Framework or cloud defaults are the application guarantee.
- Awareness documents (Top 10, CWE Top 25) are compliance.

## Concept map

Property (1.1) → authority (1.2) → boundary (1.3) → this module’s mechanism and evidence.

## Invariant prompts

- What must remain true if the client is hostile?
- What fails if this control is skipped on an indirect path?

## Threat-model prompts

- What can go wrong for the assets in this module?
- What residual remains if prevention fails?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08, seven-step loop).

## Lab briefs

Authorized **local course fixture** (or official training lab). Forbidden: live targets, real PII, weaponized lesson payloads.

## Assessment blueprint

See `module.yaml` assessmentBlueprint. Mastery states: not-attempted | developing | competent | transfer-ready. No compensating averages.

## Standards references

MASVS-NETWORK/PLATFORM/AUTH; RFC 8252 — label drafts (OAuth 2.1, SSDF 1.2, Privacy FW 1.1, WebAuthn L3 CR, NIST 800-154, CSP3, Trusted Types) as non-final. ASVS IDs when pinned later: `v5.0.0-…`. No ASVS 4.x. No MASVS L1/L2/R.

## Review triggers

Material SecureCollab change in this concern; superseding **final** standard.

## Time budget and SecureCollab

Blueprint §9.1 phase evolution. Evidence: Malicious-app/link harness and IPC review.

## Operational considerations

Pair prevention with detection and recovery where prevention is not absolute.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
