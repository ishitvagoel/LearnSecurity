# Lab: 2.2-request-path

**Module:** `2.2`  
**Authorized scope:** this directory only.  
**Invariant:** Tenant B must not be served tenant A’s cached note body for the same URL. “HTTPS on” (RFC 9846 TLS 1.3, final) is not the cache-key property.  
**Root cause class:** trust / shared mechanism (URL-only cache key after TLS termination)  
**Non-goals:** live CDNs, poisoning a public cache, DNS hijacking labs.

## Reset

Restore trees from git. Call `reset()` between mental experiments; tests call it.

## Vulnerable behavior (local only)

`cache_put` keys only on path. Bob’s `cache_get("/notes/n1", "tB")` returns alice’s body. `X-Forwarded-Host` is not even needed — the key never included tenant.

## Structural fix

Key `(path, tenant)` where tenant is the **bound** application identity (1.2), not a client `Host` header.

## Verify

```bash
python3 -m pytest tests/test_cache_key.py --impl vulnerable
python3 -m pytest tests/test_cache_key.py --impl fixed
```

## Operate

Log cache hits with tenant, not bodies. CDN `Vary` is a later origin policy, not a product slogan.

## Transfer

Add a reverse proxy that sets `X-Forwarded-Proto`. The app still must not treat that header as the TLS property.
