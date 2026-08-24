# 6.6 — Workflow, race, and exceptional-condition failures (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.

## Property (start here)

An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.

## Attacker capabilities and trust assumptions

- **Attacker:** Two tabs; an attacker who copied the token from email logs.
- **Trust:** Local accept().
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | token_replay metric. |
| Signal (no bodies) | invite_replay_denied. |
| Revoke / recover | Remove extra membership; rotate token scheme. |
| Residual | Email is a phishable channel (4.2). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.6/6.6-lab`.

## Transfer

Password reset; 2.4 share retry; 7.4 jobs.

## Usability

Invite errors (“link already used”) must be announced accessibly so people do not retry into a support backdoor.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
