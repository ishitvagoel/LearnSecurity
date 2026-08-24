# 4.3 — Sessions, cookies, and tokens (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
query access_token => None.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    if query.get("access_token"):
        return None
    return cookie.get("sc_session") or header
```

## Why this restores the cell

Reject query tokens; use cookie/header.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

OAuth “implicit in URL” is obsolete; copying it is not ASVS.

Authorization header still logs at some gateways — redact.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

## Residual risk

Referer on first-party navigations — strip on outbound.
