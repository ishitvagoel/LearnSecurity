"""Vulnerable: a query-string token still mints a session, and activity alone
keeps a session "active" forever, no matter how long ago it was minted.

Two independent defects live here, staged separately so each can be reasoned
about on its own. `session_from_request` prefers a query-string token over
the cookie or Authorization header. `session_is_active` checks only whether
a session has been touched recently (an idle clock); it never asks how long
ago the session was originally minted (an absolute-lifetime clock), so a
session that is touched every few minutes never expires, however old it is.
"""

from __future__ import annotations

IDLE_TIMEOUT_SECONDS = 900          # 15 minutes without activity
ABSOLUTE_TIMEOUT_SECONDS = 43_200   # 12 hours since the session was minted --
                                     # declared here, but never enforced below.


def session_from_request(query: dict, cookie: dict, header: str | None) -> str | None:
    return query.get("access_token") or cookie.get("sc_session") or header


def session_is_active(session: dict, now: float) -> bool:
    """Checks only that the session has been used recently. There is no
    absolute-lifetime check: as long as something keeps touching the session
    before it goes idle, it never expires, no matter how long ago it was
    minted. A session record missing a required timestamp is still treated
    as inactive rather than guessed at -- that much fail-closed behavior is
    not the defect this fixture stages."""
    issued_at = session.get("issued_at")
    last_seen_at = session.get("last_seen_at")
    if issued_at is None or last_seen_at is None:
        return False
    if now < last_seen_at:
        return False
    if now - last_seen_at >= IDLE_TIMEOUT_SECONDS:
        return False
    return True
