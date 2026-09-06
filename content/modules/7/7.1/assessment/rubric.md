# 7.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

API contracts, protocols, and inventory

## Evidence checklist

- [ ] Writable-field matrix; OpenAPI treated as inventory, not the control
- [ ] Transfer task (clinic PATCH `is_staff`; GraphQL/gRPC named)
- [ ] Lab `labs/7.1/7.1-lab`: forbidden outcome **Client PATCH sets `is_admin`**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `unknown_field_rejected`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “we have Swagger” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **7.1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/7.1.md`.
