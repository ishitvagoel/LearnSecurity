# Review a placement-diagnostic change before it merges

**Kind:** code-review
**Loop step:** 5 Verify (seeded review)

## What you are reviewing

`labs/0.2/0.2-bridge/vulnerable/diagnostic.py` is presented to you as a pull request: "Placement diagnostic — adds tooling-bridge credential support and fast-track routing." The PR description says the change lets an experienced hire's credentials count toward a tooling-bridge decision, and adds a `fast_track` option "for learners who are clearly ready to move faster," while leaving the core `quiz_score_grants_phase1_skip` check "as before, since that logic hasn't changed." Your job is to decide whether that description is a complete and accurate account of what the code in front of you actually does, using only the four questions below and the file itself — not by reading `fixed/diagnostic.py`, and not by treating this module's other lessons as an answer key someone left open for you.

## The four questions

1. **What would falsify the PR's claim that `quiz_score_grants_phase1_skip` "hasn't changed"?** State the exact call and expected return value that would prove or disprove it, then trace that call against the actual source in front of you — not against your memory of what an earlier version did. "Hasn't changed" is a claim about history, and question 1 asks whether the *current* behavior is correct regardless of how long it has looked this way.

2. **What does `tooling_bridge_required` actually check, versus what "lets credentials count toward a tooling-bridge decision" implies?** List every key the function reads from `evidence`, every comparison it makes, and every return path, in the order the code actually executes them. The description says credentials "count toward" a decision, which sounds additive — one more input among several. Does the code actually add a credential's weight to the diagnostic's own evidence, or does it let a credential *replace* that evidence outright, before the diagnostic's own field is even read? Those are different claims, and only one of them matches "counts toward."

3. **Construct a specific evidence record where the description and the actual behavior disagree.** Pick a concrete `evidence` dict — for example, one with `job_title` set and `diagnostic_gap` set to `True` — and trace `tooling_bridge_required` on it by hand. Then pick a concrete `(quiz_score, tooling_gaps, fast_track)` triple for `phase1_modules_for_learner` and trace it the same way. Write down the exact inputs that produce a disagreement between what the PR describes and what the code returns; "this seems like it could be risky" is a feeling, not a finding, and a finding without exact inputs cannot be checked by anyone who reads your review afterward.

4. **What would you ask the author to change, and what test would prove the change is real?** For each finding from question 3, state the specific code change and the specific test call — inputs and expected output — that fails today, against the file exactly as it stands, and passes after that change and no other. A requested change with no accompanying test can be satisfied by code that merely looks fixed, which is precisely the trap this module's own anti-fake tests exist to close for its lab, and precisely the trap a review that skips this question reopens.

## One line in this PR that is not a finding

`gaps = tooling_gaps or {}` inside `phase1_modules_for_learner` looks, on a fast read, like the same class of silent-default problem `tooling_bridge_required`'s missing-key handling has — a `None` quietly becoming something else. It is not: `tooling_gaps` genuinely has no meaningful content when it is `None` (no tooling diagnostic ran at all), and treating "no diagnostic" as "no observed gaps" is correct here, because this line only ever feeds `bridge` — an additive, evidence-gated set — never `required`, which this file (correctly, in this respect) never lets any argument shrink. Flagging this line as a defect on pattern-matching alone, without tracing which set it actually feeds, is exactly the mistake question 2 exists to prevent — and reviewers who have just read [Claim 3](04-build.md)'s missing-key discussion for a different function are the ones most likely to over-apply it here.

## What a rushed review accepts, and why each one fails question 3

Rejecting these requires actually tracing the code, not recognizing them as familiar phrases:

- "The description says the score check hasn't changed, so it must be fine" — treats an unverified claim about history as evidence about the present; question 1 asks you to falsify it, not to accept its framing.
- "Credentials 'count toward' the decision, so this is just weighting, not overriding" — restates the PR's own framing without tracing which return path a credential-bearing call actually takes.
- "`fast_track` is clearly meant for cases where it's obviously fine" — "obviously fine" is not a precondition the code checks; the function accepts the flag from any caller, for any reason, and question 3 asks what happens when that reason is wrong.
- "This is just a placement quiz, so the stakes are low enough not to trace it carefully" — the [transfer lesson](07-transfer.md)'s clinic scenario exists precisely because this evidence-source shape recurs at higher stakes; treating this instance as low-stakes enough to skim is how the pattern goes unrecognized later.

## Practice

Write your answers to questions 1 through 4 before running any command. Then run:

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
```

Compare the actual failures to your question-3 predictions. A finding you predicted that the suite does not actually test is a gap in the lab, worth naming; a failure the suite reports that you did not predict is a gap in your review, worth naming for the opposite reason.

## Use it somewhere new

Apply the same four questions to a PR description for a clinic's hiring-diagnostic change that claims a vendor certification "should reasonably count toward" skipping the architecture threat-model review. [Lesson 07](07-transfer.md)'s claims are exactly the list of things "should reasonably count toward" needs to actually mean before that sentence is evidence rather than a slogan.

## What this page is not doing

Do not treat a real learner's diagnostic record, a real vendor's certificate, or a real hiring decision as this exercise's subject. Assign an owner to any finding you cannot immediately fix, and do not close it on a promise alone. Answer keys are not on this site.
