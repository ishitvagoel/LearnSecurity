from __future__ import annotations

from pathlib import Path

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--claim", action="store")


@pytest.fixture
def claim_path(request: pytest.FixtureRequest) -> Path:
    value = request.config.getoption("--claim")
    assert value, "pass --claim path/to/security_claim.yaml"
    return Path(value)
