# 10.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

Logging, detection, incident response, recovery, maintenance

## Evidence checklist

- [ ] Detection rules, playbook, tabletop, restore evidence, maintenance policy
- [ ] Transfer task (Clinic: close ticket when SIEM is green.)
- [ ] Lab `labs/10.5/10.5-lab`: forbidden outcome **Incident closed without recovery evidence**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: incident_closed_without_recovery denied.

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.5.md`.
