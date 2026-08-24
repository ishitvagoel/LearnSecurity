# 1.3-LO-05 — Attack-surface inventory and evidence

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** ASVS 5.0.0 (final) — evidence, not port lists.

## Property (start here)

Each entry point has a **closed** test or an explicit residual.

## Evidence

Client header export: `test_client_internal_header_is_not_worker_identity`. Untrusted caller: empty list. Bound worker: export allowed (then 1.2 still applies per-note in a later module).

Attack surface is not “open ports” or Top 10.

## Practice

Add one surface (admin JSON) as residual-not-yet-tested.

## Transfer

Mobile client: every local cache is a new surface (Phase 8).
