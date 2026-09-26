"""Forbidden outcomes for module 3.1's asset-classification sink rule.

Every test drives the fixture through a real HTTP request/response cycle
(`fastapi.testclient.TestClient`, wired up in `conftest.py`) and reads the
two sinks back the same way: through `/internal/log-lines` and
`/internal/error-dumps`. Nothing here imports `CLASSIFICATION` or
`_redact` directly -- a fake that changes only the returned dictionary and
not the sinks themselves would still be caught, because these tests only
ever look at what the sinks actually emitted.

    python3 -m pytest labs/3.1/3.1-lab/tests --impl vulnerable
    python3 -m pytest labs/3.1/3.1-lab/tests --impl fixed
"""

from __future__ import annotations

import secrets


def _auth(token: str = "sess-alice") -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


# ---------------------------------------------------------------------------
# Forbidden outcomes (C1, C2)
# ---------------------------------------------------------------------------


def test_note_body_excluded_from_application_log(client) -> None:
    """C1: a Confidential note body must not reach the application log."""
    client.post("/notes/n1/read", headers=_auth())
    lines = client.get("/internal/log-lines").json()["lines"]
    assert not any("tenant-A-secret-body" in line for line in lines)


def test_session_token_excluded_from_application_log(client) -> None:
    """C2: the session token is an authority artifact, classified at least
    as sensitively as the body it gates. It must not reach the log either."""
    client.post("/notes/n1/read", headers=_auth())
    lines = client.get("/internal/log-lines").json()["lines"]
    assert not any("sess-alice" in line for line in lines)


# ---------------------------------------------------------------------------
# Boundary: a second, independent sink carries the same asset (C2)
# ---------------------------------------------------------------------------


def test_session_token_excluded_from_error_dump(client) -> None:
    """The error dump is reached only through the not-found branch -- a
    different function than log_event. Fixing the logger alone would not
    reach this sink; the session token must still be denied here."""
    client.post("/notes/missing-note/read", headers=_auth())
    dumps = client.get("/internal/error-dumps").json()["dumps"]
    assert dumps
    for dump in dumps:
        assert "sess-alice" not in str(dump.get("session_token", ""))
        assert all("sess-alice" not in str(v) for v in dump.values())


# ---------------------------------------------------------------------------
# Malformed / failure path: the sink that fires on error still leaks (C5)
# ---------------------------------------------------------------------------


def test_error_dump_still_diagnosable_without_secrets(client) -> None:
    """A denied field is not simply a reason to give operators nothing.
    The error dump must still name which note and which company failed to
    resolve, even while the token stays out of it -- denial and usefulness
    are two different requirements, not one."""
    client.post("/notes/missing-note/read", headers=_auth())
    dumps = client.get("/internal/error-dumps").json()["dumps"]
    assert dumps
    latest = dumps[-1]
    assert latest.get("note_id") == "missing-note"
    assert latest.get("company_id") == "companyA"
    assert "sess-alice" not in str(latest.get("session_token", ""))


# ---------------------------------------------------------------------------
# Normal case: redaction must not become "log nothing" (C3)
# ---------------------------------------------------------------------------


def test_allowed_metadata_present_after_redaction(client) -> None:
    """The requirement this fixture enforces is 'deny Confidential,
    allow Internal' -- not 'deny everything.' An operator debugging
    'did a note_read happen for n1' must still be able to see that from
    the log line."""
    client.post("/notes/n1/read", headers=_auth())
    lines = client.get("/internal/log-lines").json()["lines"]
    assert any(
        "note_read" in line and "note_id=n1" in line and "company_id=companyA" in line
        for line in lines
    )


def test_read_without_debug_hint_header_still_logs_normally(client) -> None:
    """A boundary on the optional field: its absence must not change
    whether the normal, documented fields are logged."""
    response = client.post("/notes/n1/read", headers=_auth())
    assert response.status_code == 200
    lines = client.get("/internal/log-lines").json()["lines"]
    assert any("note_read" in line for line in lines)


# ---------------------------------------------------------------------------
# Fail-safe default: an unclassified field is not a low-risk field (C4)
# ---------------------------------------------------------------------------


def test_unclassified_field_defaults_to_redacted(client) -> None:
    """A field this fixture's CLASSIFICATION table has never named -- the
    next schema addition nobody has classified yet -- must be denied by
    default, not allowed by default. A fresh, random value proves this
    isn't a hardcoded rule for `debug_hint` by name; any unrecognized key
    must fall to the same default."""
    fresh_hint = secrets.token_hex(16)
    client.post("/notes/n1/read", headers={**_auth(), "X-Debug-Hint": fresh_hint})
    lines = client.get("/internal/log-lines").json()["lines"]
    assert not any(fresh_hint in line for line in lines)


# ---------------------------------------------------------------------------
# Anti-fake: the mechanism must be field-based, not a string-literal cheat
# ---------------------------------------------------------------------------


def test_anti_fake_fresh_secret_not_a_literal_match(client) -> None:
    """Defeats a fake fix that special-cases the literal string
    'tenant-A-secret-body' (or any other hardcoded substring) instead of
    building a real per-field classification check. A freshly generated
    body, stored and then read back, must be excluded exactly as the
    fixture's own seeded body is."""
    fresh_body = f"note-body-{secrets.token_hex(16)}"
    client.put("/notes/n9", json={"body": fresh_body}, headers=_auth())
    client.post("/notes/n9/read", headers=_auth())
    lines = client.get("/internal/log-lines").json()["lines"]
    assert not any(fresh_body in line for line in lines)


def test_anti_fake_redaction_is_not_a_canned_line(client) -> None:
    """Defeats a fake fix that makes `log_event` always append a fixed
    literal line (e.g. '[event redacted]') regardless of input, which
    would pass every test above that only checks for a *secret's* absence.
    A canned line would also hide the *allowed* metadata that
    `test_allowed_metadata_present_after_redaction` requires, and it would
    not vary between two different note ids -- so this test reads two
    different notes and requires the log to actually distinguish them."""
    client.put("/notes/n2", json={"body": "irrelevant-for-this-test"}, headers=_auth())
    client.post("/notes/n1/read", headers=_auth())
    client.post("/notes/n2/read", headers=_auth())
    lines = client.get("/internal/log-lines").json()["lines"]
    assert any("note_id=n1" in line for line in lines)
    assert any("note_id=n2" in line for line in lines)
    assert not any("tenant-A-secret-body" in line for line in lines)
