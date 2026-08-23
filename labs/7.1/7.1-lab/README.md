# Lab 7.1

Authorized: this directory only.

JSON PATCH cannot set is_admin. Unknown fields are ignored or rejected — mass assignment is an authorization bug.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: PATCH sets is_admin True.
