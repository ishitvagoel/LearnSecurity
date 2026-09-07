# 6.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Cross-site and cross-context attacks

## Evidence checklist

- [ ] Origin × token matrix and share-POST tests
- [ ] Transfer task (clinic share-with-partner POST; postMessage/clickjacking/CORS named)
- [ ] Lab `labs/6.3/6.3-lab`: what must not happen: **cross-origin state-changing POST authorized by cookie alone**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without cookies: `foreign_origin_post_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **6.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/6.3.md`.
