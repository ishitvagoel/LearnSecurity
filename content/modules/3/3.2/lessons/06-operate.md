# Detecting a missing or stale threat without back-dating the model

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing the gate once is not the same as keeping the model current

[`lessons/04-build.md`](04-build.md)'s gate catches a missing id, an untraced flow, or a stale row at the one moment a human is already looking at the pull request. That moment does not cover every way a model can go wrong afterward. A named review trigger — a new share path shipping, a worker identity appearing, a new client surface opening — can fire on a day when nobody happens to be editing the threat-model file at all, and a gate that only runs on pull requests touching that file will never notice that the trigger fired somewhere else in the codebase. Operating this property means deciding what gets logged when a threat goes missing or stale, who that signal reaches, and what recovery looks like when the answer to "has anyone looked at this row since the trigger fired" is no.

## Signal design: what the line carries, and what it must never carry

A missing or stale threat produces a signal of this shape:

```text
missing_mandatory_threat reason=not_revisited id=cross-tenant-read trigger=new-share-path owner=authz
```

Four fields make this signal useful to whoever receives it. `reason` distinguishes the four ways a mandatory threat can fail this module's checks — `not_present`, `no_owner`, `no_trigger`, `not_revisited` — because a signal that only said "threat model check failed" would force the recipient to re-run the gate themselves just to find out which of four different problems they are looking at. `id` names the specific threat, `trigger` names the specific event that made the row stale (when the reason is `not_revisited`), and `owner` names who is accountable for that row, so the signal can be routed to a person rather than a general security inbox that nobody reliably reads.

One field is deliberately absent, and its absence is a decision, not an oversight: the signal never carries the threat's `mitigation` text. A mitigation description can end up naming an internal enforcement mechanism, an implementation detail, or a specific check's location in the codebase — exactly the kind of information a signal that gets forwarded into a shared ticket queue, a Slack channel with a broad membership, or a vendor's incident-management SaaS should not casually repeat. [3.1's classification lesson](../../3.1/lessons/01-property.md) already established that a signal designed to help someone debug can become a second leak if it carries the same content the original control was protecting; the same discipline applies here even though the "content" at risk is a design decision about SecureCollab's own defenses rather than a user's note body. A signal that names *which* threat and *why* it is stale, without repeating *how* SecureCollab defends against it, gives an on-call engineer everything they need to go look at the actual model file, and nothing an attacker reading the same alert stream would find useful on its own.

## Alert threshold, and the false-positive cost of getting it wrong

The merge-time gate from [`lessons/04-build.md`](04-build.md) already handles the synchronous case — a pull request that would leave the model incomplete fails immediately, in the pull request itself, and needs no separate alerting path because a human is already looking at exactly the right place. The harder case is the asynchronous one: a trigger fires in a pull request that never touches the threat-model file at all, because shipping a new share path and updating the threat model are two different changes that a team can easily let drift apart. Detecting that case requires a periodic check — running once after each deploy, or on a schedule — that re-evaluates every mandatory threat's `revisited_after` against whatever triggers have fired since the model was last touched, and pages the row's `owner` only when a fired trigger has no matching entry.

Scoping the alert to *specific rows with a specific unmet trigger*, rather than firing on every commit that merges while any trigger has ever fired, matters because the false-positive cost of over-alerting is not merely annoying — it trains the recipient to stop reading. A signal that fires every time any pull request merges, regardless of whether that pull request has anything to do with the model, teaches its recipient within a week that this alert is noise, and a real staleness event arriving in week two gets the same reflexive dismissal as the false alarms that preceded it. Scoping the alert per-row, per-trigger, means it fires exactly as often as the property it is protecting actually requires attention: once per row per trigger that has actually fired and actually gone unaddressed, not once per unrelated merge.

## Containment, revocation, and recovery

This module's threat model does not itself enforce `cross-tenant-read`'s mitigation — [4.4's `can_read` matrix](../../../4/4.4/spec.md) does — so containment and revocation for an actual cross-tenant incident belong to that module and to [10.5's incident response](../../../10/10.5/spec.md), not to this one. What this module's recovery step covers is narrower and specific to the threat model's own currency: when a `missing_mandatory_threat` signal fires, the recovery is to add the missing id, owner, trigger, or mitigation, and to record the trigger's name in the affected row's `revisited_after` list — never to change a `model_last_updated`-style date to make the row look current without actually reopening [1.3's four questions](../../../1/1.3/lessons/01-property.md) for it. [`lessons/05-verify.md`](05-verify.md)'s anti-fake tests exist precisely because "make the date look recent" and "actually re-review the row" are observably different actions from outside the gate, and only one of them is the recovery this property requires.

## The human path, and what happens when nobody reads it

Every alert this lesson describes ends with a person deciding whether a row's mitigation still holds and whether its priority is still correct — an automated gate can confirm a mitigation string is not a placeholder, but it cannot confirm the mitigation is still true after the system it describes has changed. That decision point is a security-sensitive human action, and the interface presenting it — a CI failure comment, a ticket, a paging alert — has to remain usable by the person actually on call: naming severity by a `reason` code and a threat `id` in text, not by color alone, keeps the signal legible to a screen reader and to a black-and-white terminal alike, consistent with the accessibility discipline [WCAG 2.2](https://www.w3.org/TR/WCAG22/) states for any interface where a human's action is part of the control.

Model what happens when that person does not act. A `missing_mandatory_threat` alert that nobody triages leaves the model exactly as stale as if the alert had never fired — the gate's detection is only as good as the recovery step someone actually performs, and an alerting pipeline with no owner assigned, or an owner who has left the team with nobody reassigned, produces the identical outcome to no alerting at all: a threat row that says it was reconsidered and was not. This residual is not something this module's mechanism can close from the inside; naming it honestly, rather than implying that a green gate plus a wired-up alert equals a currently-true model, is itself part of what this module's property requires.

## What this lesson is not doing

This lesson does not authorize paging a real on-call rotation, filing a real ticket, or wiring this signal into any system outside `labs/3.2/3.2-lab`. The signal shape above is a design artifact to reason about, not a live integration this course operates.
