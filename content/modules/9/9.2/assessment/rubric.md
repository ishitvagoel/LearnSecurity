# 9.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 9 stays **not-attempted**.

## Module

Secure code review

## Evidence checklist

- [ ] Data-flow / authority / interpreter questions; substring labeled as stand-in
- [ ] Transfer task (clinic template; Terraform / Actions named)
- [ ] Lab `labs/9.2/9.2-lab`: forbidden outcome **eval on user input approved in review**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without payloads: `review_block_eval`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “formatter / bot LGTM” slogans |
| Competent | System-specific invariant; lab mapped; stand-in named; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/weaponized-eval language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **9.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/9.2.md`.
