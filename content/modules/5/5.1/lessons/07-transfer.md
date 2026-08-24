# 5.1 — Data lifecycle and privacy engineering (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** CSV export to a partner; clinic-booking card PHI.

**Product sketch:** Appointment card with notes.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Postgres DELETE is not warehouse DELETE. Next.js does not erase S3 analytics.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/5.1/5.1-lab` stays the only running system you may break.
