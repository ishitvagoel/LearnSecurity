# Lab 3.3

**Authorized scope:** this directory only.
**Invariant:** Tenant isolation is not 'one Postgres role for the whole app.' A stolen app role must not SELECT other tenants without 1.2 mediation.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: shared app role reads tA notes while bound as tB.
