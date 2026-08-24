# 10.1 — Secure software lifecycle and security culture (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.

## Property (start here)

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

## Attacker capabilities and trust assumptions

- **Attacker:** Schedule pressure.
- **Trust:** Local merge_ok({}).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | merge_blocked_no_tm. |
| Signal (no bodies) | merge_without_tm denied. |
| Revoke / recover | Open TM, then merge. |
| Residual | Metrics vanity — count TMs with tests, not posters. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/10.1/10.1-lab`.

## Transfer

Exception path (E6).

## Usability

Merge and checklist UIs must be accessible to the actual reviewers you have.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
