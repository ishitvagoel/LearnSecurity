# 1.4-LO-03 — Color-only recovery confirm

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** WCAG 2.2 (final). Local fixture only.

## Property (start here)

Does `is_usable_accessible(recovery_confirm_control())` fail when confirm is green and mouse-only?

No live IdP. Run `labs/1.4/1.4-risk-register/` pytest.

## Practice

Name the user-harm if the control stays as-is (lockout vs shared session).
