# 10.5 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 10 and M4 stay **not finished**.

## Module

Logging, detection, incident response, recovery, and maintenance

## Evidence checklist

- [ ] Close-predicate map; SIEM/PagerDuty/KEV labeled as not recover
- [ ] Transfer task (clinic SIEM-green close; ransomware restore vs note integrity named)
- [ ] Lab `labs/10.5/10.5-lab`: what must not happen: **incident closed without recovery evidence** and **note body in logs**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without bodies: `incident_closed_without_recovery`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “SIEM / MTTD / backups” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-IR/Gate-10 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.5**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.5.md`.
