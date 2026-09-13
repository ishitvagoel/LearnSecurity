def test_high_quiz_score_is_not_authorization(diagnostic) -> None:
    assert diagnostic.quiz_score_grants_phase1_skip(100) is False, (
        "a placement quiz is not a 1.2 allow cell and not Gate 1"
    )


def test_low_score_does_not_skip(diagnostic) -> None:
    assert diagnostic.quiz_score_grants_phase1_skip(0) is False


def test_missing_capabilities_get_tooling_bridges(diagnostic) -> None:
    evidence = {"python": True, "browser": False, "sql": True, "network": False, "git": False}
    assert diagnostic.bridge_recommendations(evidence) == [
        "bridge-browser",
        "bridge-network",
        "bridge-git",
    ]


def test_complete_capability_map_has_no_bridges(diagnostic) -> None:
    evidence = {name: True for name in ("python", "browser", "sql", "network", "git")}
    assert diagnostic.bridge_recommendations(evidence) == []
