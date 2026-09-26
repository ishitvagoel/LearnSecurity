# Transfer: clinic SMS reminders

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## What changed, stated before you're asked to solve anything

SecureCollab's threat model, as built through this module, answers questions about a browser, an API, and a future worker — three flows, three always-name ids, one enforcement point per flow. The system you are asked to model next is a clinic's appointment-reminder feature: a booking API sends a text message, through a third-party SMS gateway vendor, to a patient's phone number, containing an appointment time and, if a careless template writer includes it, chart text. Three things changed at once, and naming them precisely matters more than solving the exercise quickly. The **actor** set gained an SMS gateway vendor — a party the clinic does not operate, sitting on the wire between the API and the handset, whose own security posture the clinic cannot inspect the way it can inspect its own code. The **channel** changed from an HTTPS request the clinic's own server both sends and receives to a one-way SMS delivery the clinic's server hands off and cannot confirm was received by the intended person rather than by whoever now holds that phone number. The **boundary** that matters most shifted from "browser versus server" to "clinic versus vendor versus carrier versus handset" — a chain of four parties, only the first of which the clinic's own threat model can directly instrument.

## Which of this module's claims survive, and which do not survive unchanged

**C1 survives in shape, not in content.** The claim that a green signal cannot stand in for the versioned model still holds exactly — but the signal that plays "scanner" here is a vendor's compliance questionnaire, not a SAST tool, and the always-name set itself has to be rederived from scratch rather than renamed. `cross-tenant-read`, `hostile-browser`, and `stolen-worker` are specific to HTTP request handling and a browser origin; none of the three names a threat that exists in an SMS pipeline. A vendor's "HIPAA certified" badge is evidence about that vendor's own general practices, in the same way a green SAST scan is evidence about pattern-matched code defects — real, but an answer to a narrower question than "has this specific system's design been walked for what can go wrong," and for the identical reason: a vendor certification has no mechanism for recognizing "this specific clinic's message template happens to interpolate chart text," any more than a SAST rule has a pattern for "this specific check compares the wrong two fields."

**C2 survives directly, with a genuinely new flow.** The claim that a threat id with no traced flow behind it is unfalsifiable transfers without modification — but this channel introduces a flow type this module's original three never needed: a delivery path the clinic's own system cannot observe past the point of handoff to the vendor. `browser-share-request`, `member-note-read`, and `worker-share-redelivery` all terminate inside SecureCollab's own infrastructure, where the clinic can trace every step. An SMS send terminates on a carrier network and a physical handset neither the clinic nor, typically, the vendor fully controls, which means "trace the flow" for this channel has to include a boundary the model can name but cannot instrument directly — a genuinely new situation this module's HTTP-only flows never presented.

**C3 survives directly.** A prioritized threat list with a placeholder mitigation on the top row is exactly as useless here as it is for `cross-tenant-read`: "reminder body reviewed by compliance" is not more actionable than "TBD" unless it names a specific template-review mechanism, an owner, and what happens when a template is updated after the review.

**C4 survives, with a new class of trigger.** The claim that a fired review trigger demands a recorded re-review, not a rewritten date, transfers without change — but the triggers that matter for this channel are different in kind from "a new share path shipped." A vendor changing its own delivery infrastructure, a new country's carrier requiring a different message format, or a template edit that adds a new field are all triggers a threat model for this channel has to name, none of which corresponds to anything in SecureCollab's original three flows.

## Success criteria

Write a threat-model document for the clinic SMS reminder feature that a gate structurally identical to `labs/3.2/3.2-lab`'s could evaluate. It succeeds if it does all four of the following, and each is checkable against a specific, statable answer rather than against how polished the write-up looks. Every row needs the same shape SecureCollab's own model uses, illustrated here with a placeholder entry rather than a real answer, so the shape is not confused with the content:

```text
{
  "id": "example-channel-threat",
  "owner": "<the team accountable for this row>",
  "trigger": "<the named event that would make this row stale>",
  "priority": <an integer rank relative to this channel's other threats>,
  "mitigation": "<a real mechanism or owning process, not a placeholder>",
  "revisited_after": []
}
```

`example-channel-threat` is not one of this channel's real threats — it is a placeholder id standing in for the shape every row you write needs, the same six fields `labs/3.2/3.2-lab`'s gate already checks for SecureCollab's original three. A row missing any one of the six fields fails this exercise the same way it fails that lab, whatever channel it describes.

1. **Names at least three always-name threats specific to this channel**, and for each one, states in one sentence why no vendor questionnaire, carrier certification, or HTTP-style scanner could have surfaced it. A model that reuses `cross-tenant-read` verbatim, unmodified, for this system has not done this step — the threats have to come from this channel's actual actors and boundaries, not from copying the previous module's answer key.
2. **Names the required flows those threats depend on**, including at least one flow that represents the clinic-to-vendor-to-carrier-to-handset chain, and states explicitly which segment of that chain the clinic's own model can trace directly and which segment it can only assume.
3. **Resolves the top-priority threat's mitigation to a real, specific, non-placeholder decision** — naming a mechanism or an owning process, not a vendor's marketing claim — and states what would have to be true for that mitigation to actually hold.
4. **Names one review trigger specific to this channel**, and for a hypothetical case where that trigger has fired, states exactly what a `revisited_after`-style record would need to contain for the gate to consider the affected row current.

If the reminder feature's opt-out mechanism (a patient's ability to stop receiving texts) becomes part of your rewritten claim — because you decide a patient who cannot reliably opt out is itself a threat worth naming — state explicitly whether that path depends on a human reading and acting on a text-based instruction, and if so, name the accessibility property that path must hold; do not add an accessibility requirement to a claim that does not actually depend on a human-mediated step.

## What this transfer does not ask you to do

Do not contact a real SMS gateway vendor, send a real text message, or use a real phone number, chart text, or appointment record. This exercise produces a document, evaluated against the four criteria above and against `content/assessment/keys/3.2.md`'s rationale for this item — not a running integration, and not a claim that any specific vendor's product is or is not secure.
