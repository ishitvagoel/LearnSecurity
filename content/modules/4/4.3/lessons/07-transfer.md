# 4.3 — Sessions, cookies, and tokens (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Magic-link email (still a URL token — time-bound, one-time, 6.6).

**Product sketch:** Clinic appointment deep link.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | OAuth “implicit in URL” is obsolete; copying it is not ASVS.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/4.3/4.3-lab` stays the only running system you may break.
