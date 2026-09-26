# Local fixture: a green scan passes an incomplete threat model

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Deriving the failure before running anything

Start from what the gate is supposed to guarantee and work forward to the exact line where that guarantee breaks, rather than starting from the broken line and working backward. [`lessons/01-property.md`](01-property.md)'s claim requires the gate to open the stored threat-model document on every call and check five things: presence of the always-name ids, an owner and trigger on each, flow coverage for `stolen-worker`'s dependency, a real mitigation on the top-priority row, and a recorded re-review for any fired trigger. For that guarantee to fail, exactly one precondition has to hold: some code path has to reach a `return` statement before the model is read. It does not matter whether the rest of the function is correct, thorough, or well-tested past that point, because a `return` on an earlier line makes everything after it unreachable for the common case.

`vulnerable/app.py`'s `evaluate_gate` has that precondition built in structurally, not as an edge case:

```python
def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    if scanner_green:
        return {"gate": "pass", "reasons": [], "scanner_extra_findings": list(scanner_findings)}
    threats = model.get("threats", [])
    ...
```

The exact step where the guarantee breaks is the first line of the function body: `if scanner_green: return ...`. Every pull request whose scanner run happens to be green — which, for a codebase without an active, unpatched dependency vulnerability, is most pull requests most days — takes this branch and never reaches `model.get("threats", [])` at all. The blast radius of this one line is total for the always-name set: it is not that `cross-tenant-read` is checked incorrectly, or checked with a bug in the comparison; it is that no code anywhere on this path ever looks at whether `cross-tenant-read` exists. A model missing all three always-name ids, with every owner field blank and every trigger unset, produces byte-for-byte the same gate response as a complete, current, correctly prioritized model, provided the scanner is green in both cases. Nothing about *this specific pull request's diff* has to be malicious for the failure to occur; a model that was accidentally left incomplete when the fixture was first written passes identically to one built with care.

## Where you may practice

Run this only inside `labs/3.2/3.2-lab/`. Every threat id, owner name, and flow name in the fixture is synthetic; nothing here reaches a scanner tenant, a vendor dashboard, or a system outside this directory.

## What the failing test shows, and what it does not

```bash
python3 -m pytest labs/3.2/3.2-lab/tests --impl vulnerable
```

`test_green_scanner_missing_cross_tenant_read_fails` submits a threat-model document with `cross-tenant-read` removed entirely — the other two always-name ids, all flows, priorities, and mitigations left intact and correct — then calls the gate with `scanner_green=True`. Against the vulnerable fixture, this test fails, and the failure means exactly one thing: the gate returned `"gate": "pass"` for a threat model that a human reading the same document would immediately recognize as missing its most important row. The test does not merely check that the gate *sometimes* returns `fail`; it checks that removing one specific, always-name id from an otherwise-complete model produces no observable change in the gate's decision when the scanner is green, which is the precise shape of "the model was never consulted."

Six other tests fail against this fixture for the same underlying reason, each isolating a different consequence of the same unreached code: a mandatory threat with no owner still passes (`test_mandatory_threat_without_owner_fails`), a model whose diagram never traces the worker-redelivery path still passes even though every id is nominally present (`test_untraced_worker_flow_fails_even_with_all_ids_present`), a top-priority threat whose mitigation field is the literal placeholder `"TBD"` still passes (`test_top_priority_threat_without_real_mitigation_fails`), a threat with no priority field at all still passes (`test_missing_priority_field_fails`), a fired review trigger with no recorded re-review still passes (`test_fired_trigger_without_revisit_fails`), and the anti-fake test showing that even a *partial* fix that revisits one threat sharing a trigger name but not another still needs to be caught — which the vulnerable fixture, reading none of this, obviously cannot catch. Two tests pass against the vulnerable fixture: a fully compliant model still gates green (because a correct model was never the problem), and scanner findings still appear as additive extras (because the vulnerable fixture happens to pass those through regardless of anything else). Those two passing tests are not evidence the fixture is safe; they are evidence that a test suite has to include normal-case tests specifically so that a reviewer can tell the difference between "this fixture is broken everywhere" and "this fixture is broken in the one place that matters."

## Why this is the smallest representative failure

This fixture deliberately leaves out several things a real CI integration would need, and each omission is chosen because including it would not change where or why the failure occurs. There is no real scanner integration — `scanner_green` is a boolean the test passes directly — because the failure is in what the gate *does* with that boolean, not in how the boolean is produced; a real SAST tool feeding a real green result into this same `evaluate_gate` function would trigger the identical short-circuit. There is no persistent database behind the stored model — it lives in a module-level dictionary reset between tests — because the failure is in the gate's read path, not in how or where the model is stored; a Postgres-backed model store sitting behind the identical `if scanner_green: return` would fail identically. There is no real git history or pull-request integration, because the failure occurs entirely within one function call and does not depend on how that call gets triggered. Each omission removes infrastructure the failure does not depend on, and none of them removes the one precondition the failure does depend on: a `return` statement that executes before the model is read.

## What comes next

[`lessons/04-build.md`](04-build.md) derives the fix by removing the shortcut without removing the scanner signal — `scanner_green` remains part of the response, but no longer decides whether the model gets read. [`lessons/05-verify.md`](05-verify.md) proves the fix holds against a model that looks compliant on a casual read but fakes one specific check, including the anti-fake case this lesson only named. [`lessons/06-operate.md`](06-operate.md) turns "the model went stale and nobody noticed" into a signal that names the missing id without ever carrying a note body or session token in the alert.

## What this lesson is not doing

This lesson does not authorize connecting a real scanner product, a real CI pipeline, or any system other than the local fixture to reproduce this failure. Copy-paste exploit payloads have no place here because there is no payload: the failure is an early `return`, not an injected string, and the lesson's entire content is showing that a completely unremarkable-looking function can fail this way without any attacker-supplied input at all.
