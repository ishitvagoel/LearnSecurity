# Lab 8.3

Authorized: this directory only. No live targets.

A deep link query as= must not switch the signed-in principal. Exported activities are an attack surface; the session is the identity.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: query as=admin becomes the session user.
