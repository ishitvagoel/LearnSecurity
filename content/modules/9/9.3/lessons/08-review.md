# 9.3 — Security-focused tests (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.

## Property (start here)

A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

## Attacker capabilities and trust assumptions

- **Attacker:** False confidence.
- **Trust:** Local is_security_test(spec).
Review `labs/9.3/9.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/9.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): assert r.status_code==200 only
- Seeded smell (label it yourself): No cross-tenant test
- Seeded smell (label it yourself): Security suite empty
- Seeded smell (label it yourself): Chaos without authz

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Coverage is security
- Fuzzing finds all authz bugs
- Snapshot tests are isolation tests

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Fuzzing without an oracle.
