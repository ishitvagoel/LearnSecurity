# 8.5 — Mobile verification and privacy (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | CI grep crash fixtures; vendor DLP. |
| Signal (no bodies) | crash_body_redacted test. |
| Revoke / recover | Purge vendor; notify if needed. |
| Residual | Vendor as processor — contract + 5.1. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/8.5/8.5-lab`.

## Transfer

Web Sentry (10.5) same cell.

## Usability

In-app “send feedback” must not require attaching a screenshot of PHI to proceed.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
