# 3.3 — Secure architecture patterns (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | pg_audit on cross-tenant seqscans. |
| Signal (no bodies) | grant_drift check in CI; connection-user metric. |
| Revoke / recover | Rotate DB password; review grants. |
| Residual | Stolen migrator role — separate credential, shorter life. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/3.3/3.3-lab`.

## Transfer

Serverless function with a shared “admin” connection string.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
