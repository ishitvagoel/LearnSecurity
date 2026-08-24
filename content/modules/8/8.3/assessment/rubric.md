# 8.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Network, deep links, WebViews, IPC

## Evidence checklist

- [ ] Malicious-link harness and IPC review
- [ ] Transfer task (Clinic: deep link as=doctor.)
- [ ] Lab `labs/8.3/8.3-lab`: forbidden outcome **Deep link as= switches the signed-in user**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: deeplink_identity_ignored.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **8.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/8.3.md`.
