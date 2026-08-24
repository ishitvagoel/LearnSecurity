# Lab 6.7

Authorized: this directory only.

Export API allows at most 3 calls per principal per window. Availability is a 1.1 cell, not 'buy a bigger box'.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: unbounded export.allow(4).
