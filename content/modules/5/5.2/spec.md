# 5.2 — Cryptographic properties and safe use

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 5.2
- **slug:** cryptographic-properties-and-safe-use
- **title:** Cryptographic properties and safe use
- **phase / track / difficulty:** 5 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.1 authored. Keys wait for 5.3; TLS is 5.4.
- **routeTags:** complete, web-api
- **releaseMilestone:** null
- **masteryGate:** 5

## Objective hierarchy

1. Produce a **crypto decision table and misuse-focused tests** (encoding ≠ AEAD; Argon2 is for passwords).
2. Name attacker capabilities (storage observer) and trust assumptions (column name is not confidentiality).
3. Transfer: clinic SSN column labeled encrypted that is Base64.

## Prerequisite concepts

1.1 confidentiality; 4.3 JWT-as-format; 5.3 keys; 5.4 TLS.

## Misconceptions

- HTTPS means data at rest is encrypted.
- Base64 is hashing.
- Stronger algorithm fixes a bad key story.

## Concept map

Property (confidentiality) → this module’s algorithm family → 5.3 key lifecycle.

## Invariant prompts

- What must remain true if a DB admin reads the column?
- What fails if `protect` is Base64?

## Threat-model prompts

- What can go wrong when the mechanism name is “encrypted”?
- What residual remains with nonce reuse or the key in the same row?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/5.2/5.2-lab`. Forbidden: protect reversible as Base64. Teaching stand-in is not a real cipher.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-11.2.1`, `v5.0.0-11.3.2`, `v5.0.0-11.3.3`; `v5.0.0-11.3.4` and `v5.0.0-11.1.4` **Level 3, labeled advanced**.
- RFC 9106 Argon2 (final) for passwords, not this field.

## Review triggers

New field, new algorithm family, or superseding ASVS/RFC.

## Time budget and SecureCollab

Evidence: crypto decision table and misuse tests. Feeds Gate 5.

## Operational considerations

Known-plaintext Base64 CI check; never log plaintext.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: encoding-vs-encryption mental models; ASVS v5.0.0-11.3.3; L3 nonce/PQC labeled advanced |
