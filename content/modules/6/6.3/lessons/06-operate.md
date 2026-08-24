# 6.3 — Cross-site and cross-context attacks (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.

## Property (start here)

A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.

## Attacker capabilities and trust assumptions

- **Attacker:** Evil origin with the victim’s browser session cookie.
- **Trust:** Local allow_share(origin, expected, token).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | csrf_rejected metric. |
| Signal (no bodies) | foreign_origin_post_denied. |
| Revoke / recover | Revoke surprise shares; notify. |
| Residual | User clicking “share” on a lookalike UI — 4.2 phishing. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.3/6.3-lab`.

## Transfer

postMessage, clickjacking, CORS * with credentials.

## Usability

CSRF errors must be readable (not color-only). Do not make the secure path harder than a cross-site GET that still mutates.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
