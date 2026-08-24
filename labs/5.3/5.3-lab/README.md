# Lab 5.3

Authorized: this directory only.

A disposable lab API key must not be a hardcoded default that always authenticates. Rotation means the old value fails.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: old hardcoded sk-lab-hardcoded still authenticates after rotation.
