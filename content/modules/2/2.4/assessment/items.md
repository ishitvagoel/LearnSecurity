# 2.4 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/2.4.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find in a pull request touching `share_note`:

**A.** "We wrapped the check-then-insert block in a `threading.Lock()` created at the top of the handler function, so two concurrent requests can't race each other."
**B.** "Two requests carrying the same idempotency key must produce exactly one committed share row, whether they arrive one after another or genuinely at the same time — and the second response must return the first row's own id."
**C.** "Our staging environment has run this endpoint for three months without ever showing two rows for one key."
**D.** "We `SELECT` for the key before we `INSERT`, so a retry can never insert a second row."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1, C2 · **Outcome:** State the property a retry must satisfy and name the check-then-act structure that still fails under real concurrent access

## 2. Discrimination — property vs. mechanism for fail-closed

Four statements about the idempotency store:

**A.** "The handler's outer `try` catches any `sqlite3.Error` and returns `accepted: false` on all of them."
**B.** "The share endpoint must deny the action, and must not persist anything, whenever it cannot confirm the idempotency key was actually recorded."
**C.** "Our managed database has a 99.99% uptime SLA, so store-unreachable is not worth designing for."
**D.** "We retry the database connection twice with backoff before giving up."

Identify which statement states the property and which state mechanisms, proxies, or non-answers for it, and rank the mechanism/proxy statements by how close each comes to being real evidence for the property.

**Claim assessed:** C3 · **Outcome:** On the same fixture, show the share endpoint denying rather than accepting a request when its idempotency store is unreachable

## 3. Diagnosis — a narrower failure path

```python
def share_note(note_id, idempotency_key):
    try:
        conn = _connect()
        conn.execute(
            "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)",
            (note_id, idempotency_key),
        )
        conn.commit()
        return {"accepted": True}
    except sqlite3.OperationalError:
        return {"accepted": False, "reason": "store_unavailable"}
```

This handler is not `vulnerable/app.py` and not `fixed/app.py` — it is a third variant with no `UNIQUE` constraint on `idempotency_key`, and a narrower `except` clause than either shipped file uses. Name the root cause of why this handler still fails this module's forbidden outcomes, the precondition under which each failure actually occurs, and the impact — as three distinct answers, not one answer restated three times. Consider both the retry/race behavior and the store-failure behavior.

**Claim assessed:** C1, C2, C3 · **Outcome:** On the local FastAPI/SQLite fixture, show both a sequential retry and eight genuinely concurrent first-requests failing to duplicate a share; on the same fixture, show the share endpoint denying rather than accepting a request when its idempotency store is unreachable

## 4. Diagnosis — predicting a candidate fix under concurrency

A teammate proposes replacing the vulnerable handler with this shape, reasoning that it directly answers `03-break.md`'s missing question:

```python
def share_note(note_id, idempotency_key):
    conn = _connect()
    existing = conn.execute(
        "SELECT id FROM shares WHERE idempotency_key = ?", (idempotency_key,)
    ).fetchone()
    if existing:
        return {"accepted": True, "share_id": existing[0]}
    row = conn.execute(
        "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)", (note_id, idempotency_key)
    )
    conn.commit()
    return {"accepted": True, "share_id": row.lastrowid}
```

Without running any code, predict which of the seven tests in `tests/test_idempotency.py` this shape passes and which it fails, and explain your prediction by tracing what happens when eight threads call this function at once, all carrying a key none of them has used before.

**Claim assessed:** C2, C4 · **Outcome:** On the local FastAPI/SQLite fixture, show both a sequential retry and eight genuinely concurrent first-requests failing to duplicate a share

## 5. Design — a mechanism choice under a deployment constraint

Two engineers propose closing the concurrency gap in `share_note`. Engineer A adds a module-level `threading.Lock()`, constructed once outside the handler function and acquired inside it on every call. Engineer B moves the `idempotency_key` column's `UNIQUE` constraint into the schema and lets the database reject the second insert. Under the constraint that SecureCollab's production deployment runs the FastAPI app under `uvicorn` with **four separate worker processes**, not one process with multiple threads, choose between the two proposals and defend your choice, including the specific reason the proposal you did not choose still fails under this constraint even if it were implemented correctly (a properly shared, module-level lock, not `candidate_fix.py`'s per-call one).

**Claim assessed:** C4 · **Outcome:** State the property a retry must satisfy and name the check-then-act structure that still fails under real concurrent access; transfer the retry, race, and fail-closed reasoning to a different limited resource

## 6. Design — a count-bounded resource under a constraint

SecureCollab wants to cap a note at five pending share invites at once. Engineer A proposes a `UNIQUE` constraint on `(note_id, invite_id)` — the same mechanism `fixed/app.py` uses for the idempotency key. Engineer B proposes a `pending_count` column on the note row, checked and incremented inside one transaction under `SERIALIZABLE` isolation. Under the constraint that the fix must correctly refuse a sixth concurrent invite attempt when five are already pending, evaluate Engineer A's proposal and state specifically what question a `UNIQUE` constraint answers that is not the question this cap needs answered.

**Claim assessed:** C4 · **Outcome:** Transfer the retry, race, and fail-closed reasoning to a different limited resource and state which claims survive the change unchanged and which do not

## 7. Transfer — the clinic's last appointment slot

Using the clinic scenario from `lessons/07-transfer.md`, state which of this module's claims (C1, C3, C4) the lesson names explicitly as surviving or breaking when the asset changes from "has this exact key been seen" to "how many patients has this slot already admitted," and trace by hand what a naive `SELECT COUNT(*) WHERE slot=S9` followed by a separate `INSERT` does when two patients' count-checks both run before either patient's insert has committed.

**Success criteria:** Your answer must name the specific mechanism difference — a uniqueness constraint answers an existence question, a capacity limit needs a maintained count under one atomic operation — and must trace the two-patient race concretely enough to state the resulting row count, not merely assert that "a race is possible."

**Claim assessed:** C1, C3, C4 · **Outcome:** Transfer the retry, race, and fail-closed reasoning to a different limited resource and state which claims survive the change unchanged and which do not

## 8. Operate — the replay signal and its residual

Write the log line your system would emit when a genuinely concurrent race resolves to one winning row and seven callers are told `replayed: true`. State which fields it must carry, which field it must never carry, and explain why this signal — even correctly emitted and correctly alerted on — cannot detect a worker that redelivers a share job after the underlying grant has since been revoked.

**Claim assessed:** C3, C5 · **Outcome:** On the same fixture, show the share endpoint denying rather than accepting a request when its idempotency store is unreachable

---

## Evidence checklist

- [ ] State machine (Lesson 02) naming the retry loop-back, the race loop-back, and the `Denied` state as three distinct transitions out of `FirstCommit`/`Attempt`
- [ ] Lab `labs/2.4/2.4-state-time`: `vulnerable/` tests show 4 of 7 failing for the stated security reasons (no check at all; fail-open on storage error); `fixed/` tests show 7 of 7 passing
- [ ] Seeded review (Lesson 08) completed against `review/candidate_fix.py` via the four-question checklist — do not open the key first
- [ ] Transfer answer (item 7) naming which claims survive and which break, with the count-bounded mechanism traced by hand
- [ ] Operate signal (item 8) that carries a hashed key id and never the raw idempotency key or note content
