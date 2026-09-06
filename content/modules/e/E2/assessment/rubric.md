# E2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 7 and M2 stay **not-attempted**. Elective.

## Module

Advanced browser and edge security

## Evidence checklist

- [ ] Enforce vs Report-Only map; encoding labeled as not CSP
- [ ] Transfer task (clinic HIPAA header; Trusted Types / COOP named)
- [ ] Lab `labs/E2/e2-lab`: forbidden outcome **Report-Only treated as isolation enforcement**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without HTML: `csp_report_only_not_enforced`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “Helmet / CSP / dashboard” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-XSS/Gate-7 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **E2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/E2.md`.
