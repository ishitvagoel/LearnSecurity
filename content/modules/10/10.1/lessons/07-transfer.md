# Same idea when clinic HIPAA training counts as a merge

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic that treats “HIPAA training complete” as enough to merge**.

`merge_ok({})` must be false. For a clinic, empty change is deny; a threat-model id may merge. A training checkbox is still a belief, not a threat model.

An EHR-lite “CODEOWNERS plus annual HIPAA training so we merge identity changes,” plus a maturity score on a slide.

## Picture: same check, clinical training

Calling it “chart” instead of “note” does not move the work. Surfaces, threat-model id, and leftover change. Marking HIPAA training complete does not put `threat_model` on the change.

| Notes app | Clinic sketch |
|---|---|
| Empty change must not merge | Empty change must not merge |
| `merge_ok({})` | `merge_ok({})` on local practice files |
| Schedule pressure | Same actor — **not** a live clinic |
| `{"threat_model": "TM-12"}` may merge | Same dict on the local practice files |
| CODEOWNERS is who clicks | CODEOWNERS plus a training checkbox |

```mermaid
flowchart LR
  Train[HIPAA training done] --> Belief[safe to merge]
  Empty[no threat_model] --> Reality["identity surface without 3.2"]
```

If training is complete while `merge_ok` is always true, the rule is gone. CODEOWNERS, a maturity score, and a “secure by design” pledge do not put `threat_model` on the change. This topic is **cite a threat-model id**; 3.2 is **write the model**. Training without `merge_ok` produces binders. `merge_ok` without 3.2 produces citations of empty documents. You need both. A later draft of the design-review guide stays a draft. An unverified manufacturer-ownership page stays unverified.

An empty change still has to be denied. TM-12 may still merge. Turning on CODEOWNERS without a merge check leaves `merge_ok({})` true. The local check is `test_merge_requires_threat_model_id` — on a practice, not a live GitHub org.

Also name the exception path (E6): an exception still names the missing threat model and when it expires.

## Write this for a clinic HIPAA training as merge

1. who can act (schedule pressure — not a live clinic);
2. what you trust (the merge check is the promise; CODEOWNERS, training, and a maturity score are not);
3. what must not happen (`merge_ok({})` true);
4. a test idea on **local** practice files only (no live GitHub org);
5. leftover (stale threat-model id, vanity ticket counts, exceptions without expiry);
6. whether a human merge path exists (must say which surface needs a threat-model id).

Use fake labels. Do not use real patient names. Also name the E6 exception path.

## What is not good enough

| Reject | Why |
|---|---|
| “CODEOWNERS” | Who clicks, not what changed |
| Live GitHub org | Course rules |
| “Secure by design certified” | The pin is unverified; not `merge_ok` |
| “Maturity Level 3” as `merge_ok` | Measurement, not the check |
| “Gate 10 is complete” | Forbidden stamp |
| “Later draft certified” | Still a draft |

## Practice

One page. No answer keys. `labs/10.1/10.1-lab` is the only running system you may break. Do not change a live org.

## What this page is not doing

Do not run live-org merge rules. Do not auto-generate threat models. Do not use real patient charts. This page does not finish Gate 10 or M4.
