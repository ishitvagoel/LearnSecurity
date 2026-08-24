# 9.5 — Authorized assessment, reporting, and remediation (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.

## Property (start here)

A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.

## Attacker capabilities and trust assumptions

- **Attacker:** Paper-compliance; ignored variant classes.
- **Trust:** Local close_finding({retest}).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | closed_without_retest metric. |
| Signal (no bodies) | finding_closed_without_retest denied. |
| Revoke / recover | Reopen. |
| Residual | Unknown variants — hunt (same root cause). |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/9.5/9.5-lab`.

## Transfer

KEV vs internal-only.

## Usability

Reports used by engineers must be readable (structure, not color-only severity).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
