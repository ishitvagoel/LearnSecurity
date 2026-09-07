# 7.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Webhooks, callbacks, and third-party APIs

## Evidence checklist

- [ ] Raw-body MAC protocol; TLS named as a different cell
- [ ] Transfer task (clinic lab-result webhook; signed redirects / 6.5 named)
- [ ] Lab `labs/7.3/7.3-lab`: what must not happen: **unsigned webhook accepted**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies/secrets: `webhook_sig_fail`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “TLS/SDK” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **7.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/7.3.md`.
