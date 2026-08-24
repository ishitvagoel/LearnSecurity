# 4.1 — Identity lifecycle (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.

## Property (start here)

After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.

## Attacker capabilities and trust assumptions

- **Attacker:** Stolen session cookie after the user left the org; a delayed worker using the old user id.
- **Trust:** Local user+session maps. Real IdP SLO is extra (4.5).
Review `labs/4.1/4.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/4.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): DELETE FROM users without session purge
- Seeded smell (label it yourself): JWT exp 30d ignored on delete
- Seeded smell (label it yourself): Worker still has user_id
- Seeded smell (label it yourself): No test session_valid after delete

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Disable login is enough
- SSO magically revokes
- Deleted means gone from backups

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Contractor access end-date; support impersonation tickets.

## HITL / WCAG 2.2

Offboarding confirmation must be accessible (1.4). A mouse-only “delete user” is a missed revoke.
