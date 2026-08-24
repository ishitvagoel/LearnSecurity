# 5.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Cryptographic properties and safe use

## Evidence checklist

- [ ] Crypto decision table and misuse tests
- [ ] Transfer task (Clinic: SSN column labeled “encrypted” that is b64.)
- [ ] Lab `labs/5.2/5.2-lab`: forbidden outcome **Stored secret is mere encoding of plaintext**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: known-plaintext-b64 test in CI.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.2.md`.
