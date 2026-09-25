# Seeded review of a check-then-insert share fix

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Treat `labs/2.4/2.4-state-time/review/candidate_fix.py` as a pull request a teammate has opened against the vulnerable handler, with a commit message claiming "adds idempotency check and thread-safety for the share endpoint." It is not the shipped `fixed/app.py`; it is a separate, plausible attempt seeded with issues at more than one severity, and your job is to find them by reading, not by running `pytest` and trusting a green result — this file is not wired into the test suite at all, on purpose, so that reading is the only tool available.

## Reading order, before any conclusion

Apply this order to the file yourself, answering each question with a specific line reference, before reading any further in this lesson or opening the examiner key:

1. **Where does authority over the row get resolved?** Find every statement that reads or writes the `shares` table, and determine whether the check ("has this key been seen") and the act ("record this key") happen as one operation the database enforces, or as two separate statements the application sequences by hand.
2. **Where does state actually change, and under what protection?** If the code uses any synchronization primitive — a lock, a semaphore, a transaction — trace where that primitive is created and confirm it is the *same* object across every request that needs to contend for it, not a new one minted per call.
3. **What happens on the failure path?** Find every `except` clause, and for each one, determine whether it denies the action or reports success without having completed it.
4. **What does the failure path make visible, and to whom?** If the failure path logs anything, check whether the fields it records match the shape [`06-operate.md`](06-operate.md) requires — hashed key material and correlation ids, never the raw key — or whether it prints something closer to a debugging statement than an operational signal.

A reviewer who can answer all four with a quoted line, rather than a general impression of "looks reasonable," has actually reviewed the file.

## Worked example: reading the check-then-act line by line

```python
existing = conn.execute(
    "SELECT id FROM shares WHERE idempotency_key = ?", (idempotency_key,)
).fetchone()
if existing:
    return {"accepted": True, "share_id": existing[0], "replayed": True}
conn.execute(
    "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)",
    (note_id, idempotency_key),
)
```

Read this in isolation and it looks correct, and for one request at a time it is: the `SELECT` finds nothing, the `INSERT` proceeds, a second sequential call's `SELECT` finds the first call's row and returns early. A reviewer who traces only one call at a time, exactly the trap `04-build.md`'s Candidate A sets, will approve this. Now widen the trace to two calls whose statements interleave: both `SELECT`s can run, both finding nothing, before either `INSERT` runs — nothing in this snippet's own five lines prevents that, because nothing here is a single atomic operation across the two statements. Whether that interleaving is actually possible in this file depends on question 2 above, which is exactly why the reading order matters: this snippet's correctness cannot be judged from this snippet alone.

## Problems to find, and why the lock does not answer question 2

The candidate fix wraps its check-then-act block in a `with lock:` statement, which reads as a direct, on-topic response to the concurrency concern this module teaches — and this is precisely why it is worth reviewing carefully rather than accepting on sight. Trace where `lock` comes from: it is `threading.Lock()`, instantiated as the first line inside the `share_note` function body, meaning every single call to this endpoint constructs its own, brand-new lock object that no other call has ever seen or ever will. Two concurrent requests each acquire their own private lock instantly and proceed straight through the "protected" section without ever contending with each other, because contention requires two threads to compete for the *same* object, and this code guarantees they never do. A lock that nothing else can ever be waiting on provides the appearance of thread-safety in a code review while providing none of its substance — a finding worth naming specifically as "the lock is not shared," not generically as "concurrency issue," because the specific defect is what tells the author how to fix it: move the lock's construction to module scope, or drop the hand-rolled lock entirely in favor of the database-level uniqueness constraint `04-build.md` prefers for exactly this reason.

## A plausible non-issue

A reviewer trained to flag "unvalidated input" everywhere might raise that `note_id: str` accepts any string in the URL path with no format check against, say, a UUID pattern. For this specific review, that is not a finding: nothing about this module's property depends on what shape a note id takes, and a malformed or nonexistent note id would fail for reasons entirely unrelated to idempotency — whatever check confirms a note exists and that the caller may act on it belongs to [1.2 Authority and protection](../../../1/1.2/lessons/01-property.md), not to this workflow's retry-and-race behavior. Raising it here spends review effort on a real category of bug that is not, in this diff, actually present, and a reviewer who reports it as a headline finding has confused "a general good practice" with "a defect in this specific change."

## Severity, named explicitly rather than left implicit

The check-then-act gap and the unshared lock are the same underlying defect from two angles — the lock was the author's own (failed) attempt to close the check-then-act gap — and together they are the highest-severity finding, because they leave the module's central forbidden outcome fully reachable under real concurrent load despite the PR's own claim to have fixed exactly that. The bare `except Exception` returning `accepted: true` on any failure is a distinct, independently serious finding, because it reintroduces the fail-open behavior [`01-property.md`](01-property.md) names as its own separate forbidden outcome — fixing the concurrency gap would not fix this one, and fixing this one would not fix the concurrency gap. The raw-key logging in that same handler is lower severity on its own (it does not create a duplicate share), but it compounds the failure path's other problems: exactly when something has already gone wrong is when this code is now also writing the unhashed idempotency key to standard output.

## Use it somewhere new

The same four-question reading order applies unchanged to a payment-capture or booking-service pull request claiming to add idempotency protection: locate the check-then-act boundary, confirm any lock is actually shared, trace every failure path for fail-open behavior, and check what the failure path logs.

## What this page is not doing

`candidate_fix.py` is a reading exercise, not an executable part of this lab's test suite, and it must not be imported, run, or treated as a template for a real fix; the actual structural fix is `fixed/app.py`, verified by `pytest --impl fixed`. Findings and their rationale live only in `content/assessment/keys/2.4.md`; do not write them anywhere a learner would see them before attempting this review.
