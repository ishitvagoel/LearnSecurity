# Lab 7.4

Authorized: this directory only.

A worker job must use **service identity**, not a leftover user session, to export notes. Stale 1.2 grants (2.4) still apply.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: exporting under alice's session from a worker job.
