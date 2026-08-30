from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parent


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--impl",
        action="store",
        required=True,
        choices=("vulnerable", "fixed"),
        help="select the intentionally vulnerable or structurally fixed local fixture",
    )


@pytest.fixture
def surface(request: pytest.FixtureRequest) -> ModuleType:
    name = request.config.getoption("--impl")
    path = ROOT / name / "surface.py"
    spec = importlib.util.spec_from_file_location(f"boundary_surface_{name}", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def surface_source(request: pytest.FixtureRequest) -> str:
    name = request.config.getoption("--impl")
    return (ROOT / name / "surface.py").read_text(encoding="utf-8")
