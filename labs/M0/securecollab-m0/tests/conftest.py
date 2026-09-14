from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parent.parent


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--impl", action="store", required=True, choices=("vulnerable", "fixed"))


@pytest.fixture
def app(request: pytest.FixtureRequest):
    name = request.config.getoption("--impl")
    path = ROOT / name / "app.py"
    spec = importlib.util.spec_from_file_location(f"m0_{name}", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # Dataclasses with postponed annotations resolve their module through
    # sys.modules while the dynamically loaded fixture is being executed.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    instance = module.SecureCollabM0()
    try:
        yield instance
    finally:
        instance.close()
