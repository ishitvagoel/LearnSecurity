# 5.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Database and persistence security

## Evidence checklist

- [ ] Schema / role / constraint map and bound-query tests
- [ ] Transfer task (clinic search box; NoSQL/GraphQL named for 7.1)
- [ ] Lab `labs/5.5/5.5-lab`: what must not happen: **query built by concatenating untrusted strings into SQL**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `sql_error_spike`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.5.md`.
