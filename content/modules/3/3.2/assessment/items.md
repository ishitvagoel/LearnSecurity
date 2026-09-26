# 3.2 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/3.2.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, mechanism, or false assurance

Four statements a reviewer might find in a pull-request description for SecureCollab's threat-model gate:

**A.** "Our SAST scan and dependency scan are both green this sprint, so the threat model is in good shape."
**B.** "The gate opens the stored threat-model document on every call and confirms `cross-tenant-read`, `hostile-browser`, and `stolen-worker` are each present with a named owner and review trigger, independent of the scanner result."
**C.** "We ran a STRIDE workshop before the quarter started and everyone agreed it was thorough."
**D.** "We added a code comment above the share-request handler noting that cross-company reads must be denied."

Sort each statement into **rule**, **mechanism**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Given a submitted threat-model document and a scanner result, decide whether the CI merge gate should pass or fail, and name which check failed.

## 2. Discrimination — which threat's coverage is actually unchecked

Four excerpts from candidate threat-model documents, each claiming all three always-name threats:

**A.** `threats: [cross-tenant-read (owner: authz, trigger: new-share-path), hostile-browser (owner: web, trigger: new-client-surface), stolen-worker (owner: platform, trigger: new-worker-identity)]`, `declared_flows: [browser-share-request, member-note-read, worker-share-redelivery]` — all three flows traced.
**B.** The same three threats, same owners and triggers, `declared_flows: [browser-share-request, member-note-read]` — `worker-share-redelivery` absent.
**C.** The same three threats and all three flows, but `stolen-worker`'s `owner` field is empty.
**D.** The same three threats and all three flows, with `stolen-worker`'s `priority` field set to `4` and a real, specific `mitigation` string.

Identify which excerpt (there may be more than one) leaves a threat's coverage claim unfalsifiable rather than merely incomplete, and explain — using this module's own vocabulary of a threat id versus a traced flow — why a threat id being present is not sufficient evidence on its own, using the specific excerpt that best demonstrates the distinction.

**Claim assessed:** C2 · **Outcome:** Given a data-flow diagram with one required flow missing, identify which always-name threat's coverage claim becomes unchecked and explain why the threat id alone was not sufficient evidence.

## 3. Diagnosis — a check that resembles the real one

```python
if all(tid in str(model) for tid in MANDATORY_IDS):
    pass
else:
    reasons.append("missing one or more mandatory threat ids")
```

This replaces `fixed/app.py`'s structural lookup against each threat's own `id` field. Construct a specific threat-model document — you do not need to write code, just describe its fields — that this check would incorrectly accept as containing all three mandatory ids, even though no actual threat entry with one of those three ids exists in the document's `threats` list. Name the root cause of why this check accepts your constructed document, the precondition under which the gap matters in practice, and the impact if this version ships — as three distinct answers, not one answer restated three times.

**Claim assessed:** C1 · **Outcome:** Given a submitted threat-model document and a scanner result, decide whether the CI merge gate should pass or fail, and name which check failed.

## 4. Diagnosis — a mitigation that looks resolved

A submitted threat model's highest-priority row reads: `{"id": "cross-tenant-read", "owner": "authz", "trigger": "new-share-path", "priority": 1, "mitigation": "pending security review"}`. Name the root cause of why this row should not pass this module's priority/mitigation check even though every field is present and non-empty, the precondition under which a reviewer might mistake this for a complete row on a casual read, and the impact of shipping a threat model whose top-priority row is unresolved in this specific way — as three distinct answers.

**Claim assessed:** C3 · **Outcome:** Given a prioritized threat list whose top-priority row has a placeholder mitigation, explain why ranking the threats did not yet produce an actionable decision, and write a real one.

## 5. Design — two candidate mechanisms under a stated constraint

Recall this module's two candidate mechanisms from `lessons/04-build.md`: (A) a merge-time gate that reads the stored model on every pull request, versus (B) a nightly batch job that audits the stored model independently of the merge path. Under the constraint that SecureCollab's team ships small, frequent pull requests roughly every fifteen minutes during business hours, and any pull request that fails CI blocks that specific developer's work until fixed, argue for one candidate over the other. Your argument must name specifically what happens under this constraint for the candidate you reject — not merely assert that it is worse in general — and must address whether a slow or occasionally-flaky audit check is more or less costly under this constraint than under the constraint `lessons/04-build.md` originally considered.

**Claim assessed:** C1, C4 · **Outcome:** Given a submitted threat-model document and a scanner result, decide whether the CI merge gate should pass or fail, and name which check failed.

## 6. Design — removing a required flow

A pull request removes `worker-share-redelivery` from `REQUIRED_FLOWS` entirely, with the description: "Decommissioning the async worker feature this quarter; removing the now-irrelevant flow requirement." Determine whether removing a required flow is, by itself, a defect — distinguish this from the case in item 2 and in `lessons/02-model.md`, where a required flow is *missing from a submission* while the underlying feature still exists — and state what this module's claims say must be true about the `stolen-worker` threat row itself before this removal ships, given that the feature it was tracking is claimed to no longer exist.

**Claim assessed:** C2, C4 · **Outcome:** Given a data-flow diagram with one required flow missing, identify which always-name threat's coverage claim becomes unchecked and explain why the threat id alone was not sufficient evidence.

## 7. Transfer — clinic SMS reminders

Complete `lessons/07-transfer.md`'s exercise: write always-name threats, required flows, a resolved top-priority mitigation, and a review trigger for the clinic SMS reminder feature, following that lesson's four success criteria.

**Success criteria:** see `lessons/07-transfer.md` §Success criteria.

**Claim assessed:** C1, C2, C3, C4 · **Outcome:** Transfer outcome in `module.yaml`.

## 8. Operate — two signals, two reason codes

Write the two distinct `missing_mandatory_threat` lines SecureCollab's gate would emit for: (a) `cross-tenant-read` present with an owner and trigger but never revisited after `new-share-path` fired, and (b) `hostile-browser` missing its `owner` field entirely. Then explain why an alert scoped to fire only when a *specific row's specific fired trigger* has no matching revisit record produces a meaningfully different false-positive rate than an alert that fires whenever *any* trigger has ever fired anywhere in the model's history, and name which of the two designs `lessons/06-operate.md` argues for and why.

**Claim assessed:** C4 · **Outcome:** Given a named review trigger that has fired, decide whether a specific threat row's re-review record satisfies it independent of any self-reported update date, and design the detection signal for a row that does not.
