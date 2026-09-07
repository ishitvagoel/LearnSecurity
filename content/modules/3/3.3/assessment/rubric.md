# 3.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Secure architecture patterns

## Evidence checklist

- [ ] ADRs with rejected alternatives (one superuser URL vs runtime `app`)
- [ ] Transfer task (serverless admin string; clinic billing replica)
- [ ] Lab `labs/3.3/3.3-lab`: what must not happen: **App DB role can SELECT another tenant's rows**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: `grant_drift`; connection-user metric

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; microservice slogans |
| Competent | System-specific rule; lab mapped; operate present; drafts/unverified labeled |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **3.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/3.3.md`.
