# Transfer: clinic last slot, payment capture, or invite token

**Kind:** transfer-challenge
**Loop step:** 7 Generalize

## The change that actually matters here

Swapping "share a note" for "book a clinic appointment" while keeping every other assumption fixed would be a rename, not a transfer — the interesting version of this exercise changes the *asset* from a boolean fact (has this exact key been seen, yes or no) to a bounded quantity (how many appointments has this clinic sold for this time slot, and is the count still under the cap). That is a change to what has to be checked, not merely to the noun describing what gets checked, and `04-build.md` already flagged it: Candidate B's uniqueness constraint answers "does a row with this value exist" by construction, and a clinic's last-slot problem is not that question. Work through this transfer with that distinction in view rather than assuming the note-sharing fix ports over unchanged.

## What SecureCollab's asset was, and what the clinic's asset is

In this module's fixture, the protected fact is "has idempotency key `k1` already produced a share row for note `n1`" — a yes-or-no question about one specific value, answerable by a single uniqueness constraint on one column. A clinic selling appointment slots protects a different fact: "has this slot already reached its capacity of one (or, for a group session, of N) booked patients." Two different idempotency keys — two different patients, each retrying honestly after their own network timeout — are not the same request being duplicated; they are two *legitimately distinct* requests competing for one scarce resource, and the system has to admit exactly one of them (or exactly N of them) rather than treat every request after the first as a replay of an earlier one.

## Which claims survive unchanged, and why

C1 — a retry with the same idempotency key must not duplicate a booking — survives the change completely unchanged, for the same reason a payment capture's `test_retry_with_the_same_key_does_not_duplicate` analogue would: this is still a pure uniqueness question about *one patient's own attempt*, independent of how many other patients exist. A `UNIQUE` constraint on `(patient_id, appointment_request_key)` closes it exactly the way `04-build.md`'s Candidate B closes the note-sharing case, because nothing about capacity enters into "did this specific patient's specific request get recorded twice."

C3 — the booking service must fail closed, not accept a booking "just this once," when its store is unreachable — also survives unchanged, and for a reason worth stating plainly: fail-closed is a property of how a system responds to *its own* uncertainty about the world, not a property that depends on what resource is being protected. Whether the store cannot answer "has this key been seen" or cannot answer "how many slots remain," the correct response to not knowing is the same: refuse, do not guess in the direction of granting access.

## Which claim breaks, and what has to replace it

C4 — this module's structural fix, a uniqueness constraint enforced by the database's write-serialization — does *not* survive the change, and this is the part of the transfer worth the most care. A uniqueness constraint on `(appointment_id)` alone would correctly stop the *same patient* from booking the same slot twice, but it says nothing about whether a *second, different* patient's booking should be admitted once the slot is full; uniqueness answers "is this exact value already present," not "have we already admitted as many distinct values as we are allowed to." The count-bounded version needs a different mechanism: either a maintained counter column checked and incremented inside one atomic transaction under a serializable isolation level (so two concurrent bookings against a slot with one seat remaining cannot both read "0 booked" before either writes), or a database-level check constraint that rejects any insert which would push a maintained count past its cap. ASVS v5.0.0-2.3.4 names this exact requirement directly: "business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application's logic" — the standard's own example is a delivery slot, which is this scenario almost exactly, not a coincidence of phrasing but a sign that this failure shape recurs often enough to earn its own line item.

Tracing the naive count-check by hand makes the gap concrete rather than asserted:

```text
patient A: SELECT COUNT(*) WHERE slot=S9  -> 0 booked, cap is 1 -> proceeds
patient B: SELECT COUNT(*) WHERE slot=S9  -> 0 booked, cap is 1 -> proceeds
patient A: INSERT booking (slot=S9)        -> succeeds, now 1 booked
patient B: INSERT booking (slot=S9)        -> no constraint stops this -> succeeds, now 2 booked
```

Both patients' `SELECT COUNT(*)` steps ran before either patient's `INSERT` had committed, so both observed "zero booked" and both proceeded — the identical shape `04-build.md` traced for Candidate A, with "has this key been seen" replaced by "how many rows currently match this slot." A bare uniqueness constraint on `slot_id` would prevent a *third* booking attempt from ever landing, but it does nothing to stop this second one, because uniqueness on the slot column alone would have rejected patient A's own booking too, once one row for `slot=S9` already existed — it cannot distinguish "the first booking for this slot" from "the second, over-capacity booking for this slot," which is exactly the distinction a count-bounded resource needs and a plain uniqueness constraint cannot express.

## Why a modern-sounding stack is not the right kind of answer here

A tempting shortcut when transferring a concurrency claim to a new surface is to reach for whatever the newest or most sophisticated-sounding technology detail is and assume its sophistication implies safety — reasoning by association with the impressive term rather than by tracing the actual mechanism. This module's own residual should be resisted the same way: a clinic's booking API being built on a modern framework, using a well-regarded ORM, or running on a managed, highly-available database cluster says nothing by itself about whether the *specific write path* for admitting a booking against a capacity limit was built with a serializable transaction or a check constraint, versus a `SELECT COUNT(*)` followed by a separate `INSERT` that Candidate A's exact gap reopens. The mechanism has to be traced, the same way `04-build.md` traced Candidate A and Candidate B by hand, rather than inferred from how modern the surrounding stack sounds.

## Success criteria

A complete transfer answer states, for each of this module's teaching claims, whether it survives the change from a uniqueness-bounded asset to a count-bounded one and names the specific mechanism difference that explains the answer — not merely "yes" or "no." It identifies that the clinic scenario needs a maintained-count mechanism rather than a bare uniqueness constraint, and it can trace, by hand, what a naive `SELECT COUNT(*)`-then-`INSERT` implementation of the count check would do against two patients racing for the clinic's last slot, using the identical tracing method `04-build.md` applied to Candidate A. It does not require writing or running any code against a real clinic, payment processor, or invite-token service; the exercise is the reasoning, performed on paper against a hypothetical schema, not a build task.

## What this page is not doing

This is a design exercise, not an integration with any real clinic scheduling system, payment processor, or invite-token service; do not attempt any of this reasoning against a live third-party booking page, a payment sandbox you do not own, or a public invite-redemption API.
