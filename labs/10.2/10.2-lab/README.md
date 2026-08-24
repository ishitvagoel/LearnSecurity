# Lab 10.2

Authorized: this directory only. No live targets.

Install must fail when the lockfile hash does not match the fetched artifact. CI green is not integrity of dependencies.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: installing when lock hash mismatches.
