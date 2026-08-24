# 11 — Capstone: SecureCollab integration (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.

## Property (start here)

After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.

## Attacker capabilities and trust assumptions

- **Attacker:** Former collaborator with a cached id; delayed worker (7.4).
- **Trust:** Local share map.
Review `labs/11/11-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/11.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): read after revoke succeeds
- Seeded smell (label it yourself): Capstone README: scanner green = done
- Seeded smell (label it yourself): No cache invalidation
- Seeded smell (label it yourself): Gate 11 claimed without artifacts

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Capstone is a new product
- Milestones M0–M5 complete because lessons exist
- Integration tests replace the 13 artifacts

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Clinic: revoke a guardian.

## HITL / WCAG 2.2

Revoke UX must be completable (1.4) or people will not revoke.
