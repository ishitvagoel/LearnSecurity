# 5.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Cryptographic properties and safe use

## Evidence checklist

- [ ] Crypto decision table and misuse-focused tests: Base64 rejection, authenticated round-trip, fresh nonce, and tamper rejection
- [ ] Transfer task (Clinic: SSN column labeled encrypted that is Base64)
- [ ] Lab `labs/5.2/5.2-lab`: what must not happen: **protect is reversible as Base64**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without plaintext: known-plaintext Base64 in CI

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; prefix or algorithm name treated as proof |
| Competent | System-specific confidentiality/integrity rule; lab maps to AES-GCM, nonce, tag, and key boundary; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.2**, and explain why a fresh nonce and authentication tag matter. Complete the assessment worksheet on the module page; it stores notes only in this browser.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.2.md`.
