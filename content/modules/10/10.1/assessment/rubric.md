# 10.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 10 and M4 stay **not-attempted**.

## Module

Secure software lifecycle and security culture

## Evidence checklist

- [ ] Change-trigger matrix; CODEOWNERS labeled as not TM
- [ ] Transfer task (clinic HIPAA training; E6 named)
- [ ] Lab `labs/10.1/10.1-lab`: forbidden outcome **merge without a threat-model identifier**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `merge_blocked_no_tm`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “CODEOWNERS / poster” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/SAMM-as-gate/Gate-10 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.1.md`.
