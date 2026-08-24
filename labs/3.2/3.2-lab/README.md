# Lab 3.2

**Authorized scope:** this directory only.
**Invariant:** A green scanner does **not** mean 'no threats.' SecureCollab threat model must still list a cross-tenant reader and a hostile Next.js client.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: empty threat list when scanner_green=True.
