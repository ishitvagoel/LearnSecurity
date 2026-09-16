"""Forbidden outcome: a high-impact recovery control is color- or mouse-only.

C2 is the property under test. The first test is the module's stated
forbidden outcome, asserted unconditionally against whichever variant
``--impl`` loaded: it must fail on vulnerable's factory object and pass on
fixed's. The next three probe boundaries the original single test never
touched. The last two are the anti-fake pair: they call
``is_usable_accessible`` directly on constructed input, independent of
either module's factory, so a fake "fixed" checker that just returns
``True`` unconditionally -- while leaving a bad object in place -- cannot
pass by having the object and the checker agree with each other.
"""


def test_recovery_control_is_usable_and_accessible(recovery) -> None:
    """The module's forbidden outcome. This assertion does not branch on the
    object's own flags -- it states the requirement once, and the vulnerable
    fixture is expected to fail it."""
    ctrl = recovery.recovery_confirm_control()
    assert recovery.is_usable_accessible(ctrl), (
        "inaccessible recovery is a security failure (lockout or unsafe workaround)"
    )


def test_color_only_without_name_is_rejected(recovery) -> None:
    """Color present, no name, not flagged mouse-only. This is the case the
    module's title names directly -- "color is the only cue" -- and it is a
    different input from the mouse-only fixture, so it needs its own test."""
    color_only = {"color": "green", "mouse_only": False, "keyboard": True}
    assert recovery.is_usable_accessible(color_only) is False, (
        "a control with no accessible name fails even if it is keyboard-operable "
        "and not flagged mouse-only -- color was still the only cue a sighted "
        "mouse user had, and a screen reader announces nothing"
    )


def test_missing_keyboard_flag_is_not_silently_accepted(recovery) -> None:
    """A control that never mentions keyboard support at all -- not
    mouse_only=True, just silent on the question. Checking only for the
    absence of the bad flag treats missing evidence as a guarantee, which is
    fail-open by omission. Read a failure here on --impl vulnerable as the
    finding, not as a bug in the test: it names a real gap in that checker."""
    silent_on_keyboard = {"name": "Confirm account recovery", "mouse_only": False}
    assert recovery.is_usable_accessible(silent_on_keyboard) is False, (
        "a control that never declares keyboard support must not be accepted just "
        "because mouse_only happens to be false; missing evidence is not a guarantee"
    )


def test_whitespace_only_name_is_rejected(recovery) -> None:
    """A name field that is present but contains no announceable content.
    ``not "  "`` is False in Python, so a naive truthiness check on `name`
    accepts this; a screen reader announces silence."""
    whitespace_name = {"name": "   ", "keyboard": True, "mouse_only": False}
    assert recovery.is_usable_accessible(whitespace_name) is False, (
        "a whitespace-only name satisfies a bare truthiness check but announces "
        "nothing a screen-reader user could act on"
    )


def test_checker_rejects_a_bad_control_regardless_of_variant(recovery) -> None:
    """Anti-fake test. A fake repair could leave a bad control object in place
    and just hardcode is_usable_accessible to return True -- the module's own
    factory test above would then pass for the wrong reason. This calls the
    checker directly on input the test controls, independent of either
    module's factory, so that fake cannot pass on either --impl."""
    bad = {"color": "green", "mouse_only": True}
    assert recovery.is_usable_accessible(bad) is False, (
        "the checker must reject a bad control on its own merits, not because "
        "this module's factory happens to also produce a bad control"
    )


def test_checker_accepts_a_good_control_regardless_of_variant(recovery) -> None:
    """Anti-fake test, the other direction: a checker hardcoded to always
    return False would make the module unusable but would still make the
    forbidden-outcome test above look correct on --impl vulnerable. A checker
    that always denies is exactly as fake as one that always allows."""
    good = {"name": "Confirm account recovery", "keyboard": True, "mouse_only": False}
    assert recovery.is_usable_accessible(good) is True, (
        "the checker must accept a genuinely good control on its own merits, not "
        "reject everything to look strict"
    )
