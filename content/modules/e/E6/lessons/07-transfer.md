# E6 — Product security leadership (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Procurement questionnaire vs this record.

**Product sketch:** Clinic: “HIPAA exception.”

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | Jira “risk” issue type without dates.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/E6/e6-lab` stays the only running system you may break.
