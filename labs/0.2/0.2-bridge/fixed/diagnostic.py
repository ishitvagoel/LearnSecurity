def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Fixed: diagnostics never grant 1.2 cells or skip Gate 1 evidence."""
    return False
