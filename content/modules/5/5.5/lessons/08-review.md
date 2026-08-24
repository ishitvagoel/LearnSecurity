# 5.5 — Database and persistence security (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).

## Property (start here)

fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.

## Attacker capabilities and trust assumptions

- **Attacker:** Member who types a note id with SQL metacharacters; stolen app role (3.3).
- **Trust:** Local query object. Real DB roles in 3.3.
Review `labs/5.5/5.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/5.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): f"SELECT ... '{note_id}'"
- Seeded smell (label it yourself): ORM .filter with raw strings
- Seeded smell (label it yourself): RLS disabled in tests “for speed” and forgotten
- Seeded smell (label it yourself): No is_bound assertion

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- ORM means no injection
- RLS replaces parameterization
- Blacklist of quotes is mediation

## Practice

Write three review notes. Do not open the keys file.

## Transfer

NoSQL operators, GraphQL args (7.1).
