# E6 — Product security leadership (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.

## Property (start here)

A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.

## Attacker capabilities and trust assumptions

- **Attacker:** Calendar; silent exceptions.
- **Trust:** Local accept_exception({owner, review_by}).
Review `labs/E6/e6-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E6.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): accept with empty owner
- Seeded smell (label it yourself): No review_by
- Seeded smell (label it yourself): a11y not in the schema
- Seeded smell (label it yourself): SAMM slide as the exception

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Leadership is soft skills not invariants
- Exceptions are failure
- Users can always call support instead of accessible recovery

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Procurement questionnaire vs this record.

## HITL / WCAG 2.2

The exception must record whether the residual includes an inaccessible control (1.4). Leadership owns that users cannot complete recovery.
