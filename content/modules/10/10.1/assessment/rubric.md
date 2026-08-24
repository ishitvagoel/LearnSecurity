# 10.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Secure software lifecycle and security culture

## Evidence checklist

- [ ] Lightweight SSDLC, change-trigger matrix, improvement plan
- [ ] Transfer task (Clinic: “HIPAA training complete” as merge.)
- [ ] Lab `labs/10.1/10.1-lab`: forbidden outcome **Merge without a threat-model identifier**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: merge_without_tm denied.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.1.md`.
