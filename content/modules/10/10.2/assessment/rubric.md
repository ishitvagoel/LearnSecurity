# 10.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 10 and M4 stay **not-attempted**.

## Module

Source control, CI/CD, dependencies, and software supply chain

## Evidence checklist

- [ ] Name vs digest map; SBOM/SLSA labeled as inventory/provenance
- [ ] Transfer task (clinic npm in prod; `action@v1` named)
- [ ] Lab `labs/10.2/10.2-lab`: forbidden outcome **dependency installed when digest mismatches lockfile**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without secrets: `hash_mismatch_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “SBOM / Dependabot / SLSA” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-registry/Gate-10 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.2.md`.
