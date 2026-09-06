# 8.1 — The hostile-client and mobile-platform model

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs. Android/Kotlin first; iOS is a later mirror.

## Identity

- **id:** 8.1
- **slug:** the-hostile-client-and-mobile-platform-model
- **title:** The hostile-client and mobile-platform model
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.2 server cells; 7.1 extra client keys.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce a **client/server responsibility matrix** plus deny tests so `integrity=ok` on the device does not authorize export.
2. Name attacker capabilities (patched APK, emulator, stolen boolean) and trust assumptions (local `allow_export(client_claim, server_attest)`).
3. Transfer: clinic `hipaaMode=true`; APK feature flags; `premium=true` — without treating Play Integrity as 1.2.

## Prerequisite concepts

1.2 authority is a server cell; 2.3 hostile browser; 7.1 client documents; 8.4 will separate debug/release channels.

## Misconceptions

- Obfuscation is authorization.
- Kotlin/Jetpack is the guarantee.
- Store listing equals device trust.
- Play Integrity is 1.2.
- MASVS L1/L2/R are current levels.

## Concept map

Server 1.2 → hostile APK (this module) → local storage (8.2) → Intents (8.3) → build channel (8.4).

## Invariant prompts

- What must remain true if the client JSON says `integrity=ok`?
- What fails if export is gated only in the Android UI?

## Threat-model prompts

- What can go wrong when policy runs on the attacker’s CPU?
- What residual remains if Play Integrity passes on an emulator farm?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/8.1/8.1-lab`. Forbidden: client `integrity=ok` with failing server attest still exports. No live Play Console or device farms.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP MASVS 2.1.0 (final, January 2024): `MASVS-PLATFORM` (sandbox / other apps); `MASVS-RESILIENCE-1` (platform integrity) is a **cost-raising residual**, not the export grant. Do **not** use obsolete MASVS L1/L2/R. MAS Testing Profiles live in MASTG 2.0.0 / MASWE.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1` function-level on the **server**; `v5.0.0-8.3.1` trusted service layer, not client JS/Kotlin.
- OWASP Mobile Top 10:2024 M7 as **awareness after** the cause.

## Review triggers

Client boolean in a server decision; new attestation API; min-SDK change.

## Time budget and SecureCollab

Evidence: responsibility matrix, client-claim tests. Feeds Gate 8 / M3 (milestone stays not-attempted).

## Operational considerations

`attest_fail_export_denied`. Honest rooted devices are an owned product policy, not a silent grant.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: hostile-client mental models; MASVS 2.1.0 PLATFORM; Play Integrity labeled a signal |
