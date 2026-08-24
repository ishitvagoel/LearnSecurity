# 2.3 — Browser security model (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.

## Property (start here)

A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.

## Attacker capabilities and trust assumptions

- **Attacker:** Injected script in origin (later 6.2); a malicious extension (residual).
- **Trust:** Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.
Review `labs/2.3/2.3-browser-policy/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/2.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): document.cookie used to persist session
- Seeded smell (label it yourself): SECURITY.md equates HttpOnly with “no XSS”
- Seeded smell (label it yourself): CSP Report-Only treated as enforcement (see E2)
- Seeded smell (label it yourself): Missing Secure on the same cookie

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- HttpOnly is XSS defense
- SameSite is CSRF complete
- localStorage is safer than cookies

## Practice

Write three review notes. Do not open the keys file.

## Transfer

React Native WebView cookie bridge.
