# 7.4 — Queues, workers, events, and service identity (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
**Forbidden outcome:** User session accepted as worker identity

**Authorized scope:** `labs/7.4/7.4-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable worker.py treats user session as worker.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: exporter({user_session: alice}) succeeds.

## Vulnerable fixture (local)

```python
def exporter(job):
    return job.get('user_session') or job.get('service')
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Ambient user context in a system worker. |
| Impact | User cookie drives a privileged export; or stale user still exports. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/7.4/7.4-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Outbox pattern; event schemas.

## Non-goals

No live-target instructions. Synthetic data only.
