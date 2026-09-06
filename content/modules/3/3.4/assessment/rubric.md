# 3.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Business logic and abuse-resistant design

## Evidence checklist

- [ ] Misuse cases, workflow state machine, abuse plan
- [ ] Transfer task (clinic: max 3 guardians per child)
- [ ] Lab `labs/3.4/3.4-lab`: forbidden outcome **Share grants exceed the product cap of 5**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: `share_cap_denied`; trim extras

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; HTML-max or WAF slogans |
| Competent | System-specific invariant; lab mapped; operate present; API4/API6 labeled awareness |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **3.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/3.4.md`.
