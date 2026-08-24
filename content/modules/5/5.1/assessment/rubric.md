# 5.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Data lifecycle and privacy engineering

## Evidence checklist

- [ ] Data-flow inventory, retention/deletion matrix, privacy review
- [ ] Transfer task (Appointment card with notes.)
- [ ] Lab `labs/5.1/5.1-lab`: forbidden outcome **Analytics copy still holds note body after account deletion**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: deleted_user_body_hits; warehouse SLA for purge.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.1.md`.
