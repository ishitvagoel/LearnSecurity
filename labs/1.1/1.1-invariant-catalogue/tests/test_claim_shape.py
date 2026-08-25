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
