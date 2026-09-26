# Seed, trace, and prioritize: building the CI gate

**Kind:** design-exercise
**Loop step:** 4 Build

## Predicting the fix from the property

[`lessons/01-property.md`](01-property.md)'s claim names exactly what has to become true: the gate must open the stored model on every call and check presence, ownership, flow coverage, prioritized mitigation, and trigger-based re-review, none of it contingent on the scanner's result. [`lessons/03-break.md`](03-break.md) located the failure at one line: an early `return` that fires whenever `scanner_green` is `True`. A reader who has followed both lessons should be able to predict the shape of the fix before reading it: remove the early `return`, keep the scanner's result as one field of the response rather than the only field read, and make every one of the five checks execute unconditionally. That prediction is correct, and the interesting engineering work is not in that one-sentence description — it is in choosing *how* the five checks are structured so that a plausible variation of "check the model" does not quietly recreate a narrower version of the same failure.

`fixed/app.py`'s `evaluate_gate` executes all five checks every time, appending a reason string for each failure it finds rather than stopping at the first one, so a reviewer reading the gate's response can see every problem in a submission at once rather than fixing one and discovering the next on a second pull request:

```python
def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    reasons: list[str] = []
    by_id = _threats_by_id(model)
    missing_mandatory = [tid for tid in MANDATORY_IDS if tid not in by_id]
    if missing_mandatory:
        reasons.append(f"missing mandatory threat id(s): {sorted(missing_mandatory)}")
    ...
    return {"gate": "pass" if not reasons else "fail", "reasons": reasons, ...}
```

`scanner_green` still appears in the function's signature and still appears in the response — removing it would throw away a real, useful signal about a different question — but no line of the function's logic branches on its value before the five checks run. The scanner's result becomes what [`lessons/01-property.md`](01-property.md) already argued it should be: additional information, never a substitute.

## Two candidate mechanisms, and where the weaker one breaks

A merge-time gate that reads the model on every pull request is not the only reasonable way to catch this failure, and a competent engineer reviewing this module's problem statement might propose a genuinely different, defensible alternative: keep the scanner-based merge check exactly as it was, and add a separate **nightly batch job** that opens every project's stored threat model independently and files a ticket if any of the five properties fails. This alternative has real strengths worth naming honestly. It decouples the audit from the merge path entirely, so a slow or flaky audit can never block a developer's pull request, and it can afford to run a more thorough, more expensive check than anything acceptable to run synchronously on every merge.

The alternative breaks on the axis this module's property cares about most: **when** the failure is caught, not **whether** it is caught eventually. A threat model that regresses — a teammate accidentally deletes the `cross-tenant-read` row while reorganizing the file, and the scanner happens to be green on that particular pull request — merges immediately under the batch-audit design, and stays merged, unreviewed, and unenforced for however long the interval between nightly runs is. If the interval is 24 hours, that is 24 hours during which every subsequent pull request builds on a codebase whose threat model quietly stopped naming one of its three always-name threats, and nothing in the merge path itself gave anyone a chance to notice before shipping. Worse, a nightly job that runs unattended for months accumulates exactly the operator-failure risk [`lessons/06-operate.md`](06-operate.md) names directly: a ticket nobody triages is indistinguishable, from the system's perspective, from a check that was never run at all. A merge-time gate fails loudly, in the one place a human is already looking — the pull request itself — at the one moment before the regression becomes the new normal. This module's chosen mechanism is the merge-time gate specifically because "a threat model regressed and nobody noticed for a day" is not an acceptable answer to "how does the model stay current," even though the batch-audit alternative is a reasonable, honestly-motivated design a real team might otherwise choose for a different property.

## Where the chosen mechanism itself stops working

A merge-time gate that reads the model correctly still rests on assumptions this lesson should not let stand unexamined. It assumes the gate's own code has not itself been tampered with — a compromised CI configuration that swaps `fixed/app.py` for `vulnerable/app.py`, or that patches out the five checks, defeats this mechanism entirely and invisibly, which is why [`lessons/01-property.md`](01-property.md) named CI/pipeline integrity as [10.2's residual](../../../10/10.2/spec.md), not this module's to close. It also assumes that a human filled in `mitigation`, `owner`, and `trigger` honestly — the gate can confirm a mitigation string is not the literal word `"TBD"`, but it cannot confirm that "deny-by-default check in 4.4's `can_read` matrix" describes a mechanism that actually exists and actually works, only that *some* non-placeholder text was written. That gap is not a bug in this lesson's gate; it is the boundary between what an automated check can verify from the outside and what still requires a human reviewer or a separate implementation test — [`lessons/05-verify.md`](05-verify.md) states this limit explicitly rather than letting a green gate imply more than it proves.

## Framework default versus application guarantee

FastAPI, and the JSON body-parsing machinery underneath it, will happily accept `{"mitigation": ""}` as a perfectly well-typed request: the field is present, it is a string, and nothing about the HTTP framework's own validation has any opinion about whether an empty string is a *meaningful* mitigation. If this module's gate were built on the assumption that "the request parsed without a 422" is equivalent to "the submission is complete," a pull request could ship a threat model whose every field technically exists — every key present, every value a string — while every mitigation field is empty, and the framework's own request validation would have nothing to say about it. The check that actually catches this, `mitigation in _PLACEHOLDER_MITIGATIONS` (which includes the empty string, `"tbd"`, `"pending"`, and a handful of other common placeholders, checked case-insensitively), is an **application guarantee** this module's own code has to supply, because no general-purpose web framework can know, for this specific field, what a real answer is supposed to look like versus what a placeholder looks like. The same distinction holds for `revisited_after`: FastAPI validates that the field, if present, is a list of strings; it has no opinion about whether the *specific* string a fired trigger names appears in that specific threat's own list, which is exactly the check [`lessons/01-property.md`](01-property.md)'s claim C4 depends on and exactly the check a framework's request-validation layer was never going to provide for free.

## What comes next

[`lessons/05-verify.md`](05-verify.md) proves this fix holds against nine test cases, including two that specifically target a plausible-but-wrong shortcut rather than a straightforwardly broken implementation. [`lessons/06-operate.md`](06-operate.md) designs the detection signal for the case this build lesson only named as a limit: a `revisited_after` entry that was added honestly versus one added as a rubber stamp, and what a system can and cannot tell about the difference from the outside.

## What this lesson is not doing

This lesson does not claim the nightly-batch alternative is always the wrong design for every property — for a property where catching a regression within a day is genuinely acceptable, batch auditing is a reasonable, lower-friction choice, and naming it as "wrong" without qualification would misrepresent a real engineering trade-off as a beginner's mistake. It is the wrong design for *this* property specifically, because this module's claim is about a merge-time gate that must not let a scanner result substitute for reading the model, and a batch job answers a different question on a different clock.
