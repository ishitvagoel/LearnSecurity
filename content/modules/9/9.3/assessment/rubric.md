# 9.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 9 stays **not finished**.

## Module

Security-focused tests

## Evidence checklist

- [ ] Forbidden-outcome vs happy-path map; ASVS/WSTG/MASTG labeled as catalogues
- [ ] Transfer task (clinic `test_get_patient_200`; fuzzing without oracle named)
- [ ] Lab `labs/9.3/9.3-lab`: what must not happen: **HTTP 200-only test counted as a security test**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `security_suite_missing_isolation`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “coverage / WSTG tick” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/Gate-9 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **9.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/9.3.md`.
