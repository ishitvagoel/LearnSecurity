# 4.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Identity lifecycle

## Evidence checklist

- [ ] Account state machine and leftover-artifact list
- [ ] Transfer task (clinic: departing clinician)
- [ ] Lab `labs/4.1/4.1-lab`: what must not happen: **Deleted user's leftover session still authenticates**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: `session_after_delete`; offboarding checklist in 10.1

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; SSO slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.1.md`.
