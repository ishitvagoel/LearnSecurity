# 5.3 — Key and secret lifecycle (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
Review `labs/5.3/5.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/5.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): DEFAULT = 'sk-lab-hardcoded' still accepted
- Seeded smell (label it yourself): Secret in README “for convenience”
- Seeded smell (label it yourself): No rotation test
- Seeded smell (label it yourself): Same key for all tenants

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- gitignore means it was never leaked
- KMS equals rotated
- Passwords and API keys are the same lifecycle

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Envelope encryption DEK vs KEK; compromise runbook.
