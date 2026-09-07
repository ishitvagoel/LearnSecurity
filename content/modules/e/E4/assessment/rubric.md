# E4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 7 and M2 stay **not finished**. Elective. This lab is **not** a native exploit course.

## Module

Memory safety and native-code boundaries

## Evidence checklist

- [ ] Length-as-mediation map; language/CISA/CWE labeled as not the copy check
- [ ] Transfer task (clinic DICOM; protobuf C named)
- [ ] Lab `labs/E4/e4-lab`: what must not happen: **copy exceeds destination**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without payload bytes: `copy_length_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “Kotlin / CWE / ASAN” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 25/native-PoC/language-as-definition language |

Knowledge check (retryable): distinguish property vs mechanism for **E4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/E4.md`.
