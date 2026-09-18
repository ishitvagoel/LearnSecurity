"""Fixed placement-diagnostic predicates. See README.md for the full
structural-fix rationale for each of the three functions below (C1-C3).
The shared shape: refuse to let a signal from outside the diagnostic (a
score, a credential claim, an unrelated flag) answer a question only the
diagnostic's own observation -- or the honest absence of one -- may
answer.
"""

from __future__ import annotations

REQUIRED_PHASE1_MODULES = frozenset({"1.2", "1.3", "1.4"})


def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Fixed: diagnostics never grant 1.2 cells or skip Gate 1 evidence."""
    return False


def tooling_bridge_required(evidence: dict) -> bool:
    """Fixed: only a genuine diagnostic-observed tooling gap can waive the
    bridge unit. A job title, vendor certification, or LMS badge is not
    diagnostic evidence and is never read. A record that never ran a
    diagnostic at all (no ``diagnostic_gap`` key) fails safe to ``True``:
    deny the skip unless the authority for it -- a real diagnostic
    result -- is positively established."""
    if "diagnostic_gap" not in evidence:
        return True
    return bool(evidence["diagnostic_gap"])


def phase1_modules_for_learner(
    quiz_score: int,
    tooling_gaps: dict | None = None,
    fast_track: bool = False,
) -> dict:
    """Fixed: 1.2, 1.3, and 1.4 are required for every learner, regardless
    of quiz score or a fast-track claim. Only genuine tooling-gap evidence
    adds a bridge unit, and a bridge unit is additive -- it can never
    remove a Phase 1 module from the required set."""
    gaps = tooling_gaps or {}
    bridge = {name for name, gap in gaps.items() if gap}
    return {"required": set(REQUIRED_PHASE1_MODULES), "bridge": bridge}
