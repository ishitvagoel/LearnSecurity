# Lab 6.1

Authorized: this directory only.

A filename argument is data, not a shell program. The lab uses argv lists, not bash -c.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: sh -c with concatenated name. No live command execution in tests.
