# 4.2 — Authentication and phishing-resistant authenticators (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
**Mechanism (not the property):** HTML autocomplete=webauthn is not a ceremony.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 4.2 |
|---|---|
| Root cause | Shared secret replayable at the wrong origin. |
| Preconditions | password method returns True for evil origin. |
| Impact (1.1 cell) | Authenticity of the principal to *this* origin. — Attacker obtains session at the real app (then 1.2). |
| Prevention | WebAuthn origin/RP ID binding; do not call passwords resistant. |
| Detection | Impossible-travel / new-device (weak); user reports. |
| Recovery | Revoke sessions; force re-bind authenticators. |

## Framework defaults vs application guarantees

HTML autocomplete=webauthn is not a ceremony.

## Mechanism limits and bypasses

WebAuthn does not authorize (1.2). Recovery paths can re-introduce phishable secrets (1.4, 4.1).

Prompt bombing; compromised authenticator; recovery email.

## Residual risk

Users with only passwords — honest residual, not a slogan.

## Practice

Table: method × origin × expected.

Run `labs/4.2/4.2-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Step-up for export: still origin-bound?

Clinic staff SSO portal.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

WebAuthn and password fallback must work with keyboard, labels, and no color-only errors (WCAG 2.2). A broken accessible path pushes people to shared passwords.
