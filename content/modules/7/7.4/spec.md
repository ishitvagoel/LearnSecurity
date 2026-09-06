# 7.4 — Queues, workers, events, and service identity

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 7.4
- **slug:** queues-workers-events-and-service-identity
- **title:** Queues, workers, events, and service identity
- **phase / track / difficulty:** 7 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 4.1 leftover sessions; 4.4 grants; 2.4 retries; 3.3 DB roles.
- **routeTags:** complete, web-api
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **worker principal check** plus deny tests so leftover `user_session` is not export identity.
2. Name attacker capabilities (stolen cookie stuffed into a job; inherited request context) and trust assumptions (local `exporter(job)`).
3. Transfer: clinic batch-export worker; outbox; event schemas — without treating “zero trust” as a product.

## Prerequisite concepts

4.1 delete must kill leftover sessions; 4.4 object×tenant; 2.4 retry/redelivery; 3.3 request-time DB role vs migrator; 7.2 field dumps from workers.

## Misconceptions

- Internal queue is trusted input.
- Async means no authz.
- Service account should be superuser “just for jobs.”
- NIST zero trust as a product replaces worker identity tests.

## Concept map

HTTP subject (4.3) → job payload → worker principal (this module) → originating-subject carry-through (8.3.3 residual) → poison/retry (2.4).

## Invariant prompts

- What must remain true if the job dict still contains `user_session: alice`?
- What fails if the worker DB role is the migrator (3.3)?

## Threat-model prompts

- What can go wrong when Celery inherits the request context?
- What residual remains if retries export after the user’s grant was revoked?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/7.4/7.4-lab`. Forbidden: exporting under alice’s session from a worker job.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP ASVS 5.0.0 (final): `v5.0.0-13.2.1` (backend service accounts, Level 2); `v5.0.0-13.2.2` (least privilege between backend components, Level 2); `v5.0.0-8.3.3` originating subject through an intermediary is **Level 3, labeled advanced** (also named in 4.4).
- NIST SP 800-207 Zero Trust Architecture (final, August 2020): **architecture guidance**, not a product and not the lab oracle.

## Review triggers

New queue/outbox; inherited request context; worker secret/role change; retry after revoke.

## Time budget and SecureCollab

Evidence: HTTP vs worker authority trace, adversarial job tests. Feeds Gate 7 / M2 (milestone stays not-attempted).

## Operational considerations

`worker_identity_wrong`; `poison_queue`. Drain after rotating service creds. Broker ACLs in 10.3.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: HTTP-vs-worker-principal mental models; ASVS v5.0.0-13.2.1; L3 8.3.3 labeled advanced |
