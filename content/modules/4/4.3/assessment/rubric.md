# 4.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Sessions, cookies, and tokens

## Evidence checklist

- [ ] Session channel diagram (query deny; cookie/header allow)
- [ ] Transfer task (clinic deep link; magic-link 6.6)
- [ ] Lab `labs/4.3/4.3-lab`: forbidden outcome **Session established from a query-string token**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without the token: `query_token_rejected`

## Rubric

| Result | Meaning |
|---|---|
| Developing | JWT slogans; missing channel; TLS as the log control |
| Competent | System-specific invariant; lab mapped; 2.3 jar vs this URL deny |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **4.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/4.3.md`.
