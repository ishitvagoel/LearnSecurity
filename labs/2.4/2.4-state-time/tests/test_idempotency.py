"""Forbidden outcomes: a retried or raced share_note call mints a second
grant, or a store failure is read as permission to proceed anyway.

C1 (retry) and C2 (concurrency) are the two claims this file carries genuine
assertions for. test_single_share and test_two_different_keys_are_two_shares
are the normal case and a boundary case (same key blocks; a different key
does not, so a fix cannot pass by refusing everything).
test_retry_with_the_same_key_does_not_duplicate is the module's headline
forbidden outcome. test_store_unreachable_is_denied_not_accepted is the
malformed/failure case for C3 (fail-closed on store failure) -- a claim this
lab's earlier version stated in every lesson and tested nowhere.
test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share
is C2: eight requests that are genuinely in flight at once, not a sequential
retry, which a check-then-act implementation can pass by luck of thread
scheduling but a database-level UNIQUE constraint cannot fail regardless of
scheduling. Two assertions carry the anti-fake weight:
test_retry_with_the_same_key_does_not_duplicate's own second assertion
(a replay must return the *first* call's share_id, not merely a truthy
accepted flag) rejects a fake that reports accepted:true on replay while
quietly minting a new row under the hood, and
test_a_never_elsewhere_used_key_is_still_deduplicated rejects a fake that
special-cases only the exact note/key strings this file happens to use
elsewhere.
"""
from __future__ import annotations

import concurrent.futures
from pathlib import Path
from types import ModuleType

from fastapi.testclient import TestClient


def test_single_share_with_a_key(client: TestClient, impl: ModuleType) -> None:
    resp = client.post("/notes/n1/share", headers={"Idempotency-Key": "k1"})
    assert resp.json()["accepted"] is True
    assert impl.share_count() == 1


def test_retry_with_the_same_key_does_not_duplicate(
    client: TestClient, impl: ModuleType
) -> None:
    first = client.post("/notes/n1/share", headers={"Idempotency-Key": "k1"})
    second = client.post("/notes/n1/share", headers={"Idempotency-Key": "k1"})
    assert impl.share_count() == 1, (
        "a retry carrying the same idempotency key must not leave a second "
        "row -- timeouts and retries are part of whether the share list "
        "stays honest, not only a smoother click"
    )
    assert second.json()["share_id"] == first.json()["share_id"], (
        "a replay must return the first share's id, not merely a truthy "
        "accepted flag -- the owner needs to see the share that actually "
        "exists, not a fresh id nobody can trace"
    )


def test_two_different_keys_are_two_shares(client: TestClient, impl: ModuleType) -> None:
    """Boundary: a fix that refuses every second POST regardless of key
    would also pass the retry test above by accident. This distinguishes
    'the same key twice' from 'a second, distinct, legitimate share'."""
    client.post("/notes/n1/share", headers={"Idempotency-Key": "k1"})
    client.post("/notes/n1/share", headers={"Idempotency-Key": "k2"})
    assert impl.share_count() == 2, (
        "two requests carrying two different keys are two different "
        "actions and must both be recorded; a checker that denies on any "
        "repeat request, key or not, is as broken as one that never checks"
    )


def test_store_unreachable_is_denied_not_accepted(
    client: TestClient, impl: ModuleType
) -> None:
    """Malformed/failure case for the fail-closed claim: point the module
    at a path its own connection call cannot open, so every subsequent
    connect() attempt raises, the same way a network partition or a
    downed database would from the handler's point of view."""
    real_path = impl._db_path
    impl._db_path = Path("/nonexistent-lab24-directory/shares.db")
    try:
        resp = client.post("/notes/n1/share", headers={"Idempotency-Key": "k1"})
    finally:
        impl._db_path = real_path
    assert resp.json().get("accepted") is False, (
        "a share request must be denied, not accepted, when the "
        "idempotency store cannot be reached -- reporting success while "
        "quietly failing to record the key is exactly the fail-open this "
        "module's Operate lesson forbids, and it is worse than a visible "
        "error because the caller has no reason to retry or investigate"
    )
    assert impl.share_count() == 0, (
        "nothing should have been persisted while the store was "
        "unreachable; a fix that returns accepted:false but still writes "
        "the row somewhere else has not actually failed closed"
    )


def test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share(
    impl: ModuleType,
) -> None:
    """C2: a retry (two calls, one after the other, the first already
    resolved before the second starts) is not the same failure as a race
    (two calls whose check-then-act windows genuinely overlap in time).
    test_retry_with_the_same_key_does_not_duplicate above proves nothing
    about this case, because its two calls never overlap. Eight threads
    each hold their own TestClient against the same app object and race a
    key none of the other tests in this file ever uses, so the only way to
    pass is to have made the check-and-record step atomic against real
    concurrent access -- a Python-level 'if key in seen: return' guard
    would still be exposed to this, but the fixed variant's SQL UNIQUE
    constraint is enforced by the storage engine's own write-serialization,
    which cannot be defeated by how the eight threads happen to interleave."""

    def fire(_: int) -> dict:
        return TestClient(impl.app).post(
            "/notes/n1/share", headers={"Idempotency-Key": "race-key"}
        ).json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fire, range(8)))

    assert impl.share_count() == 1, (
        "eight requests in flight at once, all carrying the same "
        "never-before-seen key, must still leave exactly one share row"
    )
    assert all(r.get("accepted") for r in results), (
        "every one of the eight concurrent requests must still see "
        "accepted:true -- replaying the one real share, not erroring out "
        "for the seven that lost the race"
    )


def test_a_never_elsewhere_used_key_is_still_deduplicated(
    client: TestClient, impl: ModuleType
) -> None:
    """Anti-fake test: constructs a note id and key that appear nowhere
    else in this file, so a fake that special-cases exactly "n1"/"k1" (the
    strings every other test in this file happens to use) cannot pass by
    memorizing them."""
    first = client.post("/notes/zz9/share", headers={"Idempotency-Key": "unseen-elsewhere-7f3"})
    second = client.post("/notes/zz9/share", headers={"Idempotency-Key": "unseen-elsewhere-7f3"})
    assert impl.share_count() == 1
    assert second.json()["share_id"] == first.json()["share_id"]


def test_missing_key_shares_once_per_call(client: TestClient, impl: ModuleType) -> None:
    """Documents this fixture's stated leftover rather than a security
    property: a request that carries no idempotency key at all shares once
    per call, because there is no key for the store to remember. Production
    should require a key for a high-impact action like this one; this
    fixture's own README and 04-build.md name that as out of scope here."""
    client.post("/notes/n1/share")
    client.post("/notes/n1/share")
    assert impl.share_count() == 2
