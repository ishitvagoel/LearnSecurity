# 5.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Secure communication and channel binding

## Evidence checklist

- [ ] Trust-chain / hop diagram and TLS tests
- [ ] Transfer task (Clinic SPA https vs API http; mTLS vs header)
- [ ] Lab `labs/5.4/5.4-lab`: what must not happen: **client Forwarded-Proto counted as TLS**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without cookies: `header_https_socket_http`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; tool slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.4.md`.
