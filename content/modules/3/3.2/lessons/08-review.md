# Reviewing a candidate fix that reintroduces the scanner shortcut

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

`labs/3.2/3.2-lab/review/candidate_fix.py` is a snapshot of a hypothetical pull request against `fixed/app.py`. The author's description reads: "Closed the missing-cross-tenant-read gap the auditor flagged last sprint, and added the new client-portal request flow to the required-flow list." Read that description the way a reviewer should read any pull-request description in this course: as a claim about what changed, to be checked against the diff, not as a summary you can approve without reading the code underneath it. A description that names a real, specific fix ("closed the missing-cross-tenant-read gap") is more persuasive than a vague one, and persuasiveness is not evidence.

```python
def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    reasons: list[str] = []

    if scanner_green:
        return {"gate": "pass", "reasons": [], "scanner_extra_findings": list(scanner_findings)}

    if all(tid in str(model) for tid in MANDATORY_IDS):
        pass
    else:
        reasons.append("missing one or more mandatory threat ids")

    declared_flows = set(model.get("declared_flows", []))
    missing_flows = REQUIRED_FLOWS - declared_flows
    if missing_flows:
        reasons.append(f"declared flows do not trace: {sorted(missing_flows)}")

    return {
        "gate": "pass" if not reasons else "fail",
        "reasons": reasons,
        "scanner_extra_findings": list(scanner_findings),
    }
```

## A reading order, not a checklist

Reading a diff top to bottom, in file order, teaches you the order the author wrote it in — which is rarely the order that reveals whether the fix is correct. This module's property is about which code path actually executes and what it actually reads, so read in that order instead: first, find every point where the function can return before its later lines run; second, for the code that does run, ask what it actually checks against, not what its surrounding comment or variable name suggests it checks; third, compare what this version claims to require against what the previous version required, line by line, rather than assuming a diff that adds something never quietly removes something else; fourth, ask whether the check that resolves the security-relevant decision is structurally sound, or whether it merely resembles a sound check on casual reading.

Apply the first step to this diff before anything else, because [`lessons/03-break.md`](03-break.md)'s entire property is about exactly this kind of line. Find the `return` statement. It is still there, in the same position, in this candidate fix as in the original vulnerable fixture — decide for yourself, before checking `content/assessment/keys/3.2.md`, whether the author's description ("closed the missing-cross-tenant-read gap") is consistent with a function whose scanner-green branch still returns before any of the model-reading code below it can execute for the overwhelming majority of pull requests, which is to say the ones with a green scan.

Apply the second step to the mandatory-id check specifically. The line reads `if all(tid in str(model) for tid in MANDATORY_IDS)`, and the surrounding structure — an `if`/`else`, a `reasons.append` on the failing branch — looks exactly like the shape [`lessons/04-build.md`](04-build.md)'s fixed implementation uses. Ask what `tid in str(model)` actually tests: is it checking that a threat entry with that `id` field exists in the `threats` list, or is it checking whether that exact substring appears *anywhere* in the model's string representation — including inside an unrelated field's free text? Construct, mentally or on paper, a model where the answer to those two questions differs, and decide what that difference would let through.

Apply the third step to `REQUIRED_FLOWS`. The author's description says a new flow was *added*; confirm, by comparing the full contents of the set in this file against the full contents in `fixed/app.py`, whether anything already present was also *removed* in the same change, and if so, whether the description mentioned that removal at all.

Apply the fourth step to the function's overall shape now that you have answers to the first three: given what you found, does this candidate fix actually restore the property [`lessons/01-property.md`](01-property.md) states, or does it restore a narrower version of it that happens to pass a casual read? Answering this step honestly sometimes means concluding that a diff fixes exactly one of several problems while leaving the module's property just as false as before for a different reason — a correct answer to "did this PR help" and a correct answer to "does this PR make the property true" are not always the same answer, and a reviewer who only asks the first question can approve a PR that genuinely improves on its predecessor while still leaving the merge gate exploitable by the same class of pull request that motivated writing this gate in the first place.

This reading order generalizes past this one diff. A review that starts from "what does the code actually execute, in what order, for the common case" before asking "does this look like the kind of code that fixes the problem" is the discipline [9.2's secure code review module](../../../9/9.2/spec.md) will build on directly — data flow, authority, and control flow first, plausibility second. Applying it here, to a diff about a threat-model gate rather than about authorization or injection, is itself a small piece of evidence for the claim that a reading order grounded in what code does, rather than in what a specific vulnerability class looks like, transfers across very different kinds of security-relevant code.

## A plausible non-issue, named as a question rather than an answer

The stored model global in this file is named `_CURRENT_MODEL`, where `fixed/app.py` names the equivalent global `_MODEL`. A rename with no behavioral effect is the kind of change a reviewer skimming a diff for something to comment on will sometimes flag out of habit — "why rename this mid-PR, does it touch anything else" — and asking that question is not unreasonable review practice in general. Decide, specifically for *this* diff and *this* module's property, whether that question is worth spending review time on relative to the four steps above, and be able to say why. A review that spends its comments on a cosmetic rename while missing a `return` statement that defeats the entire mechanism has optimized for finding *something*, not for finding the thing that matters.

## What this lesson does not tell you

This lesson does not state which of the reading order's four steps surfaces a genuine defect, how many defects this diff contains, or what severity each one carries. `content/assessment/keys/3.2.md` records the intended findings, their severities, and the misconception each one encodes, for use after you have formed your own answer — reading it first defeats the exercise. Do not run `candidate_fix.py`; it exists only as a reading artifact and is not wired into `conftest.py` or the test suite.

## What this lesson is not doing

This lesson does not authorize applying this candidate fix to any running system, real or fictional beyond this fixture, and does not authorize treating any real pull request, real vendor's product, or real CI configuration as equivalent to this exercise.
