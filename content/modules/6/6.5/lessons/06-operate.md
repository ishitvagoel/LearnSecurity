# 6.5 — Server-side requests and protocol parsing (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | egress deny logs. |
| Signal (no bodies) | egress_denied{host}. |
| Revoke / recover | Rotate instance role if a real system was hit — never in this course. |
| Residual | Legitimate preview of customer URLs — dedicated egress proxy. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/6.5/6.5-lab`.

## Transfer

Webhook delivery (7.3) is egress too.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
