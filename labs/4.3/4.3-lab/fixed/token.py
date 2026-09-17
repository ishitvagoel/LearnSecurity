"""Fixed: a query-string token never mints a session, and a session needs
both an idle clock and an absolute clock to stay active.

`session_from_request` refuses any request whose query string carries
`access_token`, before looking at cookie or header at all, and never reads a
session value out of the query string under any key name -- the function has
no code path that returns anything from `query`. `session_is_active` fixes
the second, independent defect from `vulnerable/token.py`: it enforces an
idle timeout AND an absolute lifetime, and it fails closed (returns False,
never raises) on a session record missing a required timestamp, on a
timestamp that would imply a negative duration, or on either deadline being
reached or passed.

A tempting shortcut this file deliberately does not take: reading a missing
timestamp with `session.get("issued_at", now)` looks like a harmless
default, but it silently treats "we have no idea how old this session is"
as "this session was just minted" -- the single most trusting answer
available for exactly the record that has proven the least. The explicit
`is None` checks below exist so a missing timestamp fails the session
instead of being quietly forgiven.
"""

from __future__ import annotations

IDLE_TIMEOUT_SECONDS = 900          # 15 minutes without activity
ABSOLUTE_TIMEOUT_SECONDS = 43_200   # 12 hours since the session was minted


def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    if query.get("access_token"):
        return None
    return cookie.get("sc_session") or header


def session_is_active(session: dict, now: float) -> bool:
    """A session is active only while it is within BOTH an idle window since
    its last recorded activity AND an absolute window since it was minted.
    Either deadline reached or passed means the session is no longer active,
    independent of the other -- activity alone must never extend a session
    past its absolute lifetime. A session missing either timestamp, or
    carrying a timestamp that would put it in the future relative to `now`,
    cannot be proven active and fails closed."""
    issued_at = session.get("issued_at")
    last_seen_at = session.get("last_seen_at")
    if issued_at is None or last_seen_at is None:
        return False
    if now < issued_at or now < last_seen_at:
        # A last-seen or issued time in the future relative to "now" --
        # clock skew, or a forged/replayed record -- cannot be trusted to
        # compute a non-negative age from.
        return False
    if now - last_seen_at >= IDLE_TIMEOUT_SECONDS:
        return False
    if now - issued_at >= ABSOLUTE_TIMEOUT_SECONDS:
        return False
    return True
