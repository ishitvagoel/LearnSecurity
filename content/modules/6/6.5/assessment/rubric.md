# 6.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Server-side requests and protocol parsing

## Evidence checklist

- [ ] Egress allow-list and URL predicate tests (no live fetches)
- [ ] Transfer task (clinic PDF URL; webhooks named)
- [ ] Lab `labs/6.5/6.5-lab`: what must not happen: **server-side fetch to link-local metadata is allowed**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without full URLs: `egress_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **6.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/6.5.md`.
