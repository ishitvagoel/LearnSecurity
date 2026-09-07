# A broken cache must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

HTTPS 200 on a cache hit does not finish this. A path-only cache key still has to fail on the broken files and pass on the repaired ones.

## Picture: a broken cache must fail the check

Asserting HTTPS can still hide that the key remains path-only.

```mermaid
flowchart LR
  V["broken files"] --> F[Must fail: company B get of company A body]
  X["repaired files"] --> P["Must pass: company A hit and company B miss"]
  F --> E[Evidence the key omitted company]
  P --> E2[Evidence the pair is now bound]
```

If both pass, you are not looking at the cross-company get.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | After company A put, company A get returns `tenant-A-note` |
| Wrong input / abuse | After company A put, company B get is not `tenant-A-note` and is `None` |
| When things break | Unknown company does not share the slot |
| Not claimed | Live CDN `Vary`; browser `no-store`; DNS authenticity |

The checks are `test_same_tenant_cache_hit` and `test_other_tenant_does_not_receive_cached_body`. They observe bodies, not HTTP 200. That check is there so a company B get of `tenant-A-note` does not pass as a cache hit.

Map each check to a rule from the request-path map. Do not paste keys. If the broken files do not fail the cross-company get, the practice files are miswired — fix the wiring, not the assertion.

TLS 1.3 on the browser hop is not this check. HTTPS 200 is a hop, not the cache key.

## What the checks do not prove

- Live CDN `Vary` behavior
- Browser `no-store`
- Forwarded-header pinning in FastAPI
- DNS authenticity

Record those as leftover or later work, not as silent passes.

## Practice

```text
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed
```

Call `cache_get` as company B. A `Cache-Control` header is the hop, not the other-tenant miss.

## Use it somewhere new

Authenticated RSS or export CSV via CDN. Asserting status 200 on `/export` is not cache-key evidence. Do not run a check against a live CDN.

## What this page is not doing

Do not add live traffic. Do not log `tenant-A-note`. Answer keys are not on this site.
