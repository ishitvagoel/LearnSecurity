# Lab 5.5

Authorized: this directory only.

Note fetch is parameterized: user input is not concatenated into a query string. Local model only — no live DB attacks.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: string-built SQL. The quoted fragment is a test of concatenation, not a live exploit.
