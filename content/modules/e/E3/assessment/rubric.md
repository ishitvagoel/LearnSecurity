# E3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 7 and M2 stay **not finished**. Elective. This lab is **not** PCI scope.

## Module

Payments, financial, health, and other high-assurance systems

## Evidence checklist

- [ ] Key-as-identity map; Stripe/PCI labeled as not the ledger
- [ ] Transfer task (health append-only; simulated copay named)
- [ ] Lab `labs/E3/e3-lab`: what must not happen: **duplicate capture double-charges**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without PAN: `duplicate_capture_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “Stripe / PCI / SAQ” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-processor/PCI-as-definition language |

Knowledge check (retryable): distinguish property vs mechanism for **E3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/E3.md`.
