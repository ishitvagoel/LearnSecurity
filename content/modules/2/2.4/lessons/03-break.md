# Local fixture: a retry duplicates a share on a real request cycle

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Starting from the handler, not from a bug name

Open `vulnerable/app.py` and read the single route it defines before reading anything below this paragraph, because the point of this lesson is to derive the failure from the code rather than to be handed a label and asked to confirm it. The handler accepts a note id in the URL path and an optional `Idempotency-Key` header, opens a connection to a SQLite file, and runs one statement: `INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)`. Nothing about that statement, or anything around it, ever reads the `shares` table before writing to it. There is no `SELECT`, no lookup, no branch on whether the incoming key has been seen. The precondition for the module's forbidden outcome is therefore not some exotic timing window at all — it is satisfied by the simplest possible sequence: one request, followed by a second request carrying the identical `Idempotency-Key` value.

Trace what happens to that second request. It arrives at the same route, with the same note id and the same header value as the first. The handler does not know, and cannot know from anything in its own code, that this request is "the same attempt" rather than "the fourth of ten independent shares this owner happens to be making today." It runs the identical `INSERT`, a second row is appended, and the response reports `accepted: true` exactly as the first response did — from the client's point of view, both requests look equally successful, and nothing in either response reveals that the share table now disagrees with the client's intention.

## Where authority actually goes wrong

The share table is what the who-may-read-this-note check consults later, whenever a company or a note viewer asks "who has this been shared with." A second row for `n1` is not a cosmetic bookkeeping error; it is a second entry in the answer to that authority question, meaning a second recipient — if this fixture modeled a distinct recipient per share rather than a bare count — would gain read access nobody on the owner's side ever separately decided to grant. The blast radius of this specific defect is bounded by how many times a client, a proxy, or a redelivering worker actually resends the same key, which in a real deployment is bounded by retry-policy configuration rather than by anything the handler itself limits; a load balancer configured to retry a POST up to three times on a 504 could, against this handler, turn one intended share into three recorded ones, each indistinguishable from a distinct, deliberate grant to whoever later reads the `shares` table.

## What the failing test tells you, and what it does not

Run this only inside `labs/2.4/2.4-state-time/`; the note ids and keys below are fixture labels, not real content.

```bash
python3 -m pytest labs/2.4/2.4-state-time/tests --impl vulnerable
```

Four of the seven tests fail against this file: `test_retry_with_the_same_key_does_not_duplicate`, `test_store_unreachable_is_denied_not_accepted`, `test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share`, and `test_a_never_elsewhere_used_key_is_still_deduplicated`. The first failure is the direct consequence of the missing `SELECT`, described above. The second and third fail for a different, additional reason worth naming precisely rather than lumping in as "more of the same bug": `vulnerable/app.py` also wraps its insert in a broad exception handler that reports `accepted: true` even when the database connection itself cannot be opened, which is a second, independent decision — fail open on any storage problem — layered on top of the first. A single test failing tells you one check is missing; four tests failing for two distinct, nameable reasons tells you the handler was never designed around the property at all, which is the more useful and more honest diagnosis. The fourth failing test is the anti-fake pair's dedup half, and it fails for the identical reason as the first — it exists to confirm that a fix cannot pass by memorizing the specific note id and key string the other tests happen to use, not to test a different mechanism.

## Why this is the smallest fixture, not a simplified one

A representative failure earns that description by leaving out everything that does not change *why* the bug occurs, and this fixture leaves out a great deal on purpose. It has no authentication, because who is allowed to call this endpoint is a separate question from whether the endpoint remembers a key it has already seen; adding a login flow would not change the missing `SELECT`. It has no note content beyond an id string, because the defect is about row count, not about what a note contains; a fixture that stored real paragraph text would test the exact same INSERT-on-every-call defect while adding nothing to the reasoning and everything to the risk of accidentally treating fixture strings as sensitive data. It uses a real FastAPI request cycle and a real SQLite file specifically because a bare Python function call — the shape this lab used before this pass — cannot exhibit the concurrency failure at all: a pure function has no connection object, no write-serialization, and nothing a database engine could enforce atomically, so a fixture that stayed at that level could only ever test the sequential-retry half of this module's property and would have to leave the race half as an unverified assertion in prose.

## Practice

Run the vulnerable variant, read the failure output for all four failing tests, and for each one write one sentence connecting the assertion that failed to the specific line in `vulnerable/app.py` that makes it fail — not to the test's name, and not to a general description of "duplicate shares." Then read [`04-build.md`](04-build.md), which derives the fix from the same trace this lesson just walked through, rather than presenting it as a finished answer.

## Use it somewhere new

The identical trace applies to a payment capture endpoint that never checks whether a capture id has already been processed, and to a clinic booking endpoint that never checks whether a slot has already been taken — in both cases, the precondition is "one request, followed by a second request an application-level check never looked at," and the blast radius is bounded by how many times the client or its infrastructure resends the request. [`07-transfer.md`](07-transfer.md) develops one of these in more depth.

## What this page is not doing

This fixture is not a payment system, a booking system, or a demonstration against any service outside `labs/2.4/2.4-state-time/`. Do not point retry logic, load-testing tools, or scripted double-submits at any system other than this local fixture, and do not treat the note ids and key strings used here as anything other than disposable labels.
