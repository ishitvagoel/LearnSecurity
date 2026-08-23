# Lab 6.5

Authorized: this directory only.

Server-side fetch allowlists lab.securecollab.test only. Link-local metadata IPs are out of scope.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: allowing 169.254.169.254. Tests do not send packets.
