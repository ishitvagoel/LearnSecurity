# 8.3 — Network, deep links, WebViews, and inter-app communication

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs. No live malicious APKs.

## Identity

- **id:** 8.3
- **slug:** network-deep-links-webviews-and-inter-app-communication
- **title:** Network, deep links, WebViews, and inter-app communication
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 8.1; 4.5 / RFC 8252; 2.1 query strings.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce an **exported-component inventory** plus deny tests so `as=admin` does not switch the session.
2. Name attacker capabilities (malicious app sending an Intent; crafted https link) and trust assumptions (local `open_link` / `current_user`).
3. Transfer: clinic `as=doctor`; OAuth native redirect (4.5) — without treating verified App Links as trusted input.

## Prerequisite concepts

2.1 untrusted query; 4.3 session channel; 4.5 claimed HTTPS redirects; 6.2 WebView is another HTML interpreter; 8.1 hostile client.

## Misconceptions

- HTTPS App Links are trusted input.
- WebView is just Chrome so 2.3 applies unchanged.
- IPC is private to our app.
- `exported=false` is the default on every API level.

## Concept map

Hostile client (8.1) → Intents/links (this module) → WebView grammar (6.2) → native OAuth (4.5).

## Invariant prompts

- What must remain true after `open_link({as: admin})`?
- What fails if App Links are verified but `as=` still binds?

## Threat-model prompts

- What can go wrong when extras become the session?
- What residual remains if a WebView bridge can export?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/8.3/8.3-lab`. Forbidden: `as=` switches the signed-in user. No live Play Store apps.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP MASVS 2.1.0 (final): `MASVS-PLATFORM-1` (IPC); `MASVS-PLATFORM-2` (WebViews); `MASVS-NETWORK-1`; `MASVS-AUTH-1`. No MASVS L1/L2/R. Related MASWE-0029 insecure deep links named as awareness of the weakness family, not a live-target test.
- IETF RFC 8252 (final): claimed HTTPS redirects for native OAuth; custom schemes are a residual.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.3.1` authorization at a trusted service layer — the session is not taken from Intent extras.

## Review triggers

New exported component; WebView bridge; OAuth redirect.

## Time budget and SecureCollab

Evidence: IPC inventory + `as=` tests. Feeds Gate 8 / M3 (not-attempted).

## Operational considerations

`deeplink_identity_ignored`. User installing an attacker app is an OS-model residual.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: Intent as untrusted input; MASVS-PLATFORM-1/2; RFC 8252 |
