# Lab 8.4

Authorized: this directory only. No live targets.

A debug-signed lab build must not call the production export API even if a client attest string is present.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: debug build with attest=ok is allowed.
