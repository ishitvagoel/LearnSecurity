# Module 1.1 assessment items

Learner-facing. No answers, intended findings, or banding examples appear on this page — see `content/assessment/keys/1.1.md`, which is not linked from the site.

## 1. Mechanism, rule, or neither?

Four statements are proposed for SecureCollab's security document:

A. "We use Argon2id for password storage."
B. "A current Tenant A member may read a Tenant A note; a Tenant B member may not, through any in-scope API response, log, or export."
C. "The application is secure."
D. "Passwords are hashed, so authentication is solved."

For each of the four, say whether it is a bounded rule, a mechanism, or a universal claim, and justify your answer using the envelope elements from [01-property-vs-mechanism.md](../lessons/01-property-vs-mechanism.md). For any statement you label a mechanism or universal claim, name the one bounded rule (if any) it could plausibly support.

**Claim assessed:** C1 · **Outcome:** Separate desired properties from mechanisms, mechanism limits, framework defaults, and evidence

## 2. Five rows, one claim

A learner submits a five-row SecureCollab catalogue. Every row has every required field filled: `property`, `assets`, `attackers`, `trust`, `untrusted`, `timeHorizon`, `forbiddenOutcomes`, `evidence` with all four modes, `detection`, `recovery`, `residualRisk`, `nonGoals`, and `reviewTriggers`. All five rows use different `id` values. Nothing in any row matches a phrase on a mechanism-slogan list.

Is this catalogue necessarily five distinct, system-specific claims? Name the one additional property a reviewer — human or automated — has to check that field presence alone does not establish, and describe a concrete way five such rows could still fail that check.

**Claim assessed:** C2 · **Outcome:** Produce a versioned SecureCollab invariant catalogue with at least five testable system-specific rows

## 3. Which evidence mode is missing?

A SecureCollab catalogue row's `evidence` block reads:

```yaml
evidence:
  normal: ["A Tenant A member reads an A note and the event records the decision"]
  negative: ["Cross-tenant reads return no note body"]
  abuse: ["Cross-tenant reads return no note body"]
```

Name which required evidence mode is absent, describe one concrete SecureCollab event that mode would have to rule out, and explain why the `abuse` entry as written is not actually evidence for the `abuse` mode even though the key is present with a non-empty value.

**Claim assessed:** C3 · **Outcome:** Specify normal, negative, abuse, and failure evidence without treating control presence as proof

## 4. Root cause, precondition, or impact?

Read this excerpt from a SecureCollab document under review: "We are secure because passwords are hashed, TLS is enabled, and the scanner is green. The same statement covers tenants, notes, exports, backups, logs, and recovery."

State, as three separate sentences, the root cause of this document's failure, one precondition that would have to hold for a reader to be misled by it, and one concrete impact if the document were merged and trusted as written. Do not use any of the three words "root cause," "precondition," or "impact" to restate the excerpt; each sentence must add information the excerpt does not already contain.

**Claim assessed:** C1 · **Outcome:** Distinguish root cause, preconditions, impact, prevention, detection, and recovery for a mechanism-only assurance failure

## 5. What does the log line actually prove?

A SecureCollab engineer proposes this detection design for the cross-tenant confidentiality claim: on every note read, log the full request body and the full response body, "so we have complete evidence if something goes wrong."

Name the specific check this design would fail against `catalogue_validator.py`'s `prohibitedFields` requirement, and explain the security consequence of that failure in terms of the confidentiality claim the detection design is supposed to be defending, not merely "it violates a rule."

**Claim assessed:** C4 · **Outcome:** Design privacy-safe operational evidence and bounded response and recovery

## 6. Prose or schema?

A teammate proposes fixing SecureCollab's mechanism-only SECURITY.md by expanding it into a longer narrative document — three paragraphs per mechanism instead of one line — rather than adopting the structured, sixteen-field claim record from [04-smallest-mechanism.md](../lessons/04-smallest-mechanism.md).

Choose one of the two approaches and defend it against the other under the stated constraint that the result must be independently reviewable by someone who did not write it. Then name one thing your chosen approach still cannot verify about SecureCollab, even once adopted.

**Claim assessed:** C2 · **Outcome:** Bound claims with assets, attacker capabilities, trust, state, time, forbidden outcomes, residual risk, and review triggers

## 7. CivicClinic: guardian access after revocation

A guardian's delegated authority over a dependent's CivicClinic record is revoked at 2:14 p.m. The guardian's browser session, opened at 2:00 p.m., is still active. At 2:20 p.m., the guardian's browser sends a request to read the dependent's appointment history.

Using the transfer method from [07-transfer.md](../lessons/07-transfer.md), state what SecureCollab's membership-integrity claim would predict for an analogous SecureCollab scenario, explain why that prediction does not transfer unchanged to this guardian scenario, and write the bounded CivicClinic rule that should govern the 2:20 p.m. request.

**Claim assessed:** C5 · **Outcome:** Transfer the method to a materially changed system and explain which original claims fail

## 8. Signal, threshold, and the false-positive it creates

Design a detection block — `signal`, `threshold`, `eventFields`, `prohibitedFields`, `failureBehavior` — for SecureCollab's availability claim (one tenant's export workload must not starve other tenants' reads). State one legitimate, non-abusive SecureCollab event your chosen threshold would still flag, and say what the on-call reviewer should do when that false positive occurs rather than silencing the channel.

**Claim assessed:** C4 · **Outcome:** Design privacy-safe operational evidence and bounded response and recovery
