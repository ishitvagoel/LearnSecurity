# 7.4 — Queues, workers, events, and service identity (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
user_session only => None exporter.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def exporter(job):
    return job.get('service') if job.get('service')=='worker-sc' else None
```

## Why this restores the cell

Jobs carry (actor type=service, tenant, resource); workers authenticate as service.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Celery inherit request context is a trap.

Service role that is still god-mode (3.3).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Outbox pattern; event schemas.

## Residual risk

Broker ACLs — 10.3.
