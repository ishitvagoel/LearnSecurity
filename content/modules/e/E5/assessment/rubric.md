# E5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 7 and M2 stay **not finished**. Elective.

## Module

Large-scale authorization and multi-tenant SaaS

## Evidence checklist

- [ ] Session-binding map; RLS/body/API1 labeled as not 1.2
- [ ] Transfer task (clinic `org_id`; Zanzibar named)
- [ ] Lab `labs/E5/e5-lab`: what must not happen: **JSON body switches the bound tenant**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies: `body_tenant_mismatch`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “RLS / Zanzibar / API1” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-tenant/Gate-7 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **E5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/E5.md`.
