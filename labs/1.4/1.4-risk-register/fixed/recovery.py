"""Fixed: named, keyboard-operable recovery confirm (WCAG 2.2 as web baseline).

The structural fix has two parts, not one:

1. The object declares positive keyboard support (``keyboard: True``), not
   merely the absence of ``mouse_only``.
2. The checker requires that positive declaration. ``control.get("keyboard")``
   must be truthy -- a control that never mentions keyboard support at all
   is rejected, not silently accepted. This closes the fail-open-by-omission
   gap the vulnerable checker had: checking for the absence of a bad flag is
   not the same as checking for the presence of a good guarantee.

The checker also treats a whitespace-only name as absent. ``"  "`` would
satisfy a naive truthiness check (``not "  "`` is ``False``) while a screen
reader announces nothing a user could act on -- the name has to have visible
content, not merely be a non-empty string.
"""


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
