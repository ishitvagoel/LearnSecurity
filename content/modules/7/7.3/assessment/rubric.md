# 7.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Webhooks, callbacks, and third-party APIs

## Evidence checklist

- [ ] Signed webhook protocol, replay tests, provider-failure runbook
- [ ] Transfer task (Clinic lab-result webhook.)
- [ ] Lab `labs/7.3/7.3-lab`: forbidden outcome **Unsigned webhook body accepted**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: webhook_sig_fail; replay_window.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **7.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/7.3.md`.
