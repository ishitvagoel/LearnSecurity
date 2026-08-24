# 4.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Authentication and phishing-resistant authenticators

## Evidence checklist

- [ ] Authenticator decision record and accessible-flow review
- [ ] Transfer task (Clinic staff SSO portal.)
- [ ] Lab `labs/4.2/4.2-lab`: forbidden outcome **Password (or wrong-origin WebAuthn) counted as phishing-resistant**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: webauthn_fail_origin; recovery_used (higher risk).

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.2.md`.
