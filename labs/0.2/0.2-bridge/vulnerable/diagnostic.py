def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Vulnerable: a diagnostic percentage is treated as 1.2 authorization."""
    return score >= 80
