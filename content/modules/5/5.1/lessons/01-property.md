# 5.1 — Data lifecycle and privacy engineering (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
**Mechanism (not the property):** Postgres DELETE is not warehouse DELETE. Next.js does not erase S3 analytics.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 5.1 |
|---|---|
| Root cause | Secondary copy not in the deletion graph. |
| Preconditions | delete_account pops NOTES only. |
| Impact (1.1 cell) | Privacy + confidentiality of bodies after the legal/product relationship ends. — Bodies persist after the person left. |
| Prevention | Inventory copies; delete or unlink bodies in each. |
| Detection | Job that searches analytics for deleted user ids (careful with logs). |
| Recovery | Purge warehouse partitions; notify if required by policy (not fake GDPR theater). |

## Framework defaults vs application guarantees

Postgres DELETE is not warehouse DELETE. Next.js does not erase S3 analytics.

## Mechanism limits and bypasses

Anonymize ids but keep bodies — still a body retention fail.

Backups, search indexes, mobile cache (8.2), support tickets with paste.

## Residual risk

Legal hold copies — named exception with owner (E6).

## Practice

Draw collection → use → share → retain → delete for the body.

Run `labs/5.1/5.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

CSV export to a partner; clinic-booking card PHI.

Appointment card with notes.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Delete-account journey must be completable with keyboard and clear status (WCAG 3.3.x). An unreachable delete is a privacy incident (1.4).
