# 4.3 — Sessions, cookies, and tokens (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
**Forbidden outcome:** Session established from a query-string token

**Authorized scope:** `labs/4.3/4.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable token.py accepts query sessions.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: session_from_request reads access_token query.

## Vulnerable fixture (local)

```python
def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    return query.get("access_token") or cookie.get("sc_session") or header
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Token placed in a logged, shared channel. |
| Impact | Session theft without XSS. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/4.3/4.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

## Non-goals

No live-target instructions. Synthetic data only.
