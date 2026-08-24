# Lab 6.3

Authorized: this directory only.

A state-changing share POST without a matching origin/CSRF token is denied. Cookie session (2.3) is not the CSRF property.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: cookie-only share POST from a foreign origin.
