# 7.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Queues, workers, events, and service identity

## Evidence checklist

- [ ] HTTP vs worker principal trace; leftover session is not identity
- [ ] Transfer task (clinic batch-export; outbox/events named)
- [ ] Lab `labs/7.4/7.4-lab`: what must not happen: **user session accepted as worker identity**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without cookies: `worker_identity_wrong`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “internal/zero-trust” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **7.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/7.4.md`.
