from __future__ import annotations
import importlib.util
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parent
MODULE = "stest.py"
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--impl", action="store", required=True, choices=("vulnerable", "fixed"))
@pytest.fixture
def impl(request: pytest.FixtureRequest):
    name = request.config.getoption("--impl")
    path = ROOT / name / MODULE
    spec = importlib.util.spec_from_file_location("impl", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "reset"):
        mod.reset()
    return mod
