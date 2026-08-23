# Lab 10.1

Authorized: this directory only. No live targets.

A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: merge_ok on a PR with no threat_model.
