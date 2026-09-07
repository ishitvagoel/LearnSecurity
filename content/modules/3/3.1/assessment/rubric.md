# 3.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Assets, classification, and security requirements

## Evidence checklist

- [ ] Data inventory, classification, requirements backlog
- [ ] Transfer task (EHR-lite booking card.)
- [ ] Lab `labs/3.1/3.1-lab`: what must not happen: **Confidential note body appears in a log line**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: log_redaction_miss alerts; purge runbook.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **3.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/3.1.md`.
