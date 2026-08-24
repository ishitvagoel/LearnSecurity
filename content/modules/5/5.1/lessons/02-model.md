# 5.1 — Data lifecycle and privacy engineering (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.

## Property (start here)

After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.

## Attacker capabilities and trust assumptions

- **Attacker:** Insider with analytics DB; buyer of a “de-identified” export that still has bodies.
- **Trust:** Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | deleted user, analytics role, remaining notes table |
| Objects | body in NOTES, body in ANALYTICS |
| Actions | delete_account, body_retained |
| Channels | product DB, analytics copy, backups (residual) |
| TCB | Delete use-case that enumerates copies. |
| Untrusted | “We don’t use analytics for authz” as a reason to skip delete |
| State / time | Delete T+0; warehouse load T+6h still has yesterday’s extract. |
| 1.1 cell | Privacy + confidentiality of bodies after the legal/product relationship ends. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| user | NOTES body | delete | gone |
| analyst | ANALYTICS body | after-delete | gone |
| backup | body | restore | residual-named |
| user | delete UI | complete | accessible |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/5.1/5.1-lab` file `lifecycle.py`.

## Transfer

CSV export to a partner; clinic-booking card PHI.

## Residual risk

Legal hold copies — named exception with owner (E6).

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
