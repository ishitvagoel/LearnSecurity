"""Tests for the Module 1.1 local invariant-catalogue lab."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys

import yaml

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from catalogue_validator import (  # noqa: E402
    find_live_target_urls,
    is_mechanism_only,
    validate_catalogue,
)


def test_selected_catalogue_is_semantically_reviewable(claim_path: Path) -> None:
    data = yaml.safe_load(claim_path.read_text(encoding="utf-8"))
    errors = validate_catalogue(data)
    assert not errors, "catalogue review failed:\n- " + "\n- ".join(errors)


def test_mechanism_slogan_is_rejected() -> None:
    assert is_mechanism_only("We are secure because we use TLS")
    assert not is_mechanism_only(
        "Tenant note bodies must remain absent from application log events"
    )


def test_public_target_is_rejected_but_local_lab_is_allowed() -> None:
    value = {
        "allowed": "http://127.0.0.1:8000/catalogue",
        "forbidden": "https://production.example.org/api",
    }
    assert find_live_target_urls(value) == ["https://production.example.org/api"]


def test_field_presence_alone_does_not_pass() -> None:
    shallow = {
        "system": "SecureCollab",
        "authorizedScope": "local synthetic course fixture",
        "syntheticDataOnly": True,
        "claims": [
            {
                "id": f"SC-CONF-0{number}",
                "property": "We are secure because we use TLS",
            }
            for number in range(1, 6)
        ],
    }
    errors = validate_catalogue(shallow)
    assert any("mechanism slogan" in error for error in errors)
    assert any(".evidence" in error for error in errors)


def test_field_complete_but_causally_shallow_claim_does_not_pass() -> None:
    fixed_path = LAB_ROOT / "fixed" / "security_claim.yaml"
    data = yaml.safe_load(fixed_path.read_text(encoding="utf-8"))
    shallow = deepcopy(data)
    shallow["claims"][0]["property"] = "We are secure because we use TLS"
    shallow["claims"][0]["evidence"]["negative"] = ["middleware exists"]

    errors = validate_catalogue(shallow)
    assert any("mechanism slogan" in error for error in errors)
    assert any("control presence is not property evidence" in error for error in errors)


def test_five_padded_duplicate_rows_do_not_pass() -> None:
    """Anti-fake: a catalogue that hits every field-presence rule by copying
    one generic, non-SecureCollab-specific claim under five different ids
    must not pass. This is the defect found while reviewing this lab for the
    module's deepening pass: no trigger phrase from MECHANISM_ONLY_PHRASES
    appears anywhere, every required list and text field is non-empty, and
    every evidence mode has at least one item, so the pre-existing checks
    were blind to it. The signature check added alongside this test is what
    the real fixture's five genuinely distinct rows must still pass."""

    def padded_claim(number: int) -> dict:
        return {
            "id": f"SC-FILL-0{number}",
            "property": "Notes must never leak to an outsider",
            "assets": ["notes"],
            "attackers": ["a bad actor"],
            "trust": ["the server"],
            "untrusted": ["the client"],
            "timeHorizon": "during use",
            "preconditions": ["something happens"],
            "mechanisms": ["a policy check"],
            "mechanismLimits": ["some limit exists"],
            "forbiddenOutcomes": ["notes leak somehow"],
            "evidence": {
                "normal": ["thing works"],
                "negative": ["thing is denied"],
                "abuse": ["thing is tried and fails"],
                "failure": ["thing breaks safely"],
            },
            "detection": {
                "signal": "something odd happens",
                "threshold": "some threshold",
                "eventFields": ["a", "b"],
                "prohibitedFields": ["note body", "password", "token"],
                "failureBehavior": "fails closed somehow",
            },
            "recovery": ["do something", "do something else"],
            "residualRisk": "some risk remains",
            "nonGoals": ["not doing something"],
            "reviewTriggers": ["something changes"],
        }

    padded = {
        "system": "SecureCollab",
        "authorizedScope": "local synthetic course fixture",
        "syntheticDataOnly": True,
        "claims": [padded_claim(n) for n in range(1, 6)],
    }
    errors = validate_catalogue(padded)
    assert any("duplicate" in error for error in errors), (
        "field-presence-complete but content-identical rows must be rejected:\n- "
        + "\n- ".join(errors or ["(no errors -- the fake passed)"])
    )

    # The real fixed fixture's five rows are genuinely distinct and must not
    # trip the same check -- this is the guard against the fix itself being
    # too aggressive and rejecting a legitimate catalogue.
    fixed_path = LAB_ROOT / "fixed" / "security_claim.yaml"
    real = yaml.safe_load(fixed_path.read_text(encoding="utf-8"))
    real_errors = validate_catalogue(real)
    assert not any("duplicate" in error for error in real_errors), real_errors
