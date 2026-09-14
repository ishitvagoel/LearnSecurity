from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--impl", choices=("fixed", "vulnerable"), default="fixed")


@pytest.fixture
def impl(request: pytest.FixtureRequest):
    name = request.config.getoption("--impl")
    path = Path(__file__).parents[1] / name / "app.py"
    spec = importlib.util.spec_from_file_location(f"m1_{name}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    app = module.SecureCollabM1()
    yield app
    app.close()
