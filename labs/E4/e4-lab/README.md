# Lab E4

Authorized: this directory only. No live targets.

A copy into a 4-byte lab buffer must not return more than 4 bytes. This models a length mismatch — it is not a weaponized native exploit.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: copy returns more bytes than the buffer. Teaching bounds, not an exploit.
