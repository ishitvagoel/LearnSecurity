# 10.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 10 and M4 stay **not finished**.

## Module

Deployment and configuration hardening

## Evidence checklist

- [ ] Boot-flag map; NODE_ENV/canary labeled as not the predicate
- [ ] Transfer task (clinic Django `DEBUG=True`; feature flag that disables authz named)
- [ ] Lab `labs/10.4/10.4-lab`: what must not happen: **production process boots with debug enabled**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without secrets: `prod_debug_forbidden`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “NODE_ENV / canary / IaC” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-host/Gate-10 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.4.md`.
