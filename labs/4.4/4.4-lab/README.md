# Lab 4.4

**Authorized scope:** this directory only.
**Invariant:** A share **grant** for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: any grant for bob allows every note id.
