# 9.4 — Automated analysis and tool orchestration (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
Review `labs/9.4/9.4-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/9.4.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): ship_ok True on unmapped HIGH
- Seeded smell (label it yourself): Suppressions without owner
- Seeded smell (label it yourself): SAST as Gate 9
- Seeded smell (label it yourself): No blind-spot note for IDOR

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Zero findings means secure
- Tool X replaces ASVS
- Reachability is optional theater

## Practice

Write three review notes. Do not open the keys file.

## Transfer

SCA CVE vs actually called function.

## HITL / WCAG 2.2

Triage UI must be usable; otherwise people mass-suppress.
