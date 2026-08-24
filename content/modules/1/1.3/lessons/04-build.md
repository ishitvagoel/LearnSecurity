# 1.3-LO-04 — Shrink TCB / split the shared mechanism

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** CISA Secure by Design (final public guidance) — do not make customers set “internal” headers.

## Property (start here)

Export is allowed only when the **server** bound a worker identity, not when a header is present.

## Structural fix

`fixed/surface.py` ignores headers. `worker_bound=True` is a lab stand-in for mTLS/workload identity. Blast radius of a stolen **browser** session no longer includes full export.

## Practice

Say what left the TCB (the header) and what entered it (worker bind).

## Transfer

Search index as shared mechanism: one index for all tenants is a least-common-mechanism failure unless queries are mediated.
