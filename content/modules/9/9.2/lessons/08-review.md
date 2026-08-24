# 9.2 — Secure code review (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.

## Property (start here)

A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.

## Attacker capabilities and trust assumptions

- **Attacker:** Rushed colleague; supply-chain PR (10.2).
- **Trust:** Local review_ok(src).
Review `labs/9.2/9.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/9.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): LGTM on eval(user)
- Seeded smell (label it yourself): Reviewer only read README
- Seeded smell (label it yourself): Framework-generated SQL ignored
- Seeded smell (label it yourself): No authority question

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Tests mean review is optional
- Formatters catch security
- AI review replaces 9.2

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Terraform, GitHub Actions yaml.

## HITL / WCAG 2.2

Review UI must be keyboard accessible; otherwise people rubber-stamp from a phone.
