# 3.2 — Threat modeling (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Modeler, scanner, reviewer |
| Objects | Threat list, scan status, DFD |
| Actions | threats_from_scan, review |
| Channels | CI, threat-model markdown in git |
| TCB | Versioned model with owners and triggers. |
| Untrusted | Scanner empty-result, “no High findings” |
| State / time | Model stale after a new share path (spiral). |
| 1.1 cell | Integrity of the *assurance story* — missing threats are untested 1.1 cells. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| modeler | cross-tenant-read | must-list | allow-item |
| scanner | empty | replace-model | deny |
| reviewer | stale model | merge | deny |
| CI | mandatory ids | gate | allow |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/3.2/3.2-lab` file `model.py`.

## Transfer

Add webhooks (7.3): which new threats?

## Residual risk

Unknown unknowns — review triggers exist for that.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
