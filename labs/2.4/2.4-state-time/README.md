# Lab: 2.4-state-time

**Module:** `2.4`
**Authorized scope:** this directory only. Local FastAPI + SQLite fixture; no public or third-party targets, no live load testing.
**Invariant:** two requests carrying the same idempotency key — whether one retries the other after a timeout, or both are genuinely in flight at the same time — must produce exactly one committed `shares` row, and the endpoint must deny the action, not accept it, when its idempotency store is unreachable. Top 10 A10:2025 "Mishandling of Exceptional Conditions" is **awareness**, mapped only after this causal fix — not this lab's own outline.
**Root cause class:** state / time / concurrency (retry, TOCTOU race, fail-open on external-resource failure)
**Non-goals:** live race exploits against production, load-testing or race-condition tooling pointed at any third-party API, wall-clock attacks on NTP.

## Reset

`git checkout` restores tracked files. Each test also calls its variant's own `reset()`, which creates a fresh on-disk SQLite temp file per test — no state leaks between tests or between runs.

## Layout

- `vulnerable/app.py` — no idempotency check at all (every POST is a fresh `INSERT`), and fails open (`except sqlite3.Error: return {"accepted": True, ...}`) on any storage problem.
- `fixed/app.py` — a `UNIQUE` constraint on `idempotency_key` makes the check and the record one atomic operation the database enforces, and an outer `try/except` around the connection itself fails closed (`accepted: False`, nothing persisted) when the store cannot be reached.
- `review/candidate_fix.py` — a seeded, **not wired into pytest**, third variant for `lessons/08-review.md`'s reading exercise. Do not import or run it; findings live only in `content/assessment/keys/2.4.md`.
- `tests/test_idempotency.py` — seven tests: normal case, the module's headline forbidden outcome (sequential retry), a boundary (two distinct keys), a malformed/failure case (store unreachable), the central concurrency case (eight genuinely concurrent first-requests), and an anti-fake pair.
- `requirements.txt` — `fastapi`, `httpx` (for `fastapi.testclient.TestClient`).

## Impact

A duplicate row in `shares` is a second, unintended entry in the answer to "who has this note been shared with" — a real authority change nobody on the owner's side separately decided to make. The blast radius scales with how many times a client, proxy, or redelivering worker actually resends the same key.

## Structural fix

Push the check into the store: `idempotency_key TEXT UNIQUE`, and catch the resulting `sqlite3.IntegrityError` to return the *existing* row's outcome rather than a second insert. This is not the same as an application-level `SELECT`-then-`INSERT` ("Candidate A" in `lessons/04-build.md`), which is correct only for one call at a time and still duplicates under real concurrent access — the fixture's own concurrency test exists specifically to catch that difference. Fail-closed: any failure to open the store denies the action and persists nothing; a missing `Idempotency-Key` header still shares once per call, a declared leftover (production should require a key for a high-impact action like this one), not a claim this lab tests.

## Verify

```bash
python3 -m pytest tests --impl vulnerable   # 4 of 7 fail
python3 -m pytest tests --impl fixed        # 7 of 7 pass
```

Run only from inside this directory (or prefix the path from the repo root, `labs/2.4/2.4-state-time/tests`). Install `requirements.txt` first if `fastapi`/`httpx` are not already available.

## Operate

Log a `share_replay` event (hashed key id, note id, actor, request id — never the raw key or note content) on a detected duplicate-key hit. Alert on a rate against a baseline, not the first replay of the day. Never fail open if the key store is down or slow. See `lessons/06-operate.md` for the full signal shape and the containment/revocation/recovery steps for a share that already landed.

## Transfer

Clinic last slot, payment capture, or invite token (`lessons/07-transfer.md`): the retry and fail-closed claims survive the change to a count-bounded resource unchanged; the `UNIQUE`-constraint structural fix does not, and needs a maintained-count mechanism instead. Worker retry with a **stale** grant is named as a residual for 7.4, not solved here.
