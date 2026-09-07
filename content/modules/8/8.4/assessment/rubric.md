# 8.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Build, distribution, attestation, and resilience

## Evidence checklist

- [ ] Debug vs release channel map; resilience labeled as cost
- [ ] Transfer task (clinic debug vs FHIR; SBOM named)
- [ ] Lab `labs/8.4/8.4-lab`: what must not happen: **debug build allowed to call production export**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without binaries: `debug_to_prod_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “R8/Play Signing” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/MASVS-L1 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **8.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/8.4.md`.
