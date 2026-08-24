# 6.4 — Files, paths, uploads, archives, XML, deserialization (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.

## Property (start here)

A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.

## Attacker capabilities and trust assumptions

- **Attacker:** Uploader or filename field attacker.
- **Trust:** Local resolve() under /tmp/sc-lab.
Review `labs/6.4/6.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/6.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): open(user_path)
- Seeded smell (label it yourself): Blacklist of '..' only
- Seeded smell (label it yourself): Trust Content-Type
- Seeded smell (label it yourself): No prefix test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- UUID filenames replace path checks
- Antivirus is the upload control
- JSON is always safe deserialize

## Practice

Write three review notes. Do not open the keys file.

## Transfer

XML entity expansion; pickle; YAML load.
