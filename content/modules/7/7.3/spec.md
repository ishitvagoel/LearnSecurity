# 7.3 — Webhooks, callbacks, and third-party APIs

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs. No live Stripe/GitHub attacks.

## Identity

- **id:** 7.3
- **slug:** webhooks-callbacks-and-third-party-apis
- **title:** Webhooks, callbacks, and third-party APIs
- **phase / track / difficulty:** 7 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.2 MAC vs encoding; 2.1 parsers; 6.5 egress.
- **routeTags:** complete, web-api
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **raw-body MAC check** plus deny tests so a missing signature is rejected.
2. Name attacker capabilities (anyone who can POST the callback URL) and trust assumptions (local `accept(sig, body, secret)`).
3. Transfer: clinic lab-result webhook; signed redirects; outbound SSRF (6.5) — without claiming “we are Stripe.”

## Prerequisite concepts

TLS hop authenticity (5.4) is not message authenticity; 2.1 duplicate-key / parse-then-MAC; 6.5 untrusted URLs; 1.2 on side effects.

## Misconceptions

- TLS to us proves the sender.
- IP allow-list is authenticity.
- Webhooks are just APIs in reverse so JWT login applies.
- Vendor SDK verify equals a custom MAC over parsed JSON.

## Concept map

TLS hop (5.4) → provider-message MAC (this module) → 1.2 on the resulting action → replay/freshness (2.3.x) → outbound URL (6.5).

## Invariant prompts

- What must remain true if the POST hits `/webhook` with an empty signature?
- What fails if `json.loads` runs before the MAC (2.1)?

## Threat-model prompts

- What can go wrong when the path is the only check?
- What residual remains if a valid MAC still shares a note without a 1.2 grant?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/7.3/7.3-lab`. Forbidden: unsigned body accepted. Disposable `lab-secret`. No live provider attacks.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-11.2.1` (industry-validated crypto for HMAC, Level 2); `v5.0.0-2.3.4` (replay / consume-once, Level 2); `v5.0.0-2.3.3` (freshness, Level 2); `v5.0.0-4.1.5` per-message digital signatures is **Level 3, labeled advanced**.
- OWASP API Security Top 10:2023 API10 as **awareness after** the cause.

## Review triggers

New inbound webhook; parse-before-MAC; tenant-supplied callback URL.

## Time budget and SecureCollab

Evidence: signed protocol notes, missing-sig tests. Feeds Gate 7 / M2 (milestone stays not-attempted).

## Operational considerations

`webhook_sig_fail`; `replay_window`. Rotate disposable secrets. Do not log bodies or secrets.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: path-vs-MAC mental models; ASVS v5.0.0-11.2.1 / 2.3.4; L3 4.1.5 labeled advanced |
