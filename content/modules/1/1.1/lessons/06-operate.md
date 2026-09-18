# Preserve useful outcomes when prevention fails

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Prevention is not the end of the claim

Every row in SecureCollab's catalogue names a mechanism and a limit on that mechanism, and a limit that goes unaddressed is a promise the catalogue has made and then abandoned. The membership-integrity row in `fixed/security_claim.yaml` states plainly that its mechanism does not repair an incorrect authorization rule and that a global idempotency key can collide across tenants if its scope is set wrong — naming those limits is only useful if the catalogue also says what happens the moment one of them is hit. That is the job this lesson's Operate step does: design the signal that notices the limit being reached, the threshold that turns noticing into action, the containment step that stops the damage from spreading, and the recovery step that restores a defensible state, all without turning the operational evidence itself into a second copy of the thing it was supposed to protect.

## Designing a signal that is useful and not a leak

`catalogue_validator.py` requires every claim's `detection` mapping to carry five fields — `signal`, `threshold`, `eventFields`, `prohibitedFields`, and `failureBehavior` — and each one earns its place by answering a question the mechanism-only SECURITY.md never asked. Take the accountability row's detection block as the worked case: its signal is a missing event sequence, an event-write failure, or administrative access outside a declared incident window; its threshold treats a committed high-impact change with no durable evidence as an immediate operational fault rather than something a weekly report picks up eventually; its `eventFields` list actor id, tenant id, target id, action, decision code, authority version, and correlation id — enough to reconstruct who did what to whom and under which policy decision; and its `prohibitedFields` explicitly bar note body, password, token, and member contact value from ever entering the event at all. That last list is not a formality. A log line built to help an investigator is still a second store of exactly the data the confidentiality row exists to protect if nobody drew the boundary around what the event may contain, and an incident response process that has to search audit logs for the same sensitive content it was trying to contain has turned its own evidence trail into a new leak channel.

```yaml
detection:
  signal: Missing event sequence, event-write failure, or administrative access outside an incident window
  threshold: Immediate operational fault for a committed high-impact change with no durable evidence
  eventFields: [actor_id, tenant_id, target_id, action, decision_code, authority_version, correlation_id]
  prohibitedFields: [note body, password, token, member contact value]
  failureBehavior: The mutation uses its documented fail-closed or recoverable outbox path and raises an independent health signal
```

Compare that block to a plausible-sounding alternative a team under deadline pressure might ship instead: logging the full request body "so we have everything if we need it later." That version is easier to write and answers a real short-term worry — what if the seven named fields turn out to be insufficient — but it fails the exact test [05-forbidden-outcomes.md](05-forbidden-outcomes.md) built the detection-field check around: `prohibitedFields` stops being enforceable the moment "everything" includes note bodies, and the operational evidence path has silently become an unaudited second copy of the asset the whole catalogue exists to bound.

## Threshold, false positives, and who receives the alert

A threshold set too low turns every legitimate retry or every tenant administrator doing ordinary bulk cleanup into a page that a human has to triage at 2 a.m., and a team that gets paged for nothing enough times starts silencing the channel — the well-documented failure mode where an alert that is too sensitive becomes, in practice, less useful than no alert at all. A threshold set too high lets the availability row's "one tenant's export workload starves every other tenant's reads" run for hours before anyone notices, because the signal never crossed the line that was supposed to trigger a human response. The accountability row's choice — immediate for a committed high-impact change with no evidence, aggregated review for ordinary denied probes — is a deliberate answer to that trade-off: it treats "something the system was supposed to prevent from being unrecorded just happened" as urgent, and treats "someone tried something and was correctly denied" as a pattern to review in aggregate rather than an event to wake anyone for individually.

## Containment, root-cause repair, and recovery validation

Detection alone does not close a claim; the catalogue's `recovery` field requires at least two concrete steps, and the two named in the confidentiality row show why one is not enough. Revoking the implicated session or membership stops the immediate access, and that step alone leaves the exposed log or export copies sitting wherever they already landed — removing those copies, repairing whatever alternate path let the leak occur, and rerunning the cross-tenant negative tests before declaring the incident closed is the second half of the same recovery, and skipping it converts "we contained it" into "we contained the part that was easy to contain." Recovery validation is the discipline of actually rerunning the evidence rather than trusting that the repair worked because the code change looked right; a fix that changes the policy check but is never verified against the abuse-case tests from [05-forbidden-outcomes.md](05-forbidden-outcomes.md) has repaired an assumption, not a behavior.

## Human recovery paths have to stay usable

Several of SecureCollab's recovery and containment steps put a person in the loop — a tenant administrator confirming a membership restoration, or a support operator approving a bulk-export hold — and a recovery design that only works for the one engineer who wrote it has traded one failure mode for another. The interface for that human step needs a clear completion state, so the administrator can tell whether their confirmation actually took effect rather than guessing from silence; an accessible alternative path when the primary interface is unavailable, because an incident is exactly the moment a normal login flow is more likely to be degraded, not less; and a failure behavior that denies rather than silently proceeds if the human step cannot be completed, matching the fail-closed rule the catalogue already applies to every automated check. A recovery runbook that assumes a keyboard-and-mouse admin console will always be available to the one on-call person that week is not a bounded claim; it is an unstated assumption exactly like the ones [02-securecollab-catalogue.md](02-securecollab-catalogue.md) asked you to name explicitly.

## The residual risk nobody's mechanism reaches

Every operational design in this lesson depends on the operator reading the alert, running the recovery step correctly, and not being the source of the compromise. Record that dependency rather than pretending it away: an operator with access to both the primary state and the only evidence store can suppress or alter the record of their own action, which is exactly the residual risk `fixed/security_claim.yaml`'s accountability row names rather than claims to solve. This module's trusted computing base explicitly excludes a privileged infrastructure administrator from what it defends against, and an operate section that quietly assumed the operator is always trustworthy would have widened that trust boundary without telling anyone — the same silent widening [01-property-vs-mechanism.md](01-property-vs-mechanism.md) opened this module by warning against, now showing up in a runbook instead of a slogan.

## Practice

Run this only inside `labs/1.1/1.1-invariant-catalogue/`. The data is synthetic.

Take the availability row from `fixed/security_claim.yaml` and write your own detection block: a signal, a threshold with its false-positive cost stated in one sentence, an `eventFields` list, a `prohibitedFields` list, and a `failureBehavior`. Then write the two-step recovery a drained, abusive tenant workload actually requires, and name one point at which a human has to act and what that person sees if the action succeeds versus fails.

## Check yourself

Explain why "log everything" fails the same check that rejects a mechanism-only property statement, and name the operator-compromise residual risk this module records rather than tries to close. [07-transfer.md](07-transfer.md) asks which of this lesson's operate decisions survive a move to a system where the human in the loop is not an employee at all.

## What this page is not doing

This lesson does not design a production alerting pipeline or claim any of these detection fields are wired to a real system; SecureCollab has no deployed service yet. Answer keys are not on this site.
