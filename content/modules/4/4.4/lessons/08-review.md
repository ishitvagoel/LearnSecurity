# 4.4 — Authorization and tenant isolation (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.

## Property (start here)

A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.

## Attacker capabilities and trust assumptions

- **Attacker:** Member with a grant on n1 who swaps note_id; IDOR enumerator.
- **Trust:** Local grants dict. SQL still needs 5.5.
Review `labs/4.4/4.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/4.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): if user.has_any_share: return note
- Seeded smell (label it yourself): Missing n2 deny test
- Seeded smell (label it yourself): Admin boolean bypass without tenant
- Seeded smell (label it yourself): Search endpoint without mediation

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- IDOR is a scanner finding not a missing cell
- RBAC role replaces object grants
- Signed ids are capabilities

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Property-level: bob can read title but not body (7.2).
