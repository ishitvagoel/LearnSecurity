# 2.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

State, time, concurrency, and distributed failure

## Evidence checklist

- [ ] State machine plus replay tests
- [ ] Transfer task (Clinic: double-book the last slot.)
- [ ] Lab `labs/2.4/2.4-state-time`: forbidden outcome **Retry creates a second share grant**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: share_count vs unique keys; never fail-open if the key store is down.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **2.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/2.4.md`.
