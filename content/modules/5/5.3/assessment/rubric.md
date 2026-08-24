# 5.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Key and secret lifecycle

## Evidence checklist

- [ ] Key hierarchy, inventory, rotation exercise, compromise runbook
- [ ] Transfer task (Clinic lab API key in a GitHub gist.)
- [ ] Lab `labs/5.3/5.3-lab`: forbidden outcome **Hardcoded default API key still authenticates after rotation**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: auth_default_denied; image_rebuild after rotate.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.3.md`.
