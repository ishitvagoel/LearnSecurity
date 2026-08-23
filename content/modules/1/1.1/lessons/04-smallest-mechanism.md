# 1.1-LO-04 — Smallest mechanism that restores a property

**Kind:** design-exercise  
**Loop step:** 4 Build

## Property

Pick **one** failed or unstated invariant from LO-02/LO-03 (usually: “password hashes are not the confidentiality of notes”).

## Task

Write the **smallest trustworthy mechanism** that would restore *that* invariant—not a product shopping list.

Example shape (you must make it specific):

- Property: Tenant note bodies never appear in application logs.
- Mechanism: structured logging allowlist of field names; tests that fail if `body` is logged.
- Why not “buy a SIEM”: that is not the property.

Separate **framework default** (uvicorn access log) from **application guarantee** (your allowlist).

## Detection and recovery

If the allowlist is bypassed, what log/alert/purge is required? (Operate preview of LO-06.)

## Transfer

If the same property must hold for a future webhook payload, what changes?
