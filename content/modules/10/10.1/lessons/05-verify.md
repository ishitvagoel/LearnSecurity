# A broken merge check must fail the empty-change test

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

A CODEOWNERS file does not require a threat-model id. Maturity Level 3 is a score. `merge_ok({})` has to be false, and `{"threat_model": "TM-12"}` may merge. Broken: the empty change still returns true. Repair refuses a change with no threat-model id. Do not merge in a live GitHub org.

## Picture: a broken merge check must fail the empty-change test

Merge can succeed on `{}` even when every other test is green.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: empty change merges]
  X["repaired files --impl fixed"] --> P[Must pass: empty change is deny]
```

Green on both sides means `threat_model` was never the failing case.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | `{"threat_model": "TM-12"}` → may merge (may pass on both) |
| Wrong input | `{}` → not merge; empty threat-model change must fail merge |
| Abuse | Unsure or empty ids are deny (fail closed; leftover if not in this check) |
| Not claimed | A live GitHub org; Gate 10; a maturity score; that TM-12 covers this change |

`test_merge_requires_threat_model_id` exists because a `merge_ok` that always returns true would ship.

A change that already cites `TM-12` can still look fine. Deny a change with no threat-model id. If the broken files do not fail `test_merge_requires_threat_model_id`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/10.1/10.1-lab/tests --impl vulnerable
python3 -m pytest labs/10.1/10.1-lab/tests --impl fixed
```

A `CODEOWNERS` file in the repo is not `merge_ok({})`. This practice never opens a live GitHub org.

## What the checks do not prove

- That TM-12’s listed files include this change’s paths (3.2 owns quality)
- That the author may cite that id
- An unverified “secure by design” page as a product
- Extra advanced software-lifecycle evidence about documenting dangerous functions
- Gate 10 or M4 complete

## Practice

Call `merge_ok({})`. A `CODEOWNERS` file is review routing, not the threat-model id.

## Use it somewhere new

HIPAA training complete is a course tile, not a threat-model id on the change. Do not use a live GitHub org.

## What this page is not doing

A live org screenshot is not a threat-model id on the change. Do not log GitHub tokens. Answer keys are not on this site. This page does not finish check-in 10.
