# 2.2-LO-01 — TLS is not the cache key

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** RFC 9846 TLS 1.3 (final); HTTP caching semantics (RFCs as pinned). Drafts stay draft.

## Property (start here)

Tenant B must not receive tenant A’s **cached** note body for the same path. Enabling TLS 1.3 (RFC 9846, final) authenticates a hop; it does not name the cache key.

## Attacker capabilities and trust assumptions

- **Attacker:** another tenant on the same origin lab; or a client who can influence `Host` / `X-Forwarded-*` **if the app trusts them**.
- **Trust:** after TLS termination, forwarded headers are **untrusted** unless the proxy is in the TCB and bound.

## Practice

One sentence: who bound the tenant used in the cache key?

## Transfer

CDN in front: origin must still key by tenant, not only URL.
