# Lab 3.1

**Authorized scope:** this directory only.
**Invariant:** Note **bodies** are Confidential; they must not appear in application logs. Classification is a property of the field, not a spreadsheet label.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: note body in logs. Classification drives logging, not 'debug=true'.
