# Watch three placement decisions fail for three related reasons

**Kind:** mechanism-lab
**Loop step:** 3 Break

A diagnostic that hands out a Phase 1 skip does not fail by being attacked. It fails by being asked a question it was never built to answer, and answering anyway. Trace the vulnerable fixture's three functions in the order a real placement flow would call them, and each failure follows from the same precondition: some input reaches a decision it was never observed to justify.

`quiz_score_grants_phase1_skip`'s precondition is simplest — the function reads `score` in a comparison at all. The exact step where it goes wrong is `return score >= 80`: at `score = 100`, that comparison evaluates `True`, and the caller reads `True` as "this learner may skip Phase 1." The blast radius is a learner who never produces the authority map, trust-boundary diagram, or risk register [modules 1.2 through 1.4](../../../1/1.2/lessons/01-property.md) require, proceeding into later modules that assume those artifacts exist.

`tooling_bridge_required`'s precondition is that its `evidence` dict contains a `job_title`, `vendor_cert`, or `lms_badge` key with a truthy value. The exact step is `if evidence.get("job_title") or evidence.get("vendor_cert") or evidence.get("lms_badge"): return False` — a single boolean check, evaluated before the function ever looks at `diagnostic_gap`. Feed it `{"job_title": "Senior Engineer", "diagnostic_gap": True}` — a case where the diagnostic *did* observe a real gap — and the function still returns `False`, because the credential check short-circuits before the observed evidence is read at all. The blast radius: a real, diagnosed Git or SQL gap goes unaddressed, not because the diagnostic missed it, but because a title on a form outranked it.

`phase1_modules_for_learner`'s precondition is `quiz_score >= 80` or `fast_track` being true. The exact step is `required.discard("1.4")`, executed unconditionally inside that branch. The blast radius is the residual this module's own spec names directly: an adaptive path that looks correct — it still computes `bridge` accurately from real tooling evidence — while quietly removing accessibility and usable-security reasoning from a fast learner's required path, for a reason (tooling speed) that has nothing to do with what 1.4 teaches. Concretely, a learner who scores well on Git and SQL but has never once had to reason about a coerced user's residual risk, or a recovery flow that fails a keyboard-only reviewer, is routed straight past the one module built to teach exactly that — and the routing decision that did it never mentions accessibility, coercion, or residual risk anywhere in its own logic, which is what makes this class of bug hard to catch by reading the function's name alone.

## Where you may practice

Run this only inside `labs/0.2/0.2-bridge/`. The scores, credential claims, and tooling-gap flags in the fixture are synthetic; none of them is a real learner record, a real vendor certificate, or a real LMS credential.

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
```

Eight of fifteen tests fail. Read `test_high_quiz_score_is_not_authorization`'s failure first: it asserts `quiz_score_grants_phase1_skip(100) is False` and the vulnerable file returns `True`, which is not a crash — it is the function doing exactly what it was written to do, on an input it should never have been asked to grant anything for. Then read `test_tooling_bridge_forbidden_outcome_job_title_does_not_override_a_real_gap`'s failure: it is the credential short-circuit described above, caught with a real `diagnostic_gap: True` in the same call so there is no ambiguity about whether a gap existed. Then `test_phase1_modules_forbidden_outcome_high_score_does_not_drop_1_4`: a call with `quiz_score=100` and an empty `tooling_gaps` dict returns a `required` set missing `"1.4"` — the assertion failure shows the actual set, `{"1.2", "1.3"}`, sitting where `{"1.2", "1.3", "1.4"}` belongs.

## Reading the failures in the wrong order

A tempting shortcut is to run the whole suite once, see eight red lines, and treat the count as the finding. That fails as an exercise for the same reason a scanner's finding count fails as evidence elsewhere in this course: a number tells you how many assertions disagreed with the code, not which of this module's three evidence-source rules each disagreement actually violates, and two of the eight failures below trace back to the same `phase1_modules_for_learner` defect from different angles (a boundary case and an anti-fake case), so counting lines overstates how many distinct causes are present. Read each failure's assertion message against the claim it is written to test, in the order the three functions above were introduced, and the eight collapse into exactly three causes — one per function — which is the number that actually matters for deciding what to fix.

## What the smallest representative failure leaves out, and why that is fine

This fixture has no HTTP layer, no database, and no real quiz UI. That is a deliberate, not a lazy, omission: none of the three failures above depends on how the score, the credential claim, or the tooling-gap observation arrived — they depend only on what each function does once it has the value. A version of this fixture wrapped in a FastAPI endpoint would fail in exactly the same three places, for exactly the same three reasons, with the network layer adding nothing to the cause and considerable noise to the lesson. What the fixture does keep, because it is load-bearing: three independent functions, each answering one question, so that a fix to one cannot be mistaken for a fix to another — which is precisely the discrimination [lessons/02-model.md](02-model.md) asked you to make by hand before running anything.

## What this page is not doing

This lesson does not attack a real LMS, a vendor's certification portal, or a hiring platform, and it does not ask you to. Do not treat a fake fixture's score, badge, or gap flag as though it were evidence about a real person. Passing these three broken assertions is not the exercise; naming, for each one, which of this module's evidence-source rules it violates is.
