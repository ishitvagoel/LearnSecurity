# A test that holds eight requests in flight, not two in sequence

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** OWASP ASVS 5.0.0 v5.0.0-15.4.1, v5.0.0-15.4.2, v5.0.0-16.5.3 (final, Level 3 items labeled advanced).

## What one passing test proves, and what it does not

A single call to `share_note` that returns `accepted: true` proves the happy path exists; it proves nothing about the module's property, because the property is a statement about *two* requests, not one. `test_single_share_with_a_key` in `tests/test_idempotency.py` is the normal case, and passing it is a precondition for everything else in this file mattering at all — a handler that cannot even record one share correctly has no duplicate-prevention claim worth checking. The next six tests each exist to close one specific way "the tests pass" could be true for the wrong reason.

## Negative and boundary: same key twice, different keys twice

`test_retry_with_the_same_key_does_not_duplicate` is the module's headline forbidden outcome: two sequential calls with `k1` must leave exactly one row, and the second call's returned `share_id` must equal the first call's, not merely report success independently. That second assertion is deliberate — a fix that returns `accepted: true` on replay while quietly minting a fresh row under a different id would still say the right word without doing the right thing, and an assertion that only checked the word would pass for the wrong reason. `test_two_different_keys_are_two_shares` is the boundary case this module's earlier version never wrote: a fix that denies *every* repeated request, key or not, would also pass the retry test by accident, so this second test exists specifically to confirm that two distinct, legitimate keys are not conflated with a repeated one. A checker that always refuses is exactly as broken as one that never checks, and only a boundary test naming both failure directions can tell them apart.

## Abuse case: eight requests that are actually in flight at once

`test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share` is this lesson's central case, and it exists because of a fact worth stating plainly: **a sequential retry test cannot exercise a race, because its two calls never overlap in time.** The test fires eight HTTP requests at the same never-before-used key from eight threads, each holding its own client against the same running application object, and then asserts that exactly one row exists afterward. The oracle here is the database's own write-serialization, not anything the test controls directly — the test cannot force a particular thread to "win," and it does not need to, because the property under test is that *whichever* thread wins, the other seven must resolve to that winner's row rather than each minting their own. This is the specific gap ASVS v5.0.0-15.4.2 names directly: "checks on a resource's state... and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions" — Candidate A in `04-build.md` is exactly a check and an action that are *not* one atomic operation, and this test is what "prevent" means made executable rather than asserted in prose.

## Failure case: the store is unreachable

`test_store_unreachable_is_denied_not_accepted` points the fixture at a database path that cannot be opened and asserts two things: that the response reports `accepted: false`, and that nothing was recorded once the real path is restored. Both assertions matter for a reason worth spelling out, because a fix that gets only the first one right has not actually fixed anything — a handler that returns `accepted: false` while still executing an insert against some other code path has not failed closed, it has failed to tell the truth about what it did. ASVS v5.0.0-16.5.3 requires exactly this: failing "gracefully and securely... preventing fail-open conditions such as processing a transaction despite errors" — and the requirement's own example is close enough to this module's forbidden outcome that no interpretation is needed to see the connection.

## The anti-fake test, and the fake it was built to catch

`test_a_never_elsewhere_used_key_is_still_deduplicated` constructs a note id (`zz9`) and a key (`unseen-elsewhere-7f3`) that appear nowhere else in the test file, specifically so that a fix which special-cases the exact strings `n1` and `k1` — the values every other test happens to use — cannot pass by having memorized them rather than implemented the general check. This module's authoring pass constructed exactly such a fake to confirm the anti-fake test earns its name rather than merely asserting that it does: a variant of `fixed/app.py` that used Candidate A's check-then-act shape (no `UNIQUE` constraint, a `SELECT` followed by an `INSERT`) passed `test_single_share_with_a_key`, `test_retry_with_the_same_key_does_not_duplicate`, `test_two_different_keys_are_two_shares`, `test_missing_key_shares_once_per_call`, and this anti-fake test — five of seven — while failing `test_store_unreachable_is_denied_not_accepted` (it never implemented a fail-closed path at all) and, decisively, `test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share`, which recorded eight rows instead of one. A fake that passes five of seven tests, including the sequential retry test that a shallower suite would treat as sufficient, is precisely the failure mode this lesson's opening paragraph warns about: the concurrency test is not a redundant restatement of the retry test, it is the one assertion in this file that a plausible, competently-written, wrong fix cannot pass.

## What a fully green suite still does not prove

Seven passing tests prove that this specific fixture, on this specific machine, resolved eight genuinely concurrent requests and one unreachable-store request correctly. They do not prove that a production deployment's connection pool, retry middleware, or a load balancer's own automatic-retry policy behaves the same way; they do not prove anything about a worker that redelivers a share job after the underlying grant has since been revoked, which `01-property.md` names as an explicit residual rather than a tested claim; and they do not prove that two entirely different idempotency keys were never minted by mistake for what a human considered one intention, since nothing in this system can observe that mistake from the outside. A green suite is evidence for exactly the claims its assertions state, not a general certificate of correctness — the same discipline [1.3 Trust boundaries and attack surface](../../../1/1.3/lessons/01-property.md) teaches by insisting that "what you trust" always names the specific rule it is trusted for.

There is a sharper limit worth naming on its own, because it is easy to miss precisely by passing this suite: `test_concurrent_first_requests_with_a_never_seen_key_still_produce_one_share` fires eight threads at a single `impl.app` object inside one Python process, so it can only ever tell apart "this call is atomic" from "this call is not atomic *within one process*." A correctly module-level-shared `threading.Lock()` — genuinely one lock object, constructed once, contended by every thread — would close this exact race and pass this exact test, for the same reason the real fix does: both serialize the eight threads this test happens to spawn. C4's claim that a shared lock "does nothing for two separate `uvicorn` worker processes" is true, and is the entire reason production code needs the database to enforce the constraint rather than a lock in application memory — but this lab's suite does not and structurally cannot test that half of the claim, because standing up two real OS processes against the same on-disk database is outside what this Tier-2 fixture builds. Treat the cross-process half of C4 as verified by argument, not by this suite's green result, the same way C5 is verified by argument rather than by a test that does not exist.

## Practice

```bash
python3 -m pytest labs/2.4/2.4-state-time/tests --impl vulnerable   # 4 of 7 fail
python3 -m pytest labs/2.4/2.4-state-time/tests --impl fixed        # 7 of 7 pass
```

Run this only inside `labs/2.4/2.4-state-time/`; do not point any of these tests, or the concurrency-testing pattern they demonstrate, at a system this course does not own.

## Use it somewhere new

The same distinction — a sequential test proves one thing, a concurrent test proves another, and neither one substitutes for the other — applies unchanged to a payment capture service's test suite and to a limited-slot booking service's test suite, whatever language or database engine either one is written against.
