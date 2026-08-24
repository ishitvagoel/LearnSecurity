# 5.1 — Data lifecycle and privacy engineering (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Job that searches analytics for deleted user ids (careful with logs). |
| Signal (no bodies) | deleted_user_body_hits; warehouse SLA for purge. |
| Revoke / recover | Purge warehouse partitions; notify if required by policy (not fake GDPR theater). |
| Residual | Legal hold copies — named exception with owner (E6). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/5.1/5.1-lab`.

## Transfer

CSV export to a partner; clinic-booking card PHI.

## Usability

Delete-account journey must be completable with keyboard and clear status (WCAG 3.3.x). An unreachable delete is a privacy incident (1.4).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
