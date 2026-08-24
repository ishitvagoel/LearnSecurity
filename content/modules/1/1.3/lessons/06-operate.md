# 1.3-LO-06 — Detect unexpected caller or egress

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 (final) Detect/Respond — outcomes, not a SIEM product.

## Property (start here)

Would you notice export from a **non-worker** identity?

## Detect / recover

Alert on internal header still present; alert on export volume. Recover: disable the bind, rotate. Do not log bodies.

## Practice

One detection sentence without naming a vendor.

## Transfer

Unexpected egress to a new object store: same operate loop.
