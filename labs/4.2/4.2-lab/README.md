# Lab 4.2

**Authorized scope:** this directory only.
**Invariant:** Password + 'remember me' is **not** phishing-resistant. A phishing-resistant authenticator must fail a lookalike origin (WebAuthn-class). Passwords stay allowed only as a labeled residual.
**Verify:** `python3 -m pytest tests/test_property.py --impl vulnerable` (forbidden outcome fails) then `--impl fixed`.

Forbidden: password counts as phishing-resistant; WebAuthn must bind origin.
