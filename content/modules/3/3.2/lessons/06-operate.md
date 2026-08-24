# 3.2 — Threat modeling (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | CI fails if required threat ids missing. |
| Signal (no bodies) | model_age_days; missing-mandatory-threat CI. |
| Revoke / recover | Add the threat, tests, owner; do not back-date. |
| Residual | Unknown unknowns — review triggers exist for that. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/3.2/3.2-lab`.

## Transfer

Add webhooks (7.3): which new threats?

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
