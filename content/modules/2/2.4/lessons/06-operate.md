# Detect a replay or a race; never fail open the key store

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing the code once does not retire this lesson

`04-build.md`'s database-enforced uniqueness constraint closes the defect this module teaches, but it does not make the failure disappear from production traffic — it changes what happens when the failure is attempted, from "a silent second grant" to "a rejected write the application now has to notice and respond to." A client that mints a fresh key on every retry instead of reusing one, an idempotency key with a lifetime configured shorter than a slow network's actual round-trip time, or a genuine outage of the idempotency store itself can all still produce the underlying *event* — two attempts at the same action — even after the code that resolves it correctly is deployed. Operating this system means deciding what becomes visible when that event happens, and what must never become visible no matter how useful it would be for debugging.

## Signal design: what the line carries, and what it must not

```text
share_replay reason=duplicate_idempotency_key note_id=n1 key_id=sha256:7f3a91 actor=owner_a request_id=req_22c1
```

Four fields make this line useful to whoever reads it later: `note_id` says which share workflow was affected, `actor` says whose action this was, `request_id` ties the line back to a specific HTTP request in the access log for correlation, and `key_id` — deliberately a hash of the idempotency key, not the raw key — lets an operator confirm two log lines refer to the same replayed attempt without the log itself becoming a second place a sensitive value is stored. The field this line does not carry, on purpose, is the note's content: nothing about diagnosing a duplicate-share event requires knowing what the note said, and a logging pipeline that captures request bodies "just in case" for debugging turns every idempotency-replay investigation into an incidental second exposure of exactly the content the sharing feature is supposed to be protecting. ASVS v5.0.0-16.5.2 asks that a system "continue to operate securely when external resource access fails, for example, by using patterns such as circuit breakers or graceful degradation" — logging the replay event and returning the first outcome, rather than either silently succeeding or crashing, is what graceful degradation means concretely for this specific workflow.

## What is a signal, and what is noise

A single `share_replay` line is expected traffic, not an incident, because ordinary network conditions produce ordinary retries constantly; a client behind a flaky mobile connection retrying one share attempt twice in an afternoon is the system working as designed, not evidence of anything wrong. The threshold that turns this signal into something worth a human's attention is a *rate* against a baseline, not a raw count: a sudden spike in `share_replay` events for one `actor`, or a sustained rate increase across the whole fleet that correlates with a deploy or an idempotency-store version change, is the shape worth paging someone over. Setting the threshold too low — alerting on the first replay of the day — trains whoever receives the page to stop reading it, which is a worse outcome than no alert at all, because an alert channel everyone has learned to ignore provides no more security than having no alert channel; setting it too high risks missing the case where a client bug has started minting a fresh key on every single retry, defeating the entire mechanism by construction while never triggering a single duplicate-key event for the store to log, since every "duplicate" now looks like a first attempt with a new key.

## Containment, revocation, and recovery

If a duplicate share did land — because it happened before this pass's fix was deployed, or because a future regression reopens the check-then-act gap — the recovery path is not "wait for the next deploy." It has to (1) identify every extra row for the affected note by comparing row count against distinct actual client intentions where that is knowable, (2) revoke the extra share the same way any other over-broad grant is revoked, through the module's own removal path rather than a direct database edit that leaves no record, and (3) tell the owner what happened and what was corrected, because a note owner who never learns their note was over-shared cannot judge for themselves whether anything sensitive reached the extra recipient before the correction. None of this recovery path depends on knowing *why* the duplicate happened; the same three steps apply whether the cause was the fixed defect resurfacing, a client bug, or an operator's own manual data-repair script run without going through the application at all.

## Accessible status, still governed by the same rule

A share workflow that shows a "still working" status message while a slow request is in flight has to meet [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 4.1.3 (Status Messages, Level AA): the status has to be programmatically determinable so that assistive technology can announce it without the user's focus needing to move to it, because a sighted user watching a spinner and a screen-reader user with no equivalent announcement are not equally informed about whether their share attempt has succeeded, is still pending, or needs to be retried. This accessibility requirement and this module's security property meet at exactly one point worth naming explicitly: if that "still working" status is implemented by re-sending the share request while the first one is still outstanding, the retry it issues has to carry the *same* idempotency key as the original attempt, not a freshly minted one — otherwise the interface built to keep a slow-connection user informed is the same interface that defeats the deduplication this entire module is about, for precisely the users a flaky connection makes retry most often.

## Residual: what happens when nobody reads the alert

Every detection path in this lesson assumes a human eventually looks at the `share_replay` signal, and that assumption is itself a residual risk worth naming rather than hiding behind the word "monitoring." An alert with no owner, a dashboard nobody has checked in a month, or an on-call rotation with no runbook for this specific signal all produce the identical operational outcome as having built no detection at all — the code recorded the event correctly, and no one acted on it. This module's Build and Verify lessons can guarantee the mechanism is correct; they cannot guarantee an organization staffs and reads its own alerting, and treating a shipped log line as equivalent to a monitored, owned, and runbooked signal is exactly the gap between "we log it" and "we recover from it" that a real incident finds.

## Use it somewhere new

A payment-capture service's replay signal needs the same shape — a hashed capture-key identifier, a request id, never the card data — and a clinic booking service's replay signal needs the same recovery discipline: identify the extra booking, release or reassign it through the application's own path, and tell the patient what happened.

## What this page is not doing

Nothing here authorizes logging real note content, real payment data, or real patient identifiers, in this fixture or anywhere else; every field name and value shown above is illustrative for a synthetic fixture only.
