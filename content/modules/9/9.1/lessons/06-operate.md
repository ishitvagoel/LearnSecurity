# 9.1 — Verification requirements and traceability (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.

## Property (start here)

A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.

## Attacker capabilities and trust assumptions

- **Attacker:** Optimistic PM; empty CI.
- **Trust:** Local covered(req, tests).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | CI: every L2 req maps a test id. |
| Signal (no bodies) | unmapped_req_blocks_release. |
| Revoke / recover | Add tests; do not backfill “done.” |
| Residual | Unmapped Level 3 risks. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/9.1/9.1-lab`.

## Transfer

MASVS STORAGE for 8.2.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
