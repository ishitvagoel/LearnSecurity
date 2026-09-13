from __future__ import annotations


def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Vulnerable: a diagnostic percentage is treated as 1.2 authorization."""
    return score >= 80


def bridge_recommendations(evidence: dict[str, bool]) -> list[str]:
    """Vulnerable: the diagnostic drops capability gaps instead of assigning bridges."""
    return []
