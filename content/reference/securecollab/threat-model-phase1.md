# SecureCollab Phase 1 — threat model stub

Design stub for Module 3.2. Not a production threat-modeling SaaS.

## Freeze

- Local `assemble_threat_model` fixture. Synthetic threat ids only.
- No real scanner tenant, no live targets.

## Scanner ≠ model

A green SAST/DAST/SCA run is coverage. It does not delete `cross-tenant-read`, `hostile-browser`, or `stolen-worker`. Each row needs an owner and a review trigger.

## Change triggers

New share path; worker identity (7.4); webhook (7.3); SMS/email channel. Do not back-date the file after adding a row.

## Tests

The missing mandatory id is the evidence. A STRIDE sticker is not.
