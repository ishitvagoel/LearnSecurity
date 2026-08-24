# 7.4 — Queues, workers, events, and service identity (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
**Mechanism (not the property):** Celery inherit request context is a trap.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 7.4 |
|---|---|
| Root cause | Ambient user context in a system worker. |
| Preconditions | exporter({user_session: alice}) succeeds. |
| Impact (1.1 cell) | Authorization of the worker plane. — User cookie drives a privileged export; or stale user still exports. |
| Prevention | Jobs carry (actor type=service, tenant, resource); workers authenticate as service. |
| Detection | worker_used_user_session metric. |
| Recovery | Revoke service creds; drain queue. |

## Framework defaults vs application guarantees

Celery inherit request context is a trap.

## Mechanism limits and bypasses

Service role that is still god-mode (3.3).

Poison message loops; cross-tenant job fields.

## Residual risk

Broker ACLs — 10.3.

## Practice

Trace one export: who is the subject at HTTP vs worker.

Run `labs/7.4/7.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Outbox pattern; event schemas.

Clinic batch-export worker.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
