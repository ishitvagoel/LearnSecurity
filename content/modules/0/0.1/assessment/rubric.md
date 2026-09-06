# 0.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 0 stays **not-attempted** until Phase 0 evidence exists.

## Module

Security engineering orientation

## Evidence checklist

- [ ] Scope map; WSTG/Burp/NICE labeled as not authorization
- [ ] Transfer task (contractor WordPress; company staging named) — do not hit those hosts
- [ ] Lab `labs/0.1/0.1-orientation`: forbidden outcome **public host treated as authorized**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without response bodies: `out_of_scope`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “WSTG / Burp / login page” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-target/Gate-0 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **0.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/0.1.md`.
