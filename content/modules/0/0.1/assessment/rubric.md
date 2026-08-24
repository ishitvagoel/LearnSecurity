# 0.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Security engineering orientation

## Evidence checklist

- [ ] Personal lab rules, scope template, vocabulary map
- [ ] Transfer task (A contractor asked to “quickly test our customer’s WordPress.”)
- [ ] Lab `labs/0.1/0.1-orientation`: forbidden outcome **HTTP to a non-allowlisted host treated as authorized**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: Denied-host log line {url, reason=out_of_scope}; never store response bodies from out-of-scope hosts.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **0.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/0.1.md`.
