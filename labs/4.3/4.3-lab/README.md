# Lab 4.3

**Authorized scope:** this directory only.
**Invariant:** A session token in the **query string** is not an acceptable session. Bearer belongs in Cookie (HttpOnly, 2.3) or Authorization, not logs and Referer.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: accepting access_token in the query string.
