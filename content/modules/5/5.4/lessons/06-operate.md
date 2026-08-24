# 5.4 — Secure communication and channel binding (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Requests where header https and socket http. |
| Signal (no bodies) | proto_mismatch; cert expiry drill (ops 10.4). |
| Revoke / recover | HSTS once you really have TLS; revoke cookies issued over cleartext. |
| Residual | Pinning mobile apps (8.x) vs operational breakage — document, don’t mandate. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/5.4/5.4-lab`.

## Transfer

mTLS service identity vs this header.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
