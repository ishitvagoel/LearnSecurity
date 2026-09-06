# SecureCollab Phase 1 — request path and cache keys

Design stub for Module 2.2. Not a production CDN runbook.

## Freeze

- Local cache fixture with `cache_put` / `cache_get` for `/notes/n1`.
- No live CDN, no DNS hijacking lab, no public cache poison.

## Hop versus key

TLS 1.3 (RFC 9846) authenticates a hop. After termination, RFC 9110 cache semantics apply. The bound 1.2 tenant must be in the key if a note body is stored at all.

## Hostile headers

`Host`, `X-Tenant`, and `X-Forwarded-*` are not the bound tenant. ASVS `v5.0.0-4.1.3`.

## Residual

CDN config can drop a key dimension. Detect mismatch without logging bodies; purge the prefix; treat escaped bodies as a 1.1 incident.
