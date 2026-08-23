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
