# 2.4 — State, time, concurrency, and distributed failure

Pass A specification only.

## Identity

- **id:** 2.4
- **slug:** state-time-concurrency-distributed-failure
- **title:** State, time, concurrency, and distributed failure
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 330
- **prerequisites:** 2.1–2.3 Pass A; 1.2 complete mediation across time
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** M0
- **masteryGate:** 2

## Objective hierarchy

1. Model **session/state machines**: replay, freshness, idempotency, ordering, retry, timeout, clocks, locks, transactions, TOCTOU, races, partial failure.
2. Local fixture: a **retry or timeout** that duplicates a side effect or fail-opens.
3. Transfer: add a queue (preview of 7.4) and show which 1.2 cells need time/idempotency.

## Misconceptions

- Happy-path tests prove absence of races.
- Timeouts are only UX.
- Top 10 A10:2025 *is* the lesson (it is **awareness regression** for exceptional conditions).
- A sequential retry test proves the concurrent case is safe too.
- Databases are automatically idempotent.
- A lock closes a concurrency gap regardless of whether every caller shares the same lock object.

## Concept map

```text
Client retries or races -> idempotency key -> check-then-act (app) vs check-and-act (store)
  -> store reachable? -> no: fail closed | yes: one committed row per key
```

## Teaching claims

Five falsifiable claims, ordered by dependency. The interrupted authoring pass already wrote all eight lessons around this structure and even named three of the five (`C1`, `C3`, `C4`) directly in `lessons/07-transfer.md`, but never formalized any of the five here or built the coverage contract that makes them checkable — this section extracts what the lessons already teach rather than inventing new claims that would require rewriting them again.

1. **C1 — A retry carrying the same idempotency key must produce exactly one committed share row, and the replayed response must return the first attempt's own `share_id`, not merely a truthy success.** For SecureCollab's `share_note` endpoint, a client that times out and resends the identical `Idempotency-Key` — an honest retry, a doubled click, or a load balancer's own retry policy — must not add a second row to the `shares` table, and the second response has to name the same share the first one created, because an owner checking "who has this been shared with" needs to see the share that actually exists, not a fresh id nobody can trace back to it.
2. **C2 — Two or more requests carrying the same never-before-seen key that are genuinely in flight at the same time — not sequenced one after another — must also resolve to exactly one committed row, and a sequential-retry test cannot exercise this case because its two calls never overlap in time.** A check-then-act implementation (`SELECT` to see whether the key exists, then `INSERT` if not) passes every test that calls the handler strictly one call after another, and still lets two concurrent calls both observe "not found" before either call's insert has run, producing the exact duplicate C1 forbids while looking, one call at a time, exactly like a correct fix.
3. **C3 — When the idempotency store cannot be reached, the share endpoint must deny the action rather than report success, and fail-closed is a property of how the system responds to its own uncertainty, not a property that depends on which resource is being protected.** A handler that returns `accepted: false` while some other code path still executes the insert has not failed closed; both halves of the claim — deny, and record nothing — have to hold together, or the fix has only changed what the response claims, not what the store actually contains.
4. **C4 — The structural fix is to make the check and the record the same atomic operation the storage engine enforces (a database uniqueness constraint), not two separate application-level statements sequenced by hand; this fix generalizes to any uniqueness-bounded resource but not to a count-bounded one.** A `UNIQUE` constraint answers "does a row with this exact value already exist," which a limited-quantity resource — a clinic's last appointment slot, a note's capped number of pending invites — does not reduce to, because admitting the *second, distinct* value once a cap is reached needs a maintained count checked and incremented inside one atomic transaction, not a bare uniqueness column. A lock is not a substitute for this: a lock object created fresh inside the handler (as in `labs/2.4/2.4-state-time/review/candidate_fix.py`) protects nothing, because no other call ever contends for it, and even a correctly *shared* lock only serializes callers inside one process — it does nothing for two separate `uvicorn` worker processes, which is the default condition for any deployment this course assumes.
5. **C5 — Guaranteeing exactly one committed row per key resolves the row-count invariant; it does not by itself guarantee the authority behind that key is still valid at the moment the request is finally acted on.** A worker that redelivers a share job after the underlying grant has since been revoked between when the job was enqueued and when it runs passes every test in this module's suite — the row count is still exactly one — while acting on authority the system has already withdrawn. This module names that gap as an explicit residual it does not close, not a case its fixture happens to cover.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 5 Verify | `test_single_share_with_a_key`, `test_retry_with_the_same_key_does_not_duplicate`, `test_two_different_keys_are_two_shares`, `test_a_never_elsewhere_used_key_is_still_deduplicated` | items.md #1 |
| C2 | 1 Property, 2 Model, 3 Break, 5 Verify | `test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share` (eight requests genuinely in flight, the case a sequential retry test cannot exercise) | items.md #1, #4 |
| C3 | 1 Property, 5 Verify, 6 Operate | `test_store_unreachable_is_denied_not_accepted` | items.md #2, #3, #8 |
| C4 | 4 Build, 5 Verify, 7 Generalize, 8 Review | Not one dedicated assertion — exercised by the full vulnerable/fixed contrast (every C2/C3 test the fixed variant passes depends on the `UNIQUE` constraint being the mechanism) and by `08-review`'s seeded finding that `candidate_fix.py`'s per-call `threading.Lock()` is a failed attempt at exactly this claim | items.md #4, #5, #6 |
| C5 | 1 Property, 2 Model, 5 Verify, 7 Generalize | Not directly code-testable — no queue or worker exists in this Tier-2 fixture. Modeled in `lessons/01-property.md`'s closing residual, `lessons/02-model.md`'s "What can still go wrong," and `lessons/05-verify.md`'s "What a fully green suite still does not prove." | items.md #7, #8 |

C1, C2, and C3 carry genuine lab assertions, well past the ≥2-claims bar. C4 is exercised indirectly (the mechanism the passing suite depends on, plus a seeded review finding) rather than by one dedicated test, and is honestly declared that way rather than mapped to a fabricated assertion. C5 is honestly declared non-code-testable: it requires a second actor (a queue or worker) this fixture does not have, and is picked up where it belongs, in [7.4 Queues, workers, events, and service identity](../../7/7.4/lessons/01-property.md).

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| State the property a retry must satisfy and name the check-then-act structure that still fails under real concurrent access even when it passes a sequential retry test | C1, C2 | `lessons/01-property.md` §The property | `lessons/01-property.md` §A worked trace, and a counterexample that looks almost identical | `lessons/01-property.md` practice; `lessons/04-build.md` Candidate A prediction exercise | items.md #1, #4 | `lessons/07-transfer.md` |
| Produce a state machine for the SecureCollab share workflow naming which transitions a retry, a race, and a key-store failure each take | C1, C2, C3 | `lessons/02-model.md` §Picture: states, and which transitions are the same event twice | `lessons/02-model.md` worked trace against the vulnerable fixture | `lessons/02-model.md` practice (draw the machine before opening the picture) | items.md #1 | `lessons/07-transfer.md` |
| On the local FastAPI/SQLite fixture, show both a sequential retry and eight genuinely concurrent first-requests failing to duplicate a share | C1, C2 | `lessons/03-break.md` §Where authority actually goes wrong | `lessons/05-verify.md` §Abuse case: eight requests that are actually in flight at once | `labs/2.4/2.4-state-time` `pytest tests --impl vulnerable\|fixed` | items.md #4 | `lessons/07-transfer.md` |
| On the same fixture, show the share endpoint denying rather than accepting a request when its idempotency store is unreachable | C3 | `lessons/01-property.md` §What must be trusted | `lessons/05-verify.md` §Failure case: the store is unreachable | `labs/2.4/2.4-state-time` `test_store_unreachable_is_denied_not_accepted` | items.md #2, #3, #8 | `lessons/07-transfer.md` |
| Treat OWASP Top 10:2025 A10 as a regression check applied after the causal fix, not as the lesson's own structure | C3 | `lessons/06-operate.md` §Signal design | `lessons/06-operate.md` fail-closed operate example | `lessons/08-review.md` four-question checklist | items.md #3 | `lessons/07-transfer.md` |
| Transfer the retry, race, and fail-closed reasoning to a different limited resource and state which claims survive the change unchanged and which do not | C1–C5 | `lessons/07-transfer.md` §Which claims survive unchanged, and why | `lessons/07-transfer.md` naive count-check trace | `lessons/07-transfer.md` write-up prompts | items.md #6, #7 | (is the transfer task) |

## Known residuals

Genuinely out of scope for this module, with the module that picks each one up:

- A worker that redelivers a share job after the underlying grant has since been revoked (C5) → [7.4 Queues, workers, events, and service identity](../../7/7.4/lessons/01-property.md)
- A count-bounded resource (a limited number of appointment slots, a capped number of pending invites) needing a maintained-counter mechanism rather than a bare uniqueness constraint (C4's limit) → transfer exercise in `lessons/07-transfer.md`; a lab-tested treatment belongs to whichever module owns that concrete resource (Elective E3 for payment capture; 6.6 for invite tokens)
- Two entirely different idempotency keys minted by mistake for what a human considers one intention — nothing in this system can observe that mistake from the outside; named in `lessons/02-model.md` as client-side key-generation discipline, out of this module's scope
- Production connection pooling, a real load balancer's retry policy, and a managed high-availability database cluster are not modeled by this local fixture; named as a limit of what a green suite proves in `lessons/05-verify.md`

## Invariant prompts

- What must remain true of the `shares` table after any combination of a retry, a race, and a store failure has happened?
- What has to be trusted for the retry claim, and does that list change for the fail-closed claim?
- Is the mechanism that closes this gap a network boundary, a process boundary, or a single function call to one library?

## Threat-model prompts

- What happens on retry, timeout, or partial commit?
- Whose clock is trusted for freshness?
- Can authorization become stale between check and use?
- Can two requests that each look like the first request actually be in flight at the same time?
- Is a proposed lock actually contended, or does every caller construct its own?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.4-LO-01 | concept-model | A retry is a second attempt, not a second grant | 1 Property |
| 2.4-LO-02 | design-exercise | A share state machine that names retry, race, and store failure | 2 Model |
| 2.4-LO-03 | mechanism-lab | Local fixture: a retry duplicates a share on a real request cycle | 3 Break |
| 2.4-LO-04 | design-exercise | Push the check into the store; do not check-then-act in the handler | 4 Build |
| 2.4-LO-05 | verification-lab | A test that holds eight requests in flight, not two in sequence | 5 Verify |
| 2.4-LO-06 | operations-exercise | Detect a replay or a race; never fail open the key store | 6 Operate |
| 2.4-LO-07 | transfer-challenge | Transfer: clinic last slot, payment capture, or invite token | 7 Generalize |
| 2.4-LO-08 | code-review | Seeded review of a check-then-insert share fix | 5 Verify (Review) |

## Lab briefs

**Lab `2.4-state-time`:** local FastAPI + SQLite component fixture (Tier 2), authorized scope `labs/2.4/2.4-state-time/` only. Forbidden outcomes: a retry duplicates a share; eight genuinely concurrent first-requests for one never-seen key duplicate a share; the endpoint reports success while its store is unreachable and nothing was recorded. Forbidden practice: load-testing or race-condition tooling pointed at any third-party API. `review/candidate_fix.py` is a seeded, not-wired-in reading exercise for `lessons/08-review.md`, not a test target.

## Assessment blueprint

See `module.yaml` `assessmentBlueprint`. `content/modules/2/2.4/assessment/items.md` (8 items) and the isolated key `content/assessment/keys/2.4.md` carry the graded evidence; the rubric no longer points at a "session worksheet."

## Standards references

OWASP ASVS 5.0.0 (final), live-checked against the canonical `v5.0.0` requirements JSON on 2026-09-22; exact requirement text recorded in `content/standards/pins.yaml` and in the `**Standards:**` lines of `lessons/01-property.md` and `lessons/05-verify.md`.

- `v5.0.0-2.3.3` — business-logic transactions succeed entirely or roll back. C1.
- `v5.0.0-2.3.4` — business-logic locking so a limited-quantity resource cannot be double-booked by manipulating application logic. C4's limit (count-bounded resources); anchors `lessons/07-transfer.md`'s clinic scenario directly.
- `v5.0.0-15.4.1` (Level 3, advanced) — thread-safe access to shared objects, avoiding race conditions. C2.
- `v5.0.0-15.4.2` (Level 3, advanced) — a resource's state check and the action that depends on it are performed as a single atomic operation, preventing TOCTOU race conditions. C2, C4.
- `v5.0.0-15.4.3` (Level 3, advanced) — locks used consistently and not modifiable by external code. C4 (the reason `candidate_fix.py`'s per-call lock is a seeded defect, not a partial fix).
- `v5.0.0-16.5.2` — continue operating securely when external resource access fails, e.g. circuit breakers or graceful degradation. C3.
- `v5.0.0-16.5.3` — fail gracefully and securely, explicitly naming "preventing fail-open conditions such as processing a transaction despite errors" as its own example. C3.

IETF RFC 9110 (Standards Track), §9.2.2 and §9.3.3: POST is defined not-idempotent; `post-not-idempotent` in `standardsRefs`. C1, C2.

OWASP Top 10:2025 A10 "Mishandling of Exceptional Conditions" (`status: awareness`): mapped only after the retry/concurrency/fail-closed causal mechanism, never as the module's own structure. C3.

Level 3 items above are labeled advanced, not a Level 2 completion requirement. Do not mix ASVS 4.x identifiers or obsolete MASVS L1/L2/R levels into this module.

## Review triggers

New async path; timeout or retry policy change; clock source change; idempotency-store or database technology change (see `module.yaml` `reviewTriggers`).

## Time budget and SecureCollab

~330 min, recomputed from the rewritten lessons' word count, the Tier-2 lab, and the 8-item assessment per the `metadata-honesty.mdc` formula. Evidence: state-machine model, concurrency/replay/fail-closed test list, fail-closed decision tested on the fixture. Feeds Gate 2 alongside 2.1–2.3.

## Operational considerations

`share_replay reason=duplicate_idempotency_key note_id=<id> key_id=sha256:<hash> actor=<id> request_id=<id>` — a hashed key, never the raw key or note content. Alert on a rate against a baseline, not the first replay of the day. Never fail-open if the key store is down (`v5.0.0-16.5.3`). See `lessons/06-operate.md` for containment/revocation/recovery steps.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-09-23 | Deepen (continuing an interrupted pass): wrote this file's teaching claims (C1–C5) and coverage contract, which the earlier session had left unwritten even though the eight lessons it rewrote already taught this structure and named three of the five claims directly in `lessons/07-transfer.md`. Synced the stale Identity/Lesson-inventory/Standards-references/Lab-briefs sections in this file to what `module.yaml` and the lessons already stated. See `module.yaml` changelog for the full pass, including the lab bug found and the standards re-verification. |
