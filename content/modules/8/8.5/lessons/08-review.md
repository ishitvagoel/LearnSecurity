# 8.5 — Mobile verification and privacy (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
Review `labs/8.5/8.5-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/8.5.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): crash_report includes body
- Seeded smell (label it yourself): READ_LOGS leftover
- Seeded smell (label it yourself): Tracker SDK without review
- Seeded smell (label it yourself): MASVS spreadsheet row without test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Store privacy labels are controls
- Debug logs stay on device
- MASTG is a scanner

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Web Sentry (10.5) same cell.

## HITL / WCAG 2.2

In-app “send feedback” must not require attaching a screenshot of PHI to proceed.
