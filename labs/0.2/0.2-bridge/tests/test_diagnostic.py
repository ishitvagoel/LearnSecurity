def test_high_quiz_score_is_not_authorization(diagnostic) -> None:
    assert diagnostic.quiz_score_grants_phase1_skip(100) is False, (
        "a placement quiz is not a 1.2 allow cell and not Gate 1"
    )
