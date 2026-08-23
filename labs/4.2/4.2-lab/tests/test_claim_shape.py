"""Fail mechanism slogans; pass property-shaped claims. Local fixture only."""

from pathlib import Path

REQUIRED = ("property", "attacker", "trust", "timeHorizon", "evidence")
ASSET = 'authentication'


def test_claim_is_property_shaped(claim_path: Path) -> None:
    import yaml

    data = yaml.safe_load(claim_path.read_text())
    assert isinstance(data, dict), "claim must be a mapping"
    missing = [key for key in REQUIRED if not str(data.get(key, "")).strip()]
    assert not missing, f"missing property-shaped fields: {missing}"
    blob = " ".join(str(data.get(key, "")).lower() for key in REQUIRED)
    assert ASSET in blob, "invariant must name this module's concern"
