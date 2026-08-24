# 6.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Server-side requests and protocol parsing

## Evidence checklist

- [ ] Egress policy, URL validation, origin-consistency tests
- [ ] Transfer task (Clinic “fetch lab result PDF from URL.”)
- [ ] Lab `labs/6.5/6.5-lab`: forbidden outcome **Server-side fetch to link-local metadata is allowed**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: egress_denied{host}.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **6.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/6.5.md`.
