# 4.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

OAuth, OpenID Connect, browser apps, and native apps

## Evidence checklist

- [ ] Protocol sequence diagrams and malicious-redirect / audience tests
- [ ] Transfer task (Clinic: wrong-aud FHIR token; RFC 8252 native redirect)
- [ ] Lab `labs/4.5/4.5-lab`: what must not happen: **JWT with wrong audience accepted as a notes-app session**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without tokens / note bodies: `jwt_aud_mismatch`; `client_revoked`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.5.md`.
