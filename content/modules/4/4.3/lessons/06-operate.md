# 4.3 — Sessions, cookies, and tokens (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Access logs containing token-shaped query keys. |
| Signal (no bodies) | query_token_rejected; log-redact gateway. |
| Revoke / recover | Revoke those tokens; rotate. |
| Residual | Referer on first-party navigations — strip on outbound. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/4.3/4.3-lab`.

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
