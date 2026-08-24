"""Forbidden outcome: high-impact recovery control is color- or mouse-only."""


def test_recovery_control_is_usable_and_accessible(recovery) -> None:
    ctrl = recovery.recovery_confirm_control()
    assert recovery.is_usable_accessible(ctrl), (
        "inaccessible recovery is a security failure (lockout or unsafe workaround)"
    )
