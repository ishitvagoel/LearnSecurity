# 7.3 — Webhooks, callbacks, and third-party APIs (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | forged client, real provider, app |
| Objects | body, HMAC, secret |
| Actions | accept |
| Channels | HTTPS callback |
| TCB | Verify signature over raw body + freshness + idempotency (2.4). |
| Untrusted | IP allow-lists as the only control; JSON fields |
| State / time | Replay yesterday’s valid signed body (residual if no nonce). |
| 1.1 cell | Authenticity + integrity of inbound integration. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| forger | empty sig | POST | deny |
| provider | valid sig | POST | allow-verify |
| replay | old valid | POST | deny-if-freshness |
| handler | event | side-effect | still-1.2 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/7.3/7.3-lab` file `hook.py`.

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

## Residual risk

Provider compromise — egress + least privilege on what a webhook may do.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
