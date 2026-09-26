from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parent


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--impl", action="store", required=True, choices=("vulnerable", "fixed"))


def _load(name: str):
    path = ROOT / name / "app.py"
    spec = importlib.util.spec_from_file_location(f"impl_app_{name}", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def client(request: pytest.FixtureRequest):
    """A fresh FastAPI TestClient, wired to whichever variant --impl
    names, with fresh module-level state for every test."""
    name = request.config.getoption("--impl")
    mod = _load(name)
    mod.reset()
    return TestClient(mod.create_app())
