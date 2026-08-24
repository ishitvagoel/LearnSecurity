# Lab E5

Authorized: this directory only. No live targets.

Tenant id for a query comes from the session, not from the JSON body. Body-supplied tenant is confused deputy of the isolation key (4.4, 7.1).

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: body tenant B overrides session A.
