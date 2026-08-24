# 4.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

OAuth, OIDC, and delegated authorization

## Evidence checklist

- [ ] Protocol sequence diagrams and malicious-redirect tests
- [ ] Transfer task (Clinic: wrong-aud FHIR token.)
- [ ] Lab `labs/4.5/4.5-lab`: forbidden outcome **JWT with wrong audience accepted as a SecureCollab session**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: jwt_aud_mismatch; client_revoked.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.5.md`.
