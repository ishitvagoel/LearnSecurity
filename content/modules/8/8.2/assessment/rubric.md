# 8.2 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Local data, keys, biometrics, offline state, and leakage surfaces

## Evidence checklist

- [ ] Device store inventory (cache, backup, screenshot, notification, clipboard)
- [ ] Transfer task (clinic offline chart; Keystore/Keychain/Electron named)
- [ ] Lab `labs/8.2/8.2-lab`: what must not happen: **note body cached as plaintext**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `logout_wipes_cache`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “private dir/fingerprint” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner/MASVS-L1 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **8.2**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/8.2.md`.
