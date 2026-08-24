# 4.2 — Authentication and phishing-resistant authenticators (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Impossible-travel / new-device (weak); user reports. |
| Signal (no bodies) | webauthn_fail_origin; recovery_used (higher risk). |
| Revoke / recover | Revoke sessions; force re-bind authenticators. |
| Residual | Users with only passwords — honest residual, not a slogan. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/4.2/4.2-lab`.

## Transfer

Step-up for export: still origin-bound?

## Usability

WebAuthn and password fallback must work with keyboard, labels, and no color-only errors (WCAG 2.2). A broken accessible path pushes people to shared passwords.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
