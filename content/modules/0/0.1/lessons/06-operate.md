# Notice a denial without keeping what was denied

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Noticing is not keeping

Fixing `target_is_authorized` once handles the moment a URL is evaluated; it says nothing about what happens to the fact that a denial occurred, and treating the fix as the end of this module's work is how a correct check ends up sitting next to an operational habit that quietly undoes it. Suppose a denial is logged the way this course expects — `out_of_scope host=example.com reason=not_allowlisted` — and suppose a teammate, wanting more context for a ticket, adds "just the response headers, not the body, that should be fine" to the same log line. It is not fine, and the reason is not a matter of degree. The entire justification for denying a host in the first place is that nobody granted this tester permission to interact with it; a response, or any piece of one, exists only because an interaction already happened, and every additional byte captured from that interaction is a second act of the same unauthorized contact the deny check was built to prevent, filed under a name — "logging," "context," "for the ticket" — that makes it sound like recordkeeping rather than repetition.

This module's own fixture cannot demonstrate that failure directly, because `target_is_authorized` is a pure predicate: it never opens a connection, never receives a response, and has no body to accidentally keep. That is a deliberate and named gap, not an oversight — the failure this lesson is about happens one layer up, in whatever code calls the checker and decides what to do with its answer, and this lesson's job is to make sure you can recognize and refuse that failure even though no test in this lab can catch it for you. A checker that fails closed, sitting upstream of code that fetches anyway on error, or that logs a captured body "just this once," has been defeated by its caller exactly as thoroughly as if the checker itself had a bug — the checker did its job and said no, and the surrounding system overrode that no in a way no unit test of the checker alone will ever surface.

```
out_of_scope host=example.com reason=not_allowlisted request_id=7f21
```

That line is the entire correct signal: a host, a reason, and enough correlation information (a request ID) for someone investigating a spike in denials to find the surrounding context in other systems, without a single byte of what that host might have returned. Compare it to what a well-intentioned "richer" version often looks like in practice — a line that also carries a truncated snippet of a response body "for debugging," or a screenshot attached to the same incident ticket "so reviewers can see what it looked like." Both of those richer versions have converted a record of a refusal into a record of the thing that was refused, and the second record is strictly worse than having no record at all, because it now exists in a ticketing system, a log aggregator, and every backup of both, multiplying the number of places an unauthorized read of that host's content now lives.

## The recovery step nobody wants to write

Noticing and recovering are different obligations, and a system that only implements the first has half a control. The recovery step this module expects, when a denial is correctly logged and nothing was fetched, is genuinely simple: stop, and tell whoever is responsible for this course or this engagement that a denial occurred, so a pattern of repeated near-misses against the same host is visible to a person rather than buried in a log nobody reads until an incident forces the question. The recovery step when something was fetched *before* the check ran — the ordering mistake, not the check itself, being wrong — is less comfortable to write down: the fetched content must be discarded, not summarized, not "kept just in case," and the discard has to happen even though it feels like throwing away evidence, because the content was never authorized evidence to begin with, and the number of places it exists should only ever shrink from the moment the mistake is discovered.

A rejected alternative worth naming here: keep the fetched body in a restricted, access-controlled location "for a security review," reasoning that the access control makes the retention safe. This fails for the same structural reason the "just the headers" version does — restricting *who* can see an unauthorized capture does not make the capture authorized, it only limits how far the compounding goes; the original act of retrieving that host's content was never sanctioned by anyone with standing to sanction it, and no storage policy applied afterward changes who was entitled to cause that retrieval in the first place. The honest recovery step is deletion, paired with a written note of what happened and why, not a more careful shelf to keep the thing on.

## Practice

Run this only inside `labs/0.1/0.1-orientation/`. No exercise below fetches or should fetch a denied host.

Write the log line your own lab environment would emit for a denial of `evillab.securecollab.test`, following the `out_of_scope host=... reason=...` shape above, and then write one sentence identifying the exact field that a well-intentioned "add more context" instinct would be tempted to add, and one sentence stating why that addition is the violation this module warns against rather than an improvement.

## Check yourself

- Why does a captured response body attached to a denial ticket make the situation worse than the denial alone, rather than merely redundant?
- What is the one operational fact this lesson's log line is required to carry, and the one category of content it must never carry, regardless of how useful that content would be for debugging?
- If code elsewhere in a real system catches an exception from a scope check and proceeds with the request anyway "to avoid breaking things," which of this module's five claims does that pattern violate, and why does the checker itself passing every test in `labs/0.1/0.1-orientation` not protect against it?
