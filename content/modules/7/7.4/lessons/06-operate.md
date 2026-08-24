# 7.4 — Queues, workers, events, and service identity (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | worker_used_user_session metric. |
| Signal (no bodies) | worker_identity_wrong; poison_queue. |
| Revoke / recover | Revoke service creds; drain queue. |
| Residual | Broker ACLs — 10.3. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/7.4/7.4-lab`.

## Transfer

Outbox pattern; event schemas.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
