# 1.4 — Risk, people, economics, usable security, and resilience (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
recovery_confirm_control exposes role=button, name, keyboard=True, color_only=False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
"""Fixed: named, keyboard-operable recovery confirm (WCAG 2.2 as web baseline)."""


def recovery_confirm_control() -> dict:
    return {
        "id": "confirm-recovery",
        "name": "Confirm account recovery",
        "keyboard": True,
        "color": "green",
        "mouse_only": False,
    }


def is_usable_accessible(control: dict) -> bool:
    if control.get("mouse_only"):
        return False
    if not str(control.get("name", "")).strip():
        return False
    if not control.get("keyboard"):
        return False
    return True
```

## Why this restores the cell

Keyboard operable, name in accessible tree, not color-only (WCAG 2.2).

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

A React component library “accessible by default” is not your journey. You still test the recovery path.

CAPTCHA or “confirm in the app” can recreate the same exclusion.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

## Residual risk

Coercion: a physically present attacker can still force a confirmation. Record as residual (do not pretend UX fixes coercion).
