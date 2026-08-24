# 4.2 — Authentication and phishing-resistant authenticators (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Step-up for export: still origin-bound?

**Product sketch:** Clinic staff SSO portal.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | HTML autocomplete=webauthn is not a ceremony.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/4.2/4.2-lab` stays the only running system you may break.
