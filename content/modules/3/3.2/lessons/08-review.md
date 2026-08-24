# 3.2 — Threat modeling (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.

## Property (start here)

A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.

## Attacker capabilities and trust assumptions

- **Attacker:** Cross-tenant member; hostile browser; future worker identity (named now as a trigger).
- **Trust:** Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.
Review `labs/3.2/3.2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/3.2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): threats = [] if scan_green
- Seeded smell (label it yourself): No cross-tenant-read item
- Seeded smell (label it yourself): Model not in git
- Seeded smell (label it yourself): STRIDE letters without assets

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Green scan means no threats
- Threat models are pre-code only
- Awareness lists are the threat list

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Add webhooks (7.3): which new threats?
