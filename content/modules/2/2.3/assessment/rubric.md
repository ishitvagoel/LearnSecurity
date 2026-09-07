# 2.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Browser security model

## Evidence checklist

- [ ] Browser policy matrix and cookie tests
- [ ] Transfer task (Clinic patient portal session cookie.)
- [ ] Lab `labs/2.3/2.3-browser-policy`: what must not happen: **Script reads the HttpOnly session cookie**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: Set-Cookie without HttpOnly in staging scans.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **2.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/2.3.md`.
