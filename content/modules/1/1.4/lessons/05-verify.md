# 1.4 — Risk, people, economics, usable security, and resilience (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | High-impact recovery control is color- or mouse-only |
| Failure | Fail closed: Keyboard operable, name in accessible tree, not color-only (WCAG 2 |

Lab tests: `test_recovery_a11y.py` under `labs/1.4/1.4-risk-register`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `High-impact recovery control is color- or mouse-only`
- `--impl fixed`: **pass**

is_usable_accessible True only when name+keyboard+non-color cue exist.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
