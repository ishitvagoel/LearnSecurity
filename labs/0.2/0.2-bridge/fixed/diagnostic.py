from __future__ import annotations

CAPABILITY_BRIDGES = {
    "python": "bridge-python",
    "browser": "bridge-browser",
    "sql": "bridge-sql",
    "network": "bridge-network",
    "git": "bridge-git",
}


def quiz_score_grants_phase1_skip(score: int) -> bool:
    """Diagnostics never grant 1.2 cells or skip Gate 1 evidence."""
    return False


def bridge_recommendations(evidence: dict[str, bool]) -> list[str]:
    """Return deterministic tooling bridges for capabilities not demonstrated."""
    return [
        bridge_id
        for capability, bridge_id in CAPABILITY_BRIDGES.items()
        if evidence.get(capability) is not True
    ]
