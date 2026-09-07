# 4.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Authentication, phishing resistance, and usable access

## Evidence checklist

- [ ] Authenticator decision record (method × origin × resistant?)
- [ ] Accessible-flow review (WCAG 2.2 on the ceremony)
- [ ] Transfer task (clinic staff SSO; step-up export)
- [ ] Lab `labs/4.2/4.2-lab`: what must not happen: **Password (or wrong-origin WebAuthn) counted as phishing-resistant**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without secrets: `webauthn_fail_origin`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; “MFA” slogans; missing origin |
| Competent | System-specific rule; lab mapped; CR labeled; residual named |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.2.md`.
