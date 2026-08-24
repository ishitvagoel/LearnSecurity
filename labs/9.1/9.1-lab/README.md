# Lab 9.1

Authorized: this directory only. No live targets.

A requirement id is covered only if a test asserts the isolation property, not if a spreadsheet row exists.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: mapping AUTHZ-1 to a test that does not assert isolation.
