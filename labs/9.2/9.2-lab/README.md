# Lab 9.2

Authorized: this directory only. No live targets.

A diff that concatenates eval( on user input must not be approved. Review is complete mediation of the interpreter, not a checklist LGTM.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: approving a diff containing eval(user).
