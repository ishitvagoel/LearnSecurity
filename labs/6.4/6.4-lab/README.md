# Lab 6.4

Authorized: this directory only.

Upload names cannot escape the lab root via .. segments. Local path join only.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: resolved path leaves /tmp/sc-lab. No real /etc access in tests.
