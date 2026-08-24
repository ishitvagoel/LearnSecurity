# 11 — Capstone: SecureCollab integration (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | A owner, B member after revoke |
| Objects | n1 share |
| Actions | revoke, read |
| Channels | API, cache (2.2), mobile (8.2) |
| TCB | Grant table as source of truth on every read. |
| Untrusted | CDN cache of n1, offline cache, email copy |
| State / time | Revoke then read. |
| 1.1 cell | Authorization over time — the course thesis in one fixture. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| B | n1 before revoke | read | allow-if-granted |
| B | n1 after revoke | read | deny |
| cache | n1 | serve B | deny |
| worker | old job | export B | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/11/11-lab` file `capstone.py`.

## Transfer

Clinic: revoke a guardian.

## Residual risk

Honest copies already made — policy + detect.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
