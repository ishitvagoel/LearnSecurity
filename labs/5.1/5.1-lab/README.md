# Lab 5.1

Authorized: this directory only.

After account deletion, SecureCollab must not retain note **bodies** in an 'analytics' copy. Retention is a 1.1 privacy/confidentiality property.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: analytics still holds the body after delete.
