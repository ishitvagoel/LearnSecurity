# 6.7 — Resource abuse, automation, and availability (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).

## Property (start here)

The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).

## Attacker capabilities and trust assumptions

- **Attacker:** Scripted member; compromised session.
- **Trust:** Local allow(n).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | export_denied_quota. |
| Signal (no bodies) | quota_denied; cost_alert. |
| Revoke / recover | Disable token; bill anomaly. |
| Residual | Legitimate burst — owned exception. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.7/6.7-lab`.

## Transfer

Notification fan-out; search complexity.

## Usability

Quota errors must be readable; do not trap keyboard users in a spinner that retries (amplifying load).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
