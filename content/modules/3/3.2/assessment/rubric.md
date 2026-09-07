# 3.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Threat modeling

## Evidence checklist

- [ ] Versioned threat model with owners and review triggers
- [ ] Transfer task (clinic SMS reminders)
- [ ] Lab `labs/3.2/3.2-lab`: what must not happen: **Green scanner produces an empty the notes app threat model**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: `missing_mandatory_threat`; `model_age_days`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; STRIDE or scanner slogans |
| Competent | System-specific rule; lab mapped; operate present; drafts labeled |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **3.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/3.2.md`.
