# 8.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Network, deep links, WebViews, and inter-app communication

## Evidence checklist

- [ ] Exported-component / query-key inventory
- [ ] Transfer task (clinic `as=doctor`; OAuth redirect named)
- [ ] Lab `labs/8.3/8.3-lab`: forbidden outcome **`as=` switches the signed-in user**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without URLs/tokens: `deeplink_identity_ignored`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “App Links/https” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/MASVS-L1 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **8.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/8.3.md`.
