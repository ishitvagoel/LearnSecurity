# Lab 10.4

Authorized: this directory only. No live targets.

Production must not boot with debug=True. Configuration is part of the TCB.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: prod+debug boots.
