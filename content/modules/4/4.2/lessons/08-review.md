# 4.2 — Authentication and phishing-resistant authenticators (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
Review `labs/4.2/4.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/4.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): phishing_resistant('password', evil, real) True
- Seeded smell (label it yourself): Marketing copy “MFA = phishing resistant”
- Seeded smell (label it yourself): Recovery SMS as default
- Seeded smell (label it yourself): No wrong-origin WebAuthn test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Any 2FA is phishing-resistant
- WebAuthn replaces authorization
- Usable login is a nice-to-have

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Step-up for export: still origin-bound?

## HITL / WCAG 2.2

WebAuthn and password fallback must work with keyboard, labels, and no color-only errors (WCAG 2.2). A broken accessible path pushes people to shared passwords.
