# 5.4 — Secure communication and channel binding (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | client, app, maybe LB |
| Objects | X-Forwarded-Proto, socket proto |
| Actions | channel_is_https |
| Channels | HTTP headers vs TLS |
| TCB | Socket or a *configured* trusted proxy hop. |
| Untrusted | Any client header about TLS |
| State / time | Mixed content, stray http:// bookmark. |
| 1.1 cell | Authenticity of the transport. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| client | X-Forwarded-Proto | assert TLS | deny |
| socket TLS | channel | https | allow |
| trusted LB | proto header | assert | allow-if-bound-peer |
| mobile | pin | fail-closed | trade-off |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/5.4/5.4-lab` file `channel.py`.

## Transfer

mTLS service identity vs this header.

## Residual risk

Pinning mobile apps (8.x) vs operational breakage — document, don’t mandate.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
