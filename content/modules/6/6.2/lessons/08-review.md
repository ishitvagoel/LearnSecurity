# 6.2 — Browser injection and active content (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
Review `labs/6.2/6.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Template concatenates title
- Seeded smell (label it yourself): CSP Report-Only as the fix
- Seeded smell (label it yourself): No &lt; test
- Seeded smell (label it yourself): Sanitizer after innerHTML assignment

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- CSP replaces encoding
- HttpOnly makes XSS harmless
- Markdown is inert

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).
