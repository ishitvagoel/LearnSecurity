# 6.2 — Browser injection and active content (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | CSP reports (not enforcement by themselves — E2). |
| Signal (no bodies) | csp_report; stored_field_review. |
| Revoke / recover | Patch content; rotate sessions if cookie not HttpOnly. |
| Residual | Trusted admin HTML — explicit tiny exception. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.2/6.2-lab`.

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
