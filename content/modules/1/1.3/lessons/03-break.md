# 1.3-LO-03 — Second layer that trusts the same identifier

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** Saltzer least common mechanism (1975, seminal). Local fixture only.

## Property (start here)

Does sending `X-SecureCollab-Internal: 1` from the **client** dump all notes?

## Attacker capabilities and trust assumptions

Bob (or anyone who can set headers on the local call). Target: `labs/1.3/1.3-trust-boundaries/` only.

## Observe

Vulnerable `export_notes` treats the header as worker identity — correlated with “the app checks a header too.” Impact: both tenants’ bodies. Do not replay this header against any network host.

## Practice

Run README pytest. Name the forbidden outcome in one sentence.

## Transfer

If the CDN injects the same header, is that a new independent layer?
