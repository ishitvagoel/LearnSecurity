# 6.1 — Interpreter confusion and injection (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.

## Property (start here)

A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.

## Attacker capabilities and trust assumptions

- **Attacker:** User who chooses a note/export name; a compromised client.
- **Trust:** Local argv.py. No live OS attack — the test only checks argv shape.
Review `labs/6.1/6.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): shell=True or sh -c concatenation
- Seeded smell (label it yourself): Blacklist of ; as the fix
- Seeded smell (label it yourself): No uses_shell test
- Seeded smell (label it yourself): Comment “user is trusted internally”

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Injection is one CWE
- ORM/subprocess wrappers auto-escape shells
- Scanner finding is the invariant

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Jinja, SQL, mail headers.
