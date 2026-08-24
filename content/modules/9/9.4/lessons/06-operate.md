# 9.4 — Automated analysis and tool orchestration (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.

## Property (start here)

A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”

## Attacker capabilities and trust assumptions

- **Attacker:** Alert fatigue; vendor dashboard theater.
- **Trust:** Local ship_ok(findings, map).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | unmapped_high count. |
| Signal (no bodies) | unmapped_high_blocks. |
| Revoke / recover | Map or fix; do not suppress silently. |
| Residual | Blind spots (authz logic) — 9.2/9.3. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/9.4/9.4-lab`.

## Transfer

SCA CVE vs actually called function.

## Usability

Triage UI must be usable; otherwise people mass-suppress.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
