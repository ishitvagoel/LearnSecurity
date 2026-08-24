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
