# E2 — Advanced browser and edge security (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | csp_mode metric. |
| Signal (no bodies) | csp_reportonly_not_enforced. |
| Revoke / recover | Flip to enforcing after fix 6.2. |
| Residual | XS-Leaks — named as elective depth. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E2/e2-lab`.

## Transfer

Trusted Types, COOP/COEP.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
