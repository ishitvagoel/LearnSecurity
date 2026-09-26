# Transfer: chart text and appointment time on one card

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## What actually changes, stated precisely

Swapping "notes app" for "clinic" while keeping every other assumption in place is a rename, not a transfer — the point [1.3's own transfer note](../../../1/1.3/lessons/01-property.md) makes about the document-preview service applies here with the same force. This transfer changes something more specific than the product noun: the **asset** moves from a note body, a field with no fixed internal structure, to a patient's chart text, a field that in most jurisdictions carries regulatory retention and disclosure obligations no note body has; and the **actor set** gains a party this module's SecureCollab fixture never modeled at all — a clinician who is authorized to read the chart but not authorized to have it appear in a debugging log any more than an unauthorized party is, because "may read through the application" and "may appear in a log line anyone with log access can see" are two different authorizations, not one. A booking card carrying **two fields with two different levels on one record** — chart text (Confidential) and appointment time (Internal) — is this transfer's actual subject, and it is deliberately the same two-level structure [`lessons/02-model.md`](02-model.md) used throughout, so that what changes is genuinely the asset and the actor, not the shape of the problem.

## Which claims survive, which break, and why

**C1 survives without modification**, because a field's classification is still a per-sink question, not a label: "chart text: Confidential" still means nothing until a specific sink — the clinic's own equivalent of `log_event` — is checked against it, and nothing about moving from a note body to chart text changes what a sink rule has to do.

**C2 survives, and gets a sharper example.** A clinic's patient-portal session token is this transfer's authority artifact, exactly parallel to SecureCollab's `session_token` — and the same ranking argument applies: a party who reads a patient's chart text from a log learns one patient's chart. A party who reads that patient's session token can act as the patient (or, if the clinic's staff use a similar portal token, as a clinician) for as long as the token remains valid. The clinic setting sharpens this because a clinician's session token, if logged, could let a reader act with clinical authority — order tests, view other patients' records the clinician is authorized to see — which is a broader authority artifact than anything in SecureCollab's current fixture, precisely because clinician accounts typically carry broader access than an individual patient's own account does.

**C3 survives**, because "chart text: Confidential" is still a level, not a requirement; the same per-sink allow/deny-with-failure-behavior structure [`lessons/04-build.md`](04-build.md) derived has to be written out again for whichever sinks the clinic's booking system actually has, since the derivation does not transfer automatically just because the vocabulary sounds similar.

**C4 survives, with a higher stake.** A field added to a clinic's booking schema tomorrow — a new "reason for visit" free-text field, say — defaults to exposure exactly as an unclassified SecureCollab field would, for the identical reason: no sink treats an unnamed field as anything other than ordinary data. The stake is higher here because a "reason for visit" field is more likely to contain clinically sensitive content by its very nature than an arbitrary new SecureCollab field is, which does not change the mechanism but does change how urgently a team should treat "we haven't classified this yet" as an active risk rather than a backlog item.

**C5 breaks in one specific way and has to be rewritten, not merely restated.** SecureCollab's recovery step for an exposed note body was "purge the log line; done," because a note body carries no regulatory retention obligation of its own. A clinic's chart-text log line cannot simply be purged the same way if the clinic is subject to a legal retention requirement on clinical records — purging may need to be reconciled with, not substituted for, whatever retention rule applies, which can mean redacting a copy while a compliant original is retained under separate, tightly controlled access, rather than deleting outright. This is the one claim this transfer cannot answer by analogy; it requires knowing the clinic's actual retention obligation before the recovery step can be written correctly, which is exactly the kind of context this lesson's opening claim pattern names: "if context is missing, the answer is no" — here, "the answer is no, this recovery step cannot be finalized without that context."

A clinic's version of the fixed sink policy would extend the same shape this module's lab already uses, with one new row for the retention-aware sink C5 requires:

```python
CLASSIFICATION = {
    "chart_text": "confidential",
    "patient_session_token": "confidential",
    "appointment_time": "internal",
}
SINK_POLICY = {
    "application_log": {"internal"},
    "compliant_retention_store": {"confidential", "internal"},  # C5's answer, once the retention question is resolved
}
```

Note that `compliant_retention_store` is the only sink in this sketch permitted to carry `confidential` at all, and it is permitted only because it is a separate, access-controlled destination built for exactly that obligation — not the same application log the rest of this module's fixture uses.

## What is not good enough as a substitute for doing this

| Rejected substitute | Why it fails |
|---|---|
| "The chart text is sensitive, so we classified it" | Names a level, not a sink; says nothing about which of the clinic's actual sinks may carry it |
| A privacy-policy document describing patient data handling | A document is not a code path any sink actually executes |
| "HTTP 200 on the booking endpoint" as evidence the classification holds | Confuses "the request succeeded" with "the response and its logs did not carry a denied field" — two unrelated observations |

## Success criteria

Write, for the clinic booking card, an inventory row and a requirements-backlog entry in the shape [`lessons/02-model.md`](02-model.md) and [`lessons/04-build.md`](04-build.md) established: asset, classification level, every sink you can name for a clinic booking system (at minimum an application log and a support-ticket path), the allow/deny decision per sink, and the failure behavior for an unclassified field. Your answer succeeds if it: correctly classifies the patient-portal session token at least as sensitively as the chart text, and explains why in terms of what possessing the token grants rather than merely asserting it; states explicitly that logging the appointment time does not authorize logging the chart text, and that the two require independently-checked decisions even though both live on one record; and, for C5 specifically, names the retention question your recovery step depends on rather than writing a recovery step that silently assumes no retention obligation exists. A complete answer also states, in one sentence, which of this module's five claims required no change at all to transfer — a correct answer should be able to say precisely that C1, C2, C3, and C4 transfer unchanged, and name why C5 is the one exception, rather than treating "some things changed" as a single undifferentiated conclusion.

## What this lesson is not doing

This is a written exercise, not a system to build or run. Do not fetch a real clinic's system, use a real patient's chart, or treat any real healthcare regulation's specific text as settled by this lesson — the retention question in C5 is deliberately left open because its answer depends on a jurisdiction and a regulation this fixture does not name, not because the answer does not matter.
