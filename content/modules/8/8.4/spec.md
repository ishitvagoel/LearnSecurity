# 8.4 — Build, distribution, attestation, and resilience

Pass A specification. Lesson prose lives in `lessons/`. No reverse-engineering cookbooks.

## Identity

- **id:** 8.4
- **slug:** build-distribution-attestation-and-resilience
- **title:** Build, distribution, attestation, and resilience
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 8.1; 5.3 secrets in artifacts.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce a **release-channel check** plus deny tests so a debug build cannot call prod export even with `attest=ok`.
2. Name attacker capabilities (leaked debug APK; student build pointed at prod) and trust assumptions (local `api_allowed(build, attest)`).
3. Transfer: clinic debug vs prod FHIR; APK SBOM (10.2) — without treating R8 or root detection as 1.2.

## Prerequisite concepts

8.1 APK hostile; 5.3 no secrets in source; 8.1 Play Integrity is a signal; MAS Testing Profiles in MASTG, not MASVS L1/L2/R.

## Misconceptions

- Obfuscation equals security.
- Play App Signing means we do not care.
- Anti-debug proves the server can trust the client.
- MASVS “R level” is a current MASVS verification level.

## Concept map

Hostile client (8.1) → which *binary* may call prod (this module) → supply chain (10.2) → 5.3 signing keys.

## Invariant prompts

- What must remain true for `api_allowed("debug", "ok")`?
- What fails if minifyEnabled is the only control?

## Threat-model prompts

- What can go wrong when prod trusts any build’s attest string?
- What residual remains if signing keys leak?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/8.4/8.4-lab`. Forbidden: debug build allowed to call production export. No live Play Console.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP MASVS 2.1.0 (final): `MASVS-CODE` (keep the app up to date / processing); `MASVS-RESILIENCE-1` / `RESILIENCE-2` **raise cost**, they do not authorize. No MASVS L1/L2/R.
- OWASP MASTG 2.0.0 (final, June 2026): MAS Testing Profiles (including resilience-oriented profiles) live here / MASWE — not as obsolete MASVS levels.
- OWASP ASVS 5.0.0 (final): `v5.0.0-13.3.1` secrets not in artifacts; `v5.0.0-8.3.1` trusted layer decides the channel.

## Review triggers

Shared debug/release API keys; signing key in repo; resilience checklist as Gate 8 evidence.

## Time budget and SecureCollab

Evidence: channel tests + limitations report. Feeds Gate 8 / M3 (not-attempted).

## Operational considerations

`debug_to_prod_denied`. Revoke debug client ids. Attestation farms remain.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: resilience is cost; MASVS-CODE/RESILIENCE; debug≠prod |
