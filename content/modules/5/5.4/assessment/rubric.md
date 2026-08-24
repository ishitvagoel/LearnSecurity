# 5.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Secure communication and channel binding

## Evidence checklist

- [ ] Trust-chain diagram, TLS tests, certificate failure drill
- [ ] Transfer task (Clinic: “we’re on TLS” because the SPA uses https:// in axios baseURL while API is http internally logged as https.)
- [ ] Lab `labs/5.4/5.4-lab`: forbidden outcome **Client X-Forwarded-Proto treated as TLS**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: proto_mismatch; cert expiry drill (ops 10.4).

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **5.4**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/5.4.md`.
