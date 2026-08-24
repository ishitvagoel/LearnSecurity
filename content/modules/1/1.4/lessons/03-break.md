# 1.4 — Risk, people, economics, usable security, and resilience (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.

## Property (start here)

A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.

## Attacker capabilities and trust assumptions

- **Attacker:** A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.
- **Trust:** Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.
**Forbidden outcome:** High-impact recovery control is color- or mouse-only

**Authorized scope:** `labs/1.4/1.4-risk-register` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable control is color- and mouse-only.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: High-impact action gated by a widget is_usable_accessible() fails.

## Vulnerable fixture (local)

```python
"""Vulnerable: recovery confirm is color-only (inaccessible = insecure)."""


def recovery_confirm_control() -> dict:
    return {"id": "confirm-recovery", "color": "green", "mouse_only": True}


def is_usable_accessible(control: dict) -> bool:
    if control.get("mouse_only"):
        return False
    if not control.get("name"):
        return False
    if control.get("color") and not control.get("name"):
        return False
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Psychological acceptability ignored; control designed for a demo mouse. |
| Impact | Lockout; or user pastes recovery codes into a chat; residual 1.1 confidentiality loss. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/1.4/1.4-risk-register/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?

## Non-goals

No live-target instructions. Synthetic data only.
