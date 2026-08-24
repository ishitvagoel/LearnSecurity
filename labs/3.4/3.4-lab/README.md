# Lab 3.4

**Authorized scope:** this directory only.
**Invariant:** A note share grant cannot be applied twice to exceed the product rule (max 5 members). Abuse is a **logic** invariant, not a new CWE name.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: 8 share retries yield count>5.
