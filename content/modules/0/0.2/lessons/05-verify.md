# A green suite proves the deny fired, not that placement is fair

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** NIST CSF 2.0 (final) `DE`/`RS` as outcome labels for what "verified" means operationally here — a passing test is a Detect-shaped signal, not a Respond- or Recover-shaped one, and this course's own Gate 1 evidence rules govern what counts as the actual artifact.

Fifteen tests exercise three functions, and each function gets the same four-case shape before an anti-fake test closes it out: a normal case that should pass honestly, this claim's forbidden outcome, a boundary case at the exact value the vulnerable file's threshold used, and a malformed-input case. Reading them in that order matters, because a suite that only ever runs the forbidden-outcome case cannot tell a real fix from a fix that special-cases that one input.

## The four cases, and what distinguishes a real pass from a lucky one

For `quiz_score_grants_phase1_skip`, the normal case (`score=0`) passing is nearly worthless on its own — a function that always returns `True` would fail it, but so would nearly any function, so it barely discriminates. The forbidden-outcome case (`score=100`) passing is the one that matters, and the boundary case (`score=79` and `score=80` both denied) is what tells you whether a "fix" merely raised the threshold instead of removing it: a repair that changed `>= 80` to `>= 101` would still fail the forbidden-outcome test at `score=100`... but would pass it at a slightly higher score the suite does not happen to try, which is exactly why the anti-fake test exists here at all, calling a fresh value (`53`) neither the normal nor the forbidden-outcome case uses.

For `tooling_bridge_required`, the case that actually distinguishes a real fix from a plausible fake is the forbidden-outcome test: `{"job_title": "Senior Engineer", "diagnostic_gap": True}` must return `True`, because a version that merely swapped which credential fields it checks — say, checking only `vendor_cert` and forgetting `job_title` — would still pass a test that only tried the fields it kept checking. The malformed case (an empty evidence dict, `{}`) checks the opposite failure mode: a "fix" that removes the credential short-circuit but leaves the missing-key case defaulting to `False` (bridge not required) has fixed C2's stated defect while leaving a quieter version of the same shape — "no evidence" read as "evidence of safety" — sitting one line away.

For `phase1_modules_for_learner`, the boundary case is doing real work for a reason specific to this function: `quiz_score=79` already passed before any fix, because 79 never triggered the vulnerable `discard`, so a suite that only checked 79 could look green against a completely unrepaired function. Checking `80` — the exact value the bug fires on — is what turns "the fix works for scores the bug didn't touch anyway" into "the fix removed the bug."

## What a green suite still does not prove

Passing all fifteen tests proves that these three functions, called with these arguments, never let a score, a credential, or a fast-track flag reach a skip or a required-set shrink. It does not prove the diagnostic that calls these functions is wired correctly — a caller that ignores `tooling_bridge_required`'s return value entirely and grants the skip anyway would leave every test here green while reproducing the exact forbidden outcome one layer up. It does not prove the quiz itself is a fair or accurate measure of anything; this module's claims do not depend on the quiz being good, only on its score never being read as Gate 1 evidence. And it does not prove [Claim 4](02-model.md) or [Claim 5](06-operate.md) hold, since neither is code-tested here at all — a reviewer who sees fifteen green tests and stops has verified three of this module's five claims, not five.

This gap is worth stating in the reviewer's own words rather than only in the suite's, because it is exactly the mistake this module's own C1 forbids in a different guise: reading a green pytest run as though it were the reviewed evidence Gate 1 actually requires is a number standing in for an artifact, the same category error a quiz score commits. Fifteen passing assertions are real evidence that three specific functions behave as specified on the inputs this file tries; they are not evidence that a learner who wrote them understands why the credential check had to be removed rather than merely reordered, and a rubric that stops at "the tests are green" has quietly reintroduced the module's own forbidden shape into its own verification step.

## The anti-fake tests, named against the fakes they reject

`test_anti_fake_quiz_score_fresh_unused_value_is_denied` rejects a fix of the shape `return score not in (100,)` — technically denying the one score this file's other tests happen to try, while leaving every other score free to branch on some other rule a later edit could add. `test_anti_fake_tooling_bridge_a_different_credential_field` rejects a fix that strips out the `job_title` check specifically but leaves `vendor_cert` or `lms_badge` still able to override real diagnostic evidence — verified by hand: constructing exactly that incomplete fix and running the suite against it produces fourteen passes and one failure, on this test alone. `test_anti_fake_phase1_modules_fast_track_alone_does_not_drop_1_4` rejects a fix that removes the `quiz_score >= 80` branch but leaves `fast_track` still able to discard `"1.4"` on its own — the same hand-verification, fourteen passes and one failure, on this test alone.

## The abuse case this suite is built to survive

A hurried learner or a manager motivated to get a skip granted will not try one credential field and stop; they will try combinations, because the first one that works is all they need. `test_anti_fake_tooling_bridge_a_different_credential_field` is written with exactly that abuse pattern in mind — it supplies `vendor_cert` and `lms_badge` together, not because a real evidence record would plausibly carry both, but because a fix that closes the `job_title` path while leaving either of the other two open is precisely the outcome an actor trying several fields in sequence would find. A suite that tested only the field named in the module's own forbidden-outcome sentence would pass a fix that is abuse-resistant against a reader who tries the obvious field once, and fails one that tries the two the lesson did not name first.

## Run it

```text
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
python3 -m pytest labs/0.2/0.2-bridge/tests --impl fixed
```

The first command shows eight failures across the three forbidden-outcome, boundary, and anti-fake cases described above. The second shows all fifteen passing. If your own edit to the fixed file makes both commands pass identically, you have not fixed anything — you have made the deny disappear from both variants, and the suite's job is to catch exactly that by disagreeing between them.
