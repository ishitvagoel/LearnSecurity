# 4.2 — Authentication, phishing resistance, and usable access

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.2
- **slug:** authentication-phishing-resistance-and-usable-access
- **title:** Authentication, phishing resistance, and usable access
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.1 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce an **authenticator decision record and accessible-flow review** for SecureCollab Phase 1 (password/OTP phishable; WebAuthn origin-bound).
2. Name attacker capabilities (lookalike origin; intercepted password) and trust assumptions (URL-reading is not a TCB).
3. Transfer: clinic staff SSO; step-up for export still origin-bound.

## Prerequisite concepts

1.1 authenticity; 1.2 after session mint; 1.4 usable path; 4.1 leftover sessions.

## Misconceptions

- Any 2FA is phishing-resistant.
- WebAuthn replaces authorization.
- Usable login is a nice-to-have.

## Concept map

Lifecycle (4.1) → this module’s authenticator × origin → 4.3 session channel → 4.5 federation.

## Invariant prompts

- What must remain true if the user types a password at evil.example?
- What fails if WebAuthn ignores RP ID?

## Threat-model prompts

- What can go wrong with OTP as “MFA”?
- What residual remains for password-only users?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.2/4.2-lab`. Forbidden: password or wrong-origin WebAuthn counted as phishing-resistant. No live phishing sites.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST SP 800-63B-4 (final).
- W3C WebAuthn Level 3 **Candidate Recommendation**.
- OWASP ASVS 5.0.0 `v5.0.0-6.3.3` (Level 2 MFA; Level 3 hardware phishing-resistant **labeled advanced**).
- WCAG 2.2 (final).

## Review triggers

New recovery path; WebAuthn becoming Rec; new step-up.

## Time budget and SecureCollab

Evidence: authenticator decision record, accessible-flow review. Feeds M1.

## Operational considerations

`webauthn_fail_origin`; `recovery_used`. Do not log secrets.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: origin-binding models; WebAuthn labeled CR |
