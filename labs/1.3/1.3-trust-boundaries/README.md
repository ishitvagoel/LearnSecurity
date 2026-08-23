# Lab: 1.3-trust-boundaries

**Module:** `1.3`  
**Authorized scope:** this directory only.  
**Invariant:** A caller who can set HTTP headers (browser, Next.js, hostile client) must not obtain a full-note export by sending `X-SecureCollab-Internal`.  
**Root cause class:** trust / shared mechanism (header treated as worker identity)  
**Non-goals:** live CDNs, real networks, weaponized header lists beyond this one teaching name.

## Reset

Restore `vulnerable/` and `fixed/` from git.

## Vulnerable behavior (local only)

`export_notes` trusts a client header as if it were the TCB worker bind. Both tenants' bodies return. Correlated "second layer" (header check) shares the first layer's unsanitized identifier.

## Structural fix

Ignore client headers for export. Only a **server-side** `worker_bound` flag (stand-in for mTLS / workload identity, not a header) may export. That splits the mechanism.

## Verify

```bash
python3 -m pytest tests/test_boundary.py --impl vulnerable   # fail client-header test
python3 -m pytest tests/test_boundary.py --impl fixed        # pass
```

## Operate

Alert on export calls that still include the internal header (probe). Do not log note bodies.

## Transfer

Put a CDN in front: cache keys that include tenant-unaware URLs become a new shared mechanism (least common mechanism).
