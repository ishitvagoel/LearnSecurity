# Detect a mismatched hit or a mismatched hop; purge and rotate without logging bodies

**Kind:** operations-exercise
**Loop step:** 6 Operate

## A fix that only lives in one place

`04-build.md` repaired three functions inside the origin's own code, and `05-verify.md` proved the repair holds against the local suite. Neither step touches the fact that a real deployment has an edge, a CDN, and an operator who can redeploy either one — none of which run the code this module tested. Claim C5 names this directly: a CDN configuration change, a redeployed edge, or an operator error can reintroduce a path-only cache key or a trusted forwarded header without a single line of the origin's Python changing at all, so the fix from `04-build.md` needs a companion signal that would catch its own silent reversal.

## Two signals, for two different reversions

A cache-key regression and a hop-authentication regression fail differently and need different evidence to notice. A cache-key regression is visible only by comparing what the cache *served* against what the caller was actually *bound to* — the mismatch is between two identities the origin itself computed, not an error any single request raises on its own. A hop-authentication regression is visible as an explicit rejection at the moment the check runs, because `hop_is_trustworthy` already returns a boolean the caller can act on.

```mermaid
stateDiagram-v2
    [*] --> Serving
    Serving --> CacheHit: cache lookup succeeds
    CacheHit --> Compare: compare served company to bound company
    Compare --> Serving: match -- no signal needed
    Compare --> Mismatch: served company != bound company
    Mismatch --> Signal1["emit cdn_hit_company_mismatch\n(path, bound company, served company --\nnever the body)"]
    Signal1 --> Purge["purge the (path, served-company) entry"]
    Purge --> Incident: [entry had already been served to a caller]
    Purge --> Serving: [entry purged before any caller received it]
    Serving --> HopCheck: relay attempted
    HopCheck --> Rejected: hop_is_trustworthy() is False
    Rejected --> Signal2["emit hop_rejected\nreason=hostname_mismatch|version|untrusted\n(hostnames, never key material)"]
    Signal2 --> Serving
    Incident --> [*]
```

The failure transition from `Compare` — a served company that does not equal the bound company — is the state most monitoring setups never build, because a healthy system never reaches it; it only becomes reachable after C5's own regression has already happened, which is exactly when it matters most. A dashboard built only from happy-path metrics (cache hit rate, response latency) will show this regression as *improved* performance, because a wrongly-shared cache entry serves faster than a correctly-scoped miss.

## What the signal must and must not carry

Both signals name the mismatch without ever carrying the value that made it sensitive. `cdn_hit_company_mismatch` carries the request path, the bound company, and the company the cache actually served — three identifiers, none of them the note body itself. `hop_rejected` carries the expected and presented hostnames and a reason code, never the certificate's private key material or any session token that might have accompanied the rejected relay. A signal that includes the leaked body to "help investigate" turns the monitoring pipeline into a second copy of the exact leak it exists to detect — the log now needs its own incident response, on top of the one the cache already started. The general shape of this constraint recurs everywhere a detection signal sits downstream of a secrecy failure: the evidence that proves a leak happened is, definitionally, the same data whose exposure the leak consists of, so a signal schema has to be designed to prove the mismatch occurred without ever repeating the sensitive value that made the mismatch matter.

## Worked example: two log lines, read for what they omit

```text
cdn_hit_company_mismatch path=/notes/n1 bound=companyB served=companyA request_id=req_9f2e
hop_rejected reason=hostname_mismatch expected=notes-origin.securecollab.internal presented=billing-origin.securecollab.internal request_id=req_a103
```

Neither line contains `tenant-A-note`, any other note body, or a certificate's private key. `request_id` lets an operator correlate either line with the rest of that request's own trace without needing the sensitive value at all — the correlation identifier and the sensitive value are two different fields serving two different jobs, and a schema that conflates them by, for example, using the note's own id as the correlation key would still leak nothing extra here, but would in a system where the identifier itself was sensitive. A third field worth naming and rejecting: `served_body_hash`, added "just in case," would let an investigator confirm two mismatched hits served identical content without ever needing the plaintext — a defensible addition a careful designer might propose, and one this fixture deliberately does not build, because it adds a new field whose own security properties (does a hash reveal enough to matter for a short, guessable note?) this module has not analyzed.

## Recovery is not the same action for the two claims

For C1's cache regression, recovery is a purge of the specific `(path, company)` entry, or — if the deployment cannot key its purge that precisely — the whole prefix that could contain a mis-keyed entry, followed by a decision about whether any caller already received the wrong body before the purge ran. If one did, that is a secrecy incident, not a performance blip, and it gets the same disclosure and rotation treatment any other secrecy incident does, regardless of how briefly the mismatch existed. For C3's hop regression, recovery is narrower: `hop_rejected` already prevented the relay from completing, so there is no body to have leaked through that specific rejected attempt — the operational work is confirming the rejection reason is a real infrastructure drift (a misrouted edge, an expiring certificate) and not a false positive from a legitimate certificate rotation in progress, which is a different investigation with a different urgency.

## A certificate failure drill is not the same exercise as a purge drill

`module.yaml`'s assessment blueprint names a certificate-failure drill as separate evidence from the purge playbook above, and the two should stay separate: a purge drill answers "how fast can we stop serving a wrongly-shared cache entry," while a certificate-failure drill answers "when `hop_is_trustworthy` starts rejecting hops that used to succeed, is that a real problem or an expected consequence of a certificate rotation nobody told this check about." Collapsing the two into one runbook risks training an operator to treat every `hop_rejected` burst as routine, which is exactly the assumption C3 exists to keep from becoming automatic.

## Practice

Sketch both signal lines above for a `(note_id="n1", bound=companyB, served=companyA)` mismatch and a hostname-rejected relay, naming every field each line carries and confirming neither line contains a body, a key, or a token.

## Use it somewhere new

For an authenticated CSV export, name the export-specific version of each signal: what does "served company" mean for a streamed export rather than a single JSON body, and does purging an in-flight export require anything beyond removing the cache entry the next request would have hit?

## What this page is not doing

This page does not stand up a real CDN, a real alerting pipeline, or a real certificate rotation; it designs the two signals and the two recovery paths a real deployment would need, verified only against the vocabulary this module's local fixture already established. Answer keys are not on this site.
