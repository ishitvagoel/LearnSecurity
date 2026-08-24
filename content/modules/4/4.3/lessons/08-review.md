# 4.3 — Sessions, cookies, and tokens (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
Review `labs/4.3/4.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/4.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): session_from_request uses query
- Seeded smell (label it yourself): JWT in localStorage as “SPA best practice” 2016 blog
- Seeded smell (label it yourself): No Referer policy
- Seeded smell (label it yourself): Tokens printed in uvicorn logs

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- JWT is more secure than sessions
- Query strings are private over HTTPS
- Logout clears stolen tokens automatically

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).
