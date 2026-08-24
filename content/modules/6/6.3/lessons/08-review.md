# 6.3 — Cross-site and cross-context attacks (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
Review `labs/6.3/6.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Cookie auth + no Origin check
- Seeded smell (label it yourself): GET /share?to= 
- Seeded smell (label it yourself): CORS * with credentials
- Seeded smell (label it yourself): Token in cookie not bound to session

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- SameSite is CSRF done
- JSON APIs cannot CSRF
- CORS is CSRF defense

## Practice

Write three review notes. Do not open the keys file.

## Transfer

postMessage, clickjacking, CORS * with credentials.

## HITL / WCAG 2.2

CSRF errors must be readable (not color-only). Do not make the secure path harder than a cross-site GET that still mutates.
