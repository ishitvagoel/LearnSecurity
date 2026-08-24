# 4.3 — Sessions, cookies, and tokens (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.

## Property (start here)

A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.

## Attacker capabilities and trust assumptions

- **Attacker:** Referer leak to a CDN; access-log operator; shared screenshot of a URL.
- **Trust:** Local request dict. Real TLS still leaks query to files and analytics.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Session established from a query-string token |
| Failure | Fail closed: Reject query tokens; use cookie/header |

Lab tests: `test_property.py` under `labs/4.3/4.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Session established from a query-string token`
- `--impl fixed`: **pass**

query-only request yields no session.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Magic-link email (still a URL token — time-bound, one-time, 6.6).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
