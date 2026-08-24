# 7.4 — Queues, workers, events, and service identity (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.

## Property (start here)

A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen cookie posted into a job; a job that forgets to drop the user context.
- **Trust:** Local exporter(ctx).
Review `labs/7.4/7.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/7.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): job['session']=request.cookies
- Seeded smell (label it yourself): Worker uses DATABASE_URL superuser
- Seeded smell (label it yourself): No test user_session rejected
- Seeded smell (label it yourself): Retry duplicates (2.4)

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Internal queue is trusted input
- Async means no authz
- Service account should be superuser “just for jobs”

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Outbox pattern; event schemas.
