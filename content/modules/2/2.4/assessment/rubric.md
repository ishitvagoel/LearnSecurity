# 2.4 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another.

## Module

State, time, concurrency, and distributed failure — five teaching claims (C1–C5), named in `spec.md` §Teaching claims: a retry must not duplicate a share (C1), a genuinely concurrent race must not duplicate a share either, and a sequential test cannot show this (C2), the store must fail closed when unreachable (C3), the structural fix is one atomic check-and-record operation that generalizes to uniqueness-bounded resources but not count-bounded ones (C4), and resolving row-count-once does not by itself guarantee the authority behind the key is still valid at time of use (C5, a named residual).

## Evidence checklist

- [ ] State machine (Lesson 02) for the SecureCollab share workflow naming the transitions a sequential retry, a genuine race, and a key-store failure each take, including the `Denied` state's own recovery edge
- [ ] Local reproduction of this module's forbidden outcomes (Lesson 03): a retry duplicating a share, and — via the lab's genuinely concurrent test — a race duplicating one
- [ ] Lab `labs/2.4/2.4-state-time`: `vulnerable/` tests show 4 of 7 failing for the stated security reasons (no idempotency check at all; fail-open on any storage error); `fixed/` tests show 7 of 7 passing
- [ ] Assessment items (`content/modules/2/2.4/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Seeded review (Lesson 08) completed against `review/candidate_fix.py` via the four-question reading order — do not open the key first
- [ ] Operate signal (Lesson 06) for a duplicate-key replay that carries a hashed key id and request id, never the raw key or note content, plus containment/revocation/recovery steps for a share that did land
- [ ] Transfer task (Lesson 07) naming which of this module's claims survive a change from a uniqueness-bounded asset (the idempotency key) to a count-bounded one (the clinic's last slot), and which do not, with the mechanism difference traced by hand

## Rubric

| Result | Meaning |
|---|---|
| Developing | Names only the sequential-retry claim (C1) without the concurrency claim (C2) or the fail-closed claim (C3); accepts a lock, a database's general reputation, or an SLA as evidence for a specific claim without checking what it actually guarantees; missing forbidden-outcome lab evidence for the concurrent case |
| Competent | States C1–C4 as system-specific properties of SecureCollab's `share_note` workflow, not tool names; reproduces both the sequential and the concurrent forbidden outcome on the lab and maps each to the claim it tests; correctly distinguishes a lock's scope (uncontended, in-process, cross-process) from the database-level mechanism that actually closes the gap |
| Transfer-ready | Lesson 07's transfer task completed, correctly naming C4 as the claim that breaks for a count-bounded resource and tracing the two-request race that breaks it, without Top 10/scanner language standing in for any of C1–C5 |

Knowledge check (retryable, 80% threshold): the eight module-specific items in `content/modules/2/2.4/assessment/items.md`.

## Seeded review

Use the local `review/candidate_fix.py` artifact via Lesson 08's four-question reading order. Intended findings and banding live only in `content/assessment/keys/2.4.md`.
