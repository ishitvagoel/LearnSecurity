"""Vulnerable: recovery confirm is color-only and mouse-only.

C2: an account-recovery confirm step that a legitimate owner cannot complete
with a keyboard, a name a screen reader can speak, and a cue that is not
color alone has failed as a security control, not as a UI nit.

The object is the obvious defect: color, no name, mouse-only. The checker
carries a second, quieter defect that the tests are written to expose on
purpose — it never asks for positive evidence of keyboard support. It only
checks that ``mouse_only`` is not set. A control with no ``keyboard`` key at
all (never declared either way) slips through, because absence of the bad
flag is being treated as proof of the good guarantee. That is fail-open by
omission, not by explicit misconfiguration, and it is the same shape as the
"we didn't check that path" failures earlier modules named.
"""


def recovery_confirm_control() -> dict:
    return {"id": "confirm-recovery", "color": "green", "mouse_only": True}


def is_usable_accessible(control: dict) -> bool:
    """The checker. It is meant to be called on arbitrary control dicts, not
    only on this module's own factory output -- see the anti-fake tests in
    tests/test_recovery_a11y.py, which construct inputs directly."""
    if control.get("mouse_only"):
        return False
    if not control.get("name"):
        return False
    if control.get("color") and not control.get("name"):
        return False
    return True
