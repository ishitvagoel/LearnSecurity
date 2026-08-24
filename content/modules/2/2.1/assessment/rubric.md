# 2.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Bytes, encodings, parsers, and interpreter boundaries

## Evidence checklist

- [ ] Parser-boundary map and ambiguity tests
- [ ] Transfer task (Clinic booking: duplicate patient_id keys.)
- [ ] Lab `labs/2.1/2.1-parser-boundaries`: forbidden outcome **Parser differential: ACL tenant disagrees with stored tenant**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: ingest_reject_duplicate_key count; never log raw ambiguous bodies.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **2.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/2.1.md`.
