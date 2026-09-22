# Lab 0.2 — a diagnostic score is not Gate 1 evidence

**Module:** `0.2`
**Authorized scope:** this directory only. Local course fixture. No live LMS, vendor-quiz, or cert-portal targets.
**Tier:** 1 (predicate). All three functions are pure over plain `int`/`dict`/`bool` arguments, with no request cycle or persisted state any of the three claims below depends on. See `lab-realism.mdc`.

**Invariant (C1):** `quiz_score_grants_phase1_skip(score)` is `False` for every score. A diagnostic percentage never authorizes skipping modules 1.2, 1.3, or 1.4, or Gate 1.
**Invariant (C2):** `tooling_bridge_required(evidence)` is decided only by the diagnostic's own `diagnostic_gap` observation. A job title, vendor certification, or LMS badge must never waive the bridge, and an evidence record with no diagnostic result at all fails safe to `True` (bridge required).
**Invariant (C3):** `phase1_modules_for_learner(...)`'s `required` set is always `{"1.2", "1.3", "1.4"}`. No score, fast-track flag, or bridge assignment may remove a Phase 1 module from it; only the separate `bridge` set may vary.
**Root cause class:** a signal from outside the diagnostic — a score threshold, a credential claim, an unrelated flag — answering a question only the diagnostic's own observation (or its absence) may answer.
**Non-goals:** live LMS/vendor-quiz/cert-portal attacks, real learner PII, an actual Gate 1 evidence review implementation.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/0.2/0.2-bridge`.

## Vulnerable behavior (local only)

`quiz_score_grants_phase1_skip` returns `score >= 80` — a percentage stands in for the authority map, trust-boundary diagram, and risk register modules 1.2–1.4 actually require.

`tooling_bridge_required` returns `False` (bridge waived) whenever `job_title`, `vendor_cert`, or `lms_badge` is truthy, before ever looking at `diagnostic_gap` — a credential from a different authority overrides the diagnostic's own evidence, even when that evidence says a gap is present. A record with no `diagnostic_gap` key at all (no diagnostic ran) also returns `False`, treating "we never checked" the same as "we checked and found nothing."

`phase1_modules_for_learner` discards `"1.4"` from the required set whenever `quiz_score >= 80` or `fast_track` is truthy — the adaptive-path-hides-1.4 residual named in this module's own spec, reproduced here as a real function instead of only a review-trigger sentence. The `bridge` set is computed correctly in the same function, which is what makes the `1.4` drop easy to miss on a skim.

## Structural fix

`quiz_score_grants_phase1_skip` has no code path that reads `score` in a comparison at all — it returns `False` unconditionally, so there is no threshold left to raise by mistake later.

`tooling_bridge_required` reads only `diagnostic_gap`. The three credential fields are never inspected — not checked and then overridden, simply never read. A missing `diagnostic_gap` key fails safe to `True` (fail-safe defaults: deny the skip unless the diagnostic's own authority for it is positively established), rather than defaulting to the most trusting answer.

`phase1_modules_for_learner` always returns `set(REQUIRED_PHASE1_MODULES)` for `required`; no argument to the function can change that assignment. `bridge` remains a separate, additive set computed only from `tooling_gaps`.

## Verify

```bash
python3 -m pytest tests --impl vulnerable   # 8 of 15 fail
python3 -m pytest tests --impl fixed        # 15 of 15 pass
```

From the repository root:

```bash
python3 -m pytest labs/0.2/0.2-bridge/tests --impl vulnerable
python3 -m pytest labs/0.2/0.2-bridge/tests --impl fixed
```

Fifteen tests across three functions: for each, a normal case, the module's forbidden outcome, a boundary case at the vulnerable file's old threshold, a malformed/failure case, and an anti-fake test that uses values or field combinations never written elsewhere in the file.

Verified against two actual fakes (by hand, restoring `vulnerable/diagnostic.py` afterward): a `tooling_bridge_required` that strips only the `job_title` check but leaves `vendor_cert`/`lms_badge` still able to override real evidence passes 14 of 15 tests, failing exactly `test_anti_fake_tooling_bridge_a_different_credential_field`. A `phase1_modules_for_learner` that removes only the `quiz_score >= 80` branch but leaves `fast_track` still able to drop `"1.4"` also passes 14 of 15, failing exactly `test_anti_fake_phase1_modules_fast_track_alone_does_not_drop_1_4`.

## Operate

Signal `phase1_skip_denied` with the learner id and the module id requested; never the quiz's item text or answer content — see [`lessons/06-operate.md`](../../../content/modules/0/0.2/lessons/06-operate.md). Audit the skipped-module list on every cohort export. Do not back-date Gate 1.

## Transfer

Vendor cert used to skip a threat-model review. Clinic onboarding quiz. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/0/0.2/lessons/07-transfer.md).
