# A fix that lives in one function: detect, purge, rotate

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Why the fix from lesson four is not the end of the story

[`lessons/04-build.md`](04-build.md) derived a mechanism and named its own limit honestly: `_redact` governs the two sinks it is wired into, and nothing else. A new sink added next quarter, an exception path this fixture never modeled, or a hosting platform's own request-capture agent can all reintroduce the exact failure [`lessons/03-break.md`](03-break.md) reproduced, without anyone touching `log_event` or `write_error_dump` at all. A classification requirement that stops at "and then we fixed the logger" is only true until the next code path forgets it, which is why C5 — the last of this module's five teaching claims — requires a detection signal and a recovery path alongside the sink check, not instead of it.

## Designing the signal: what it carries, and the one field it must never carry

A **redaction-miss signal** fires when a sink emits a field whose classification level is not in that sink's own policy — in other words, when the mechanism [`lessons/04-build.md`](04-build.md) built has itself failed to run, or has run against a sink that was never wired into it. The signal has to name enough for an operator to act on: which event was being processed (`event`), which sink emitted the miss (`sink`), and which classification level was denied (`level`). It deliberately omits the one field that would make the signal useful for debugging and simultaneously turn the signal itself into a second leak: the actual denied *value*.

```text
log_redaction_miss reason=confidential_field event=note_read sink=application_log level=confidential
```

Compare this to a design that seems, at first glance, more helpful: `log_redaction_miss ... value=tenant-A-secret-body`. Carrying the value would let an operator confirm at a glance that the alert is real and not a false positive — a genuine cost of the safer design, worth naming rather than hiding. But an alert channel is itself a sink, usually reaching a different, often *wider* audience than the original log (a paging system, an incident channel, a ticket) — so a signal that carries the denied value has recreated exactly the failure it exists to report, one hop downstream, in a system this classification mechanism was never wired to protect in the first place. The signal's job is to prove a denial happened and to name where, not to reproduce what was denied.

## Alert threshold, false-positive cost, and who receives it

A single redaction-miss event is worth investigating, not paging someone at 3 a.m. for: it can indicate a genuine new leak, but it can also indicate a deliberate, correctly-classified test — this module's own `test_unclassified_field_defaults_to_redacted` triggers exactly this signal on every run, by design, because a fresh unclassified field being denied is the *correct* behavior, not an incident. A reasonable threshold pages on-call only after a sustained rate — say, redaction misses from a single sink exceeding a small count within a short window — because a sustained rate across real traffic is much more likely to mean a new, unclassified field shipped to production than a single denied test fixture. The false-positive cost of a threshold set too low is direct and measurable: engineers stop trusting the alert, and the next genuine miss gets the same shrug the last dozen false ones got, which is a worse outcome than no alert at all, because it consumes the same on-call attention budget while teaching the team to ignore exactly the signal meant to catch this failure. The receiving audience is the team that owns the sink in question — application logging for `application_log`, whichever team owns exception handling for `error_dump` — not a generic security inbox that receives volume without owning the fix.

## Containment, revocation, recovery

The moment a redaction miss is confirmed as a genuine new leak rather than a test artifact, three actions follow, in order. **Contain**: identify every sink instance that emitted the denied field and stop new instances of the same miss — typically, route the offending sink through `_redact` immediately, even before root-causing why it was missed in the first place, because every additional emission while root-causing is in progress widens the exposure for no benefit. **Purge**: locate and remove the already-written records containing the denied value from whatever store holds them — the log files, the search index, any backup that already copied them — rather than leaving the exposure in place "until someone gets to it." **Rotate**: if the denied value was an authority artifact rather than mere content — a session token, in this module's fixture — the exposed value has to be invalidated, because purging where it was logged does nothing about copies that may already have been read; a session token that already left the sink and was read by even one unintended party is compromised regardless of whether the log line itself is later deleted, and only revoking the token closes that window. Purging a note body's log line, without a corresponding revocation, is a complete recovery for that leak, precisely because a note body carries no power of its own — this is the same asymmetry [`lessons/01-property.md`](01-property.md) established between content and authority artifacts, showing up again in what recovery actually requires.

One discipline binds all three: never re-emit the denied value while investigating or reporting it. A ticket, a chat message, or an incident report that quotes the leaked line in full to "show the team what happened" creates a fresh, un-redacted copy of the exact value this whole mechanism exists to contain, now sitting in a store — a ticketing system, a chat log — this module's sink rule was never wired to reach.

## The human-in-the-loop path has to be usable, not just present

An operator triaging a redaction-miss alert is a human-mediated control, and [blueprint §16.12](../../../../../secure-application-engineering-curriculum-blueprint.md) requires that a security-sensitive journey with a human step be tested for usability and accessibility, not merely specified. A dashboard that shows a redaction-miss badge as a colored dot alone — red for active, gray for resolved — fails an operator who cannot distinguish those colors or who is using a screen reader, exactly the class of failure the W3C's WCAG 2.2 Success Criterion 1.4.1 (Use of Color) names: color must never be the *only* means of conveying that state. The fix costs nothing structurally — a text label (`"active"`, `"resolved"`) or an icon with alt text alongside the color carries the same information to every operator, not only the ones for whom the color distinction happens to work.

## Operator failure is a residual risk, not an edge case

Every alert this lesson designs assumes a human reads it, and that assumption fails routinely, not exceptionally: on-call rotations lapse, alert fatigue from an earlier badly-tuned threshold causes real signals to be dismissed alongside false ones, and a redaction-miss alert routed to a channel nobody actively monitors is operationally no different from no alert at all. Naming this as residual risk — rather than treating "we have an alert" as equivalent to "this is handled" — is what keeps the operate step honest: the mechanism in [`lessons/04-build.md`](04-build.md) fails closed by default, but the detection and recovery this lesson adds fail open by default, the moment the human step in the loop does not happen. A mature backlog entry names who owns response to this specific alert and how that ownership is verified to still be true, not only what the alert says when it fires.

## Practice

Using the signal shape above, write the corresponding line for a redaction miss on the error-dump sink instead of the application log, and name one reason the threshold for paging on-call might reasonably differ between the two sinks — consider how often each sink fires under normal, non-incident traffic, and what that difference implies for how quickly a sustained-rate threshold would trip on each.

## Use it somewhere new

A clinic's booking system needs the same three-part response — contain, purge, rotate — for a chart-text redaction miss, with one difference worth predicting before [`lessons/07-transfer.md`](07-transfer.md) asks you to write it out: which of this lesson's three recovery actions changes least when the asset moves from a note body to a patient's chart text, and which changes because a clinic record, unlike a note, may carry legal retention obligations a purge has to account for.
