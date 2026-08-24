# 4.3 — Sessions, cookies, and tokens (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Browser, logger, third-party referrer |
| Objects | access_token query param, session |
| Actions | session_from_request |
| Channels | query, header, cookie, logs |
| TCB | Parser that ignores query tokens. |
| Untrusted | URL, Referer, reverse-proxy logs |
| State / time | Link forwarded in chat months later. |
| 1.1 cell | Authenticity/confidentiality of the session artifact. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| browser | query token | authn | deny |
| browser | HttpOnly cookie | authn | allow-if-valid |
| logger | url | store | no-token |
| cdn | Referer | receive | no-token |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/4.3/4.3-lab` file `token.py`.

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

## Residual risk

Referer on first-party navigations — strip on outbound.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
