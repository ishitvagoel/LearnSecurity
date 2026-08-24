# Lab 6.6

Authorized: this directory only.

An invite token cannot be accepted twice. Exceptional retry is not a second membership (ties 2.4).

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: second accept('t1') succeeds.
