# 7.4 — Queues, workers, events, and service identity (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | User session accepted as worker identity |
| Failure | Fail closed: Jobs carry (actor type=service, tenant, resource); workers authenticate as service |

Lab tests: `test_property.py` under `labs/7.4/7.4-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `User session accepted as worker identity`
- `--impl fixed`: **pass**

user_session is not worker identity.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Outbox pattern; event schemas.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
