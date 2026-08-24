# 10.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Source control, CI/CD, and software supply chain

## Evidence checklist

- [ ] Hardened pipeline, SBOM, provenance, simulated compromise exercise
- [ ] Transfer task (Clinic: npm install in prod pod.)
- [ ] Lab `labs/10.2/10.2-lab`: forbidden outcome **Dependency installed when digest mismatches lockfile**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: hash_mismatch_denied.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.2.md`.
