from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest
from fastapi.testclient import TestClient

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
def impl(request: pytest.FixtureRequest) -> ModuleType:
    """Load vulnerable/app.py or fixed/app.py as a fresh module per test, so
    each test gets its own FastAPI app object and its own on-disk SQLite
    file -- no state leaks between tests, and none of these tests can pass
    by accident because an earlier test already inserted the row."""
    name = request.config.getoption("--impl")
    path = ROOT / name / "app.py"
    spec = importlib.util.spec_from_file_location(f"lab24_{name}_app", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.reset()
    return mod


@pytest.fixture
def client(impl: ModuleType) -> TestClient:
    return TestClient(impl.app)
