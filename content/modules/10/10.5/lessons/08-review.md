# 10.5 — Logging, detection, incident response, recovery, maintenance (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.

## Property (start here)

An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Real incident; optimistic closer.
- **Trust:** Local close_incident({recovery, logs}).
Review `labs/10.5/10.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/10.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): close with recovery todo
- Seeded smell (label it yourself): Note bodies in logs
- Seeded smell (label it yourself): No restore evidence
- Seeded smell (label it yourself): Support tool is god-mode (3.3)

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- MTTD is the goal
- Backups untested are recovery
- Disclosure is legal-only

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Ransomware restore vs note-level integrity.

## HITL / WCAG 2.2

IR runbooks and status pages must be usable under stress (keyboard, language, not color-only severity).
