# Lab E3

Authorized: this directory only. No live targets.

A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: two capture('k1') yield two charges.
