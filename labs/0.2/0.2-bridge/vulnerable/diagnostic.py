"""Vulnerable placement-diagnostic predicates.

Three independent defects, one per function, all sharing the same root
cause class: a signal that was never Gate 1 evidence gets treated as
though it were.

``quiz_score_grants_phase1_skip`` (C1) lets a high tooling-quiz score stand
in for the authority map, trust-boundary diagram, and risk register that
modules 1.2/1.3/1.4 actually require.

``tooling_bridge_required`` (C2) lets a credential from a different
authority -- a job title, a vendor certification claim, or an LMS
"mastery" badge -- waive a Git/SQL/HTTP bridge unit even when the
diagnostic itself never observed the underlying skill, and treats "no
diagnostic ran at all" the same as "the diagnostic found no gap."

``phase1_modules_for_learner`` (C3) lets the same high score (or an
unrelated "fast_track" flag) silently drop module 1.4 from a learner's
required path -- the adaptive-path-hides-1.4 residual named in this
module's own spec, reproduced here as a real, testable function instead
of only a review-trigger sentence.
"""

from __future__ import annotations

REQUIRED_PHASE1_MODULES = frozenset({"1.2", "1.3", "1.4"})


def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Vulnerable: a diagnostic percentage is treated as 1.2 authorization."""
    return score >= 80


def tooling_bridge_required(evidence: dict) -> bool:
    """Vulnerable: a job title, vendor certification, or LMS mastery badge
    can waive a tooling bridge unit even when no diagnostic ever ran, and
    an evidence record that never ran a diagnostic at all (no
    ``diagnostic_gap`` key) is treated the same as one that positively
    found no gap."""
    if evidence.get("job_title") or evidence.get("vendor_cert") or evidence.get("lms_badge"):
        return False
    if "diagnostic_gap" not in evidence:
        return False
    return bool(evidence["diagnostic_gap"])


def phase1_modules_for_learner(
    quiz_score: int,
    tooling_gaps: dict | None = None,
    fast_track: bool = False,
) -> dict:
    """Vulnerable: a high score, or an unrelated fast-track claim, drops
    module 1.4 from the required set. Only the required set is affected;
    the bridge set is computed correctly here, which is precisely what
    makes the 1.4 drop easy to miss on a skim -- the tooling logic looks
    right because it is."""
    gaps = tooling_gaps or {}
    required = set(REQUIRED_PHASE1_MODULES)
    if quiz_score >= 80 or fast_track:
        required.discard("1.4")
    bridge = {name for name, gap in gaps.items() if gap}
    return {"required": required, "bridge": bridge}
