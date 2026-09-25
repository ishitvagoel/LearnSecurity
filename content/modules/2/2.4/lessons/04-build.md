# Push the check into the store; do not check-then-act in the handler

**Kind:** design-exercise
**Loop step:** 4 Build

## Predicting the fix before reading it

`03-break.md` traced the defect to a missing question: the handler never asks whether it has already seen this idempotency key. The most direct fix a reader could predict from that trace, without reading any further, is to add the question — look the key up, and only insert if it is not already there. That prediction is correct as far as it goes, and it is also the fix a substantial share of engineers ship, verify against a sequential retry test, and never revisit. This lesson exists because that fix is incomplete in a way a sequential test cannot reveal, and because the actually correct version looks almost identical on the page.

## Candidate A: check, then act, in the application

```text
handler(note_id, key):
    existing = database.select_by_key(key)
    if existing:
        return existing.share_id
    row = database.insert(note_id, key)
    return row.share_id
```

A competent engineer would reasonably write this, and for one request handled at a time, it is correct: the first call's `select_by_key` finds nothing, inserts, and returns; a second, later call's `select_by_key` finds the first call's row and returns it without inserting a second one. It passes `test_single_share_with_a_key` and `test_retry_with_the_same_key_does_not_duplicate` without any special effort, because both of those tests call the handler strictly one call after another, and strict sequencing is exactly the case this shape handles correctly.

It breaks precisely at the boundary `02-model.md` named as the hardest case: two calls whose `select_by_key` steps both run before either call's `insert` step runs. Nothing about Candidate A prevents this, because `select_by_key` and `insert` are two separate statements sent to the database as two separate round trips, with an arbitrarily small but real gap between them during which the Python process is free to be interrupted, rescheduled, or simply racing against a second worker process handling the second request concurrently. Both calls' checks can observe "no existing row" before either call's insert has run, and both calls then proceed to insert — the exact duplicate this module is about, produced by code that looks, read one call at a time, exactly like the fix. `05-verify.md`'s concurrency test is written specifically to exercise this gap rather than trust that it never gets hit in practice.

## Candidate B: let the database enforce uniqueness, and handle the conflict

```text
CREATE TABLE shares (..., idempotency_key TEXT UNIQUE)

handler(note_id, key):
    try:
        row = database.insert(note_id, key)   # one statement
        return row.share_id
    except UniqueConstraintViolation:
        existing = database.select_by_key(key)
        return existing.share_id
```

This is the shape `fixed/app.py` ships. The `INSERT` and the uniqueness check are now the same operation, enforced by the database engine's own write path rather than by two separate statements the application sequences by hand — when two concurrent inserts race for the same key, the database serializes the two writes internally (this is what a write-ahead or rollback journal is *for*), lets exactly one of them succeed, and rejects the other with a constraint violation the application catches and translates into "return the existing row." The atomicity does not come from anything clever in the Python code; it comes from moving the check into the one place — the storage engine's own commit path — that every concurrent writer has to go through regardless of how the application code above it happens to be scheduled. This is the general shape [1.3 Trust boundaries and attack surface](../../../1/1.3/lessons/02-model.md) calls "shared tools can make two checks into one": here, the shared tool being the single storage engine is what makes the check trustworthy, rather than a liability.

Candidate B's own trace of the counterexample above confirms the difference directly: two concurrent calls both attempt `INSERT`, the database's own row-level locking admits one write and makes the second one wait, the second one's `INSERT` then fails against a row that already exists, and the `except` branch returns that row's id rather than inserting a duplicate. Nothing about *when* the second call arrives changes this outcome, because the database's internal serialization — not the Python interpreter's thread scheduling — decides the ordering.

## Where Candidate B itself stops working

Candidate B is not a universal answer to every concurrency problem this course will meet; it works because "has this exact key been recorded" reduces cleanly to "does a row with this exact value already exist," which a uniqueness constraint answers by construction. It stops working the moment the check is not a pure existence test — for example, "does this note still have fewer than five shares" is a *count* constraint, not a uniqueness constraint, and a naive `SELECT COUNT(*) ... ; if count < 5: INSERT` reintroduces exactly the check-then-act gap Candidate A had, because no ordinary column constraint enforces "fewer than N rows matching some other row's value." A correct fix for a count-bounded resource needs a different mechanism — a database-level check constraint evaluated against a maintained counter column, or a serializable transaction isolation level around the read and the write — and [`07-transfer.md`](07-transfer.md)'s clinic scenario is a count-bounded resource for exactly this reason, not a coincidence of subject matter.

## The framework default is not the application's guarantee

Neither FastAPI nor `uvicorn` retries a POST on the server's behalf, and neither one deduplicates a request based on a header it does not know the meaning of; `Idempotency-Key` is an application-level convention, not an HTTP-level or framework-level mechanism, and nothing in the framework will refuse a second request carrying one. This matters concretely for exactly the failure `vulnerable/app.py` demonstrates: a developer who has confirmed that FastAPI validates the request shape, that Pydantic rejects a malformed body, and that the route is only reachable over HTTPS in production, has verified three real framework guarantees and zero idempotency guarantees, because none of those three checks has anything to do with whether the same key was seen before. The uniqueness constraint in Candidate B is not a framework feature either — it is a schema decision the application author has to make explicitly, and a `CREATE TABLE` statement that omits `UNIQUE` on this column silently reverts to Candidate A's failure mode even while every framework-level check continues to pass.

## Practice

Before running anything, predict which of the seven tests in `tests/test_idempotency.py` Candidate A (rewritten without the `UNIQUE` constraint) would pass and which it would fail, then verify your prediction by editing a scratch copy of `fixed/app.py` to drop the constraint and re-running the suite. Do not commit that edit; it exists only to test your prediction against reality.

## Use it somewhere new

A payment capture service and an invite-token redemption service both reduce to the same uniqueness question Candidate B answers directly — one capture id, one redemption per token — while a limited-quantity resource like a clinic's last appointment slot needs the count-bounded variant named above.

## What this page is not doing

Neither candidate here is a production payments or booking system; both are local design sketches meant to be traced by hand and against `labs/2.4/2.4-state-time/`, not deployed anywhere.
