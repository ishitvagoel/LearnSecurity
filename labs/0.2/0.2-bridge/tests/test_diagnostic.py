"""C1: no quiz score grants a Phase 1 / Gate 1 skip. C2: a tooling-bridge
skip requires the diagnostic's own gap evidence, never a job title, a
vendor certification, an LMS badge, or the absence of any diagnostic at
all. C3: modules 1.2, 1.3, and 1.4 are required for every learner,
regardless of score, a fast-track claim, or tooling-bridge assignment.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# C1 -- a quiz score, at any value, never grants a Phase 1 / Gate 1 skip.
# ---------------------------------------------------------------------------

def test_high_quiz_score_is_not_authorization(diagnostic) -> None:
    """The module's original forbidden outcome: a perfect score must not
    read as authorization to skip 1.2 or Gate 1."""
    assert diagnostic.quiz_score_grants_phase1_skip(100) is False, (
        "a placement quiz is not a 1.2 allow cell and not Gate 1"
    )


def test_low_score_does_not_skip(diagnostic) -> None:
    """Honest path: a low score also does not skip -- the function must
    not branch on the score in either direction."""
    assert diagnostic.quiz_score_grants_phase1_skip(0) is False


def test_boundary_old_vulnerable_threshold_is_still_denied(diagnostic) -> None:
    """Boundary case at the exact threshold the vulnerable file used
    (score >= 80). A repair that merely raises the threshold instead of
    removing it would still fail at 80 and pass at 79; the fixed file must
    deny both, and this is the pair most likely to expose a
    raised-not-removed threshold."""
    assert diagnostic.quiz_score_grants_phase1_skip(80) is False
    assert diagnostic.quiz_score_grants_phase1_skip(79) is False


def test_negative_score_is_malformed_and_still_denied(diagnostic) -> None:
    """Malformed input: a score that should never occur (a diagnostic
    bug, a corrupted record) must not be read as a special case that
    somehow grants the skip either."""
    assert diagnostic.quiz_score_grants_phase1_skip(-1) is False


def test_anti_fake_quiz_score_fresh_unused_value_is_denied(diagnostic) -> None:
    """Anti-fake test. A fake repair could special-case exactly the two
    values this file's other tests use (100 and 0) -- for example
    ``return score not in (100,)`` -- while leaving every other score
    branching on some other rule. This calls a value never written
    anywhere else in this file."""
    assert diagnostic.quiz_score_grants_phase1_skip(53) is False, (
        "the deny must hold for every score, not only the two values "
        "this test file happens to use elsewhere"
    )


# ---------------------------------------------------------------------------
# C2 -- a tooling-bridge skip requires the diagnostic's own gap evidence.
# ---------------------------------------------------------------------------

def test_tooling_bridge_required_for_a_genuine_gap(diagnostic) -> None:
    """Normal case: the diagnostic itself observed a gap, with no
    credential claims present at all -- the bridge is correctly
    required."""
    assert diagnostic.tooling_bridge_required({"diagnostic_gap": True}) is True


def test_tooling_bridge_not_required_when_diagnostic_finds_no_gap(diagnostic) -> None:
    """Normal case, the legitimate skip: the diagnostic ran and positively
    found no gap. This is the one case where a skip is actually earned,
    and it must still be granted -- the fix is not "never skip the
    bridge," it is "only skip on the diagnostic's own evidence.\""""
    assert diagnostic.tooling_bridge_required({"diagnostic_gap": False}) is False


def test_tooling_bridge_forbidden_outcome_job_title_does_not_override_a_real_gap(
    diagnostic,
) -> None:
    """Forbidden outcome: a job-title claim must not override the
    diagnostic's own evidence, even when that evidence says a gap is
    present. A hiring manager's badge should never be able to turn a real,
    diagnosed gap into "bridge not required.\""""
    evidence = {"job_title": "Senior Engineer", "diagnostic_gap": True}
    assert diagnostic.tooling_bridge_required(evidence) is True, (
        "a job title must not waive a bridge the diagnostic itself found necessary"
    )


def test_tooling_bridge_missing_diagnostic_fails_safe_to_required(diagnostic) -> None:
    """Malformed / failure case: no diagnostic ran at all -- an empty
    evidence record. Fail-safe defaults require this to come back as
    bridge required, not as an unearned skip."""
    assert diagnostic.tooling_bridge_required({}) is True, (
        "the absence of a diagnostic is not evidence of no gap"
    )


def test_anti_fake_tooling_bridge_a_different_credential_field(diagnostic) -> None:
    """Anti-fake test. A narrow repair might strip out only the
    ``job_title`` check (the field the forbidden-outcome test above
    exercises) while leaving ``vendor_cert`` or ``lms_badge`` still able
    to override real evidence. This calls a combination that test does
    not: a vendor-certification claim, still with a genuine diagnosed
    gap, still with a never-elsewhere-used field name (``lms_badge`` is
    also present to widen the net)."""
    evidence = {"vendor_cert": True, "lms_badge": True, "diagnostic_gap": True}
    assert diagnostic.tooling_bridge_required(evidence) is True, (
        "every credential field must be ignored, not only the one the "
        "other test happens to name"
    )


# ---------------------------------------------------------------------------
# C3 -- 1.2, 1.3, and 1.4 are required regardless of score, fast-track, or
# tooling-bridge assignment; only the bridge set may vary.
# ---------------------------------------------------------------------------

def test_phase1_modules_required_for_a_low_score_with_a_real_tooling_gap(diagnostic) -> None:
    """Normal case: a low score, a genuine Git gap. All three Phase 1
    modules are required and the bridge set names the real gap."""
    result = diagnostic.phase1_modules_for_learner(0, {"git": True})
    assert result["required"] == {"1.2", "1.3", "1.4"}
    assert result["bridge"] == {"git"}


def test_phase1_modules_forbidden_outcome_high_score_does_not_drop_1_4(diagnostic) -> None:
    """The module's own named residual, reproduced as a forbidden outcome:
    a perfect tooling score must not remove module 1.4 -- accessibility
    and usable-security reasoning -- from the required path."""
    result = diagnostic.phase1_modules_for_learner(100, {})
    assert "1.4" in result["required"], (
        "a high tooling score must not hide 1.4's accessibility residual"
    )
    assert result["required"] == {"1.2", "1.3", "1.4"}


def test_phase1_modules_boundary_at_the_old_vulnerable_threshold(diagnostic) -> None:
    """Boundary case at the exact score the vulnerable file's threshold
    used. One point on either side of 80 must make no difference to the
    required set -- if it does, a fix merely moved the threshold instead
    of removing the branch."""
    just_below = diagnostic.phase1_modules_for_learner(79, {})
    at_threshold = diagnostic.phase1_modules_for_learner(80, {})
    assert "1.4" in just_below["required"]
    assert "1.4" in at_threshold["required"], (
        "1.4 must be required at score 80, not only at 79"
    )


def test_phase1_modules_malformed_missing_tooling_diagnostic_does_not_crash(diagnostic) -> None:
    """Malformed / failure case: no tooling diagnostic was ever run
    (``tooling_gaps`` is ``None``, not an empty dict). The function must
    not raise, must still require all three Phase 1 modules, and must not
    invent a bridge unit from nothing."""
    result = diagnostic.phase1_modules_for_learner(0, None)
    assert result["required"] == {"1.2", "1.3", "1.4"}
    assert result["bridge"] == set()


def test_anti_fake_phase1_modules_fast_track_alone_does_not_drop_1_4(diagnostic) -> None:
    """Anti-fake test. A narrow repair might only remove the
    ``quiz_score >= 80`` branch while leaving the unrelated ``fast_track``
    flag still able to drop 1.4. This uses a low score (never elsewhere
    paired with ``fast_track=True`` in this file) so a fix that patches
    only the score comparison cannot pass by accident."""
    result = diagnostic.phase1_modules_for_learner(0, {}, fast_track=True)
    assert "1.4" in result["required"], (
        "a fast-track claim, on its own, must not drop 1.4 either"
    )


def test_anti_fake_phase1_modules_high_score_and_fast_track_together_does_not_drop_1_4(
    diagnostic,
) -> None:
    """Anti-fake test. Every other case in this file pairs a high score
    with ``fast_track=False`` (the default) or pairs a low score with
    ``fast_track=True`` -- never both signals present at once. A repair
    that keeps the vulnerable branch but changes its ``or`` to an ``and``
    (drop 1.4 only when the score is high AND the flag is set) would pass
    every test above, because none of them ever sets both, while still
    reproducing the module's own forbidden outcome for a learner who
    happens to have both a high score and a fast-track claim."""
    result = diagnostic.phase1_modules_for_learner(95, {}, fast_track=True)
    assert "1.4" in result["required"], (
        "a high score and a fast-track claim together must not drop 1.4 "
        "either -- an and-gated branch is a narrower version of the same "
        "defect, not a fix"
    )
