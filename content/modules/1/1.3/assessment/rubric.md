# 1.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Trust boundaries and attack surface

## Evidence checklist

- [ ] Trust-boundary diagram and attack-surface inventory
- [ ] Transfer task (Clinic booking: X-Internal-Admin on the public API.)
- [ ] Lab `labs/1.3/1.3-trust-boundaries`: forbidden outcome **Client internal header dumps all tenants' notes**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: Public-edge log: internal-header-seen without worker identity.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **1.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/1.3.md`.
