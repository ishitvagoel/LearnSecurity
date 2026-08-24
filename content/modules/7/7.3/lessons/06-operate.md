# 7.3 — Webhooks, callbacks, and third-party APIs (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | sig_fail metric. |
| Signal (no bodies) | webhook_sig_fail; replay_window. |
| Revoke / recover | Rotate webhook secret; review accepted events. |
| Residual | Provider compromise — egress + least privilege on what a webhook may do. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/7.3/7.3-lab`.

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
