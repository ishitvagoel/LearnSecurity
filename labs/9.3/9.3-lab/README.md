# Lab 9.3

Authorized: this directory only. No live targets.

A test that only asserts status 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: treating a status-only test as a security test.
