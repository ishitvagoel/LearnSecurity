"""C1: a query-string token must never mint or resume a session; cookie and
Authorization must keep working. C3: a session needs BOTH an idle timeout
and an absolute lifetime -- activity alone must not extend a session past
its absolute limit, and a missing timestamp must fail closed, not be
guessed at.
"""

from __future__ import annotations

IDLE_TIMEOUT_SECONDS = 900
ABSOLUTE_TIMEOUT_SECONDS = 43_200


# ---------------------------------------------------------------------------
# C1 -- channel: query string is refused; cookie and header still work.
# ---------------------------------------------------------------------------

def test_query_string_token_is_rejected(impl) -> None:
    got = impl.session_from_request({"access_token": "secret"}, {}, None)
    assert got is None


def test_cookie_session_still_works(impl) -> None:
    got = impl.session_from_request({}, {"sc_session": "cookie-tok"}, None)
    assert got == "cookie-tok"


def test_authorization_header_still_works(impl) -> None:
    got = impl.session_from_request({}, {}, "header-tok")
    assert got == "header-tok"


# ---------------------------------------------------------------------------
# C3 -- lifetime: idle AND absolute limits, both enforced together.
# ---------------------------------------------------------------------------

def test_active_session_within_both_windows_is_active(impl) -> None:
    """Normal case: minted an hour ago, touched a minute ago -- well inside
    both the idle window and the absolute window."""
    now = 1_000_000.0
    session = {"id": "s1", "issued_at": now - 3_600, "last_seen_at": now - 60}
    assert impl.session_is_active(session, now) is True


def test_forbidden_outcome_activity_alone_does_not_extend_the_absolute_limit(impl) -> None:
    """The module's C3 forbidden outcome. A session minted roughly six days
    ago (far past the 12-hour absolute cap) but touched one second ago must
    NOT be reported active. An idle-only check sees "touched one second
    ago" and stops looking; it never asks how long ago this session was
    actually minted, so it silently promises an absolute lifetime it never
    enforces. This is the exact shape of a stolen token being kept alive
    indefinitely by periodic replay."""
    now = 1_000_000.0
    ancient_but_active = {
        "id": "s2",
        "issued_at": now - (ABSOLUTE_TIMEOUT_SECONDS * 10),  # ~6 days ago
        "last_seen_at": now - 1,                              # touched 1s ago
    }
    assert impl.session_is_active(ancient_but_active, now) is False, (
        "activity within the idle window is not the same evidence as being "
        "within the absolute lifetime; a session this old must be inactive "
        "no matter how recently it was touched"
    )


def test_idle_timeout_boundary_exact_deadline_is_expired(impl) -> None:
    """Exactly at the idle deadline, the session is already expired -- the
    deadline is the first moment a session is no longer good, not the last
    moment it still is. One second earlier, it must still be active. Both
    helpers share this logic, so both must agree here; the module's defect
    is the missing absolute check, not this boundary."""
    now = 1_000_000.0
    issued_at = now - 100  # comfortably inside the absolute window either way
    at_deadline = {"id": "s3", "issued_at": issued_at, "last_seen_at": now - IDLE_TIMEOUT_SECONDS}
    one_second_early = {"id": "s3", "issued_at": issued_at, "last_seen_at": now - IDLE_TIMEOUT_SECONDS + 1}
    assert impl.session_is_active(at_deadline, now) is False, (
        "exactly at the idle deadline must already be expired"
    )
    assert impl.session_is_active(one_second_early, now) is True, (
        "one second before the idle deadline must still be active"
    )


def test_missing_timestamp_fails_closed_not_open(impl) -> None:
    """A session record missing a required timestamp cannot be proven
    active. A plausible-looking fake reads a missing field with
    session.get("issued_at", now) -- "assume it was just minted" -- which
    is fail-open: it turns "we don't know this session's age" into the most
    trusting possible answer. The correct behavior is to fail closed."""
    now = 1_000_000.0
    missing_issued_at = {"id": "s4", "last_seen_at": now - 5}
    missing_last_seen_at = {"id": "s4", "issued_at": now - 5}
    assert impl.session_is_active(missing_issued_at, now) is False
    assert impl.session_is_active(missing_last_seen_at, now) is False


def test_anti_fake_absolute_expiry_with_fresh_never_elsewhere_used_values(impl) -> None:
    """Anti-fake test, direction one. A fake repair could special-case the
    exact issued_at/last_seen_at values the forbidden-outcome test above
    happens to use -- for example hard-coding a check against that one
    issued_at constant -- while leaving the general absolute-lifetime
    arithmetic broken. This constructs a different ancient-but-active
    session, with values never written anywhere else in this file, so
    memorizing one pair of numbers cannot pass it."""
    now = 2_500_000.0
    different_ancient_but_active = {
        "id": "s5",
        "issued_at": now - 900_000,   # roughly 10 days, still far past the cap
        "last_seen_at": now - 3,
    }
    assert impl.session_is_active(different_ancient_but_active, now) is False, (
        "the absolute-lifetime check must refuse a genuinely old, actively "
        "touched session it has not seen before, not only the one pair of "
        "timestamps this test file happens to call the forbidden-outcome case"
    )


def test_anti_fake_active_session_with_fresh_never_elsewhere_used_values(impl) -> None:
    """Anti-fake test, the other direction: a checker hardcoded to always
    report inactive would make the fixed variant unusable but could still
    look correct against the forbidden-outcome and missing-timestamp cases
    alone. A checker that always denies is as fake as one that always
    allows. Fresh values, never used elsewhere in this file."""
    now = 2_500_000.0
    freshly_active = {"id": "s6", "issued_at": now - 120, "last_seen_at": now - 5}
    assert impl.session_is_active(freshly_active, now) is True
