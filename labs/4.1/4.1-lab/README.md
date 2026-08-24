# Lab 4.1

**Authorized scope:** this directory only.
**Invariant:** A **deleted** SecureCollab user must not read notes with a leftover session. Lifecycle is part of 1.2 mediation over time.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: delete_user leaves session_valid True.
