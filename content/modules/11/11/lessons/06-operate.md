# 11 — Capstone: SecureCollab integration (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | read_after_revoke. |
| Signal (no bodies) | revoked_share_read_denied. |
| Revoke / recover | Notify A; rotate links. |
| Residual | Honest copies already made — policy + detect. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/11/11-lab`.

## Transfer

Clinic: revoke a guardian.

## Usability

Revoke UX must be completable (1.4) or people will not revoke.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
