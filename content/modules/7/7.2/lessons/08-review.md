# 7.2 — Object, property, and function security (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.

## Property (start here)

A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.

## Attacker capabilities and trust assumptions

- **Attacker:** Member using GraphQL __typename or REST ?fields=.
- **Trust:** Local resolve(role, field).
Review `labs/7.2/7.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/7.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): return orm.__dict__
- Seeded smell (label it yourself): GraphQL expose all columns
- Seeded smell (label it yourself): IDOR test only on object not field
- Seeded smell (label it yourself): UUID as “capability”

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Object-level authz implies field-level
- Private JSON keys are hidden
- GraphQL resolvers inherit REST policy magically

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Bulk update; search highlighting leaking snippets.
