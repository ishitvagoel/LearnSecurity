# 3.4 — Business logic and abuse-resistant design (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.

## Property (start here)

A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.

## Attacker capabilities and trust assumptions

- **Attacker:** A scripted member; a confused deputy UI that retries (2.4).
- **Trust:** Local counter. Real rate limits are 6.7.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | share_cap_denied metric; anomaly on one note. |
| Signal (no bodies) | denied 6th share; lock contention on hot notes. |
| Revoke / recover | Trim extra grants; notify owner. |
| Residual | Legitimate teams >5 need an owned exception (E6). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/3.4/3.4-lab`.

## Transfer

Invite tokens (6.6) and export quotas (6.7).

## Usability

Error “share limit reached” must be programmatically announced (WCAG 4.1.3), not only a red border.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
