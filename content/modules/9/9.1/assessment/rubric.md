# 9.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 9 stays **not-attempted**.

## Module

Verification requirements and traceability

## Evidence checklist

- [ ] Threat → requirement → test → result chain; ASVS L2 vs L3 labeled
- [ ] Transfer task (clinic HIPAA done column; MASVS-STORAGE named)
- [ ] Lab `labs/9.1/9.1-lab`: forbidden outcome **status-only row counted as AUTHZ-1 coverage**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `unmapped_req_blocks_release`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “ASVS imported / green CI” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/Gate-9 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **9.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/9.1.md`.
