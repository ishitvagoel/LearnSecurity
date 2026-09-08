#!/usr/bin/env python3
"""Create the repository's disposable QA environment from the lock file."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def venv_python(path: Path) -> Path:
    return path / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venv", type=Path, default=ROOT / ".venv", help="disposable environment path")
    parser.add_argument("--offline", action="store_true", help="do not contact a package index")
    args = parser.parse_args()
    env_path = args.venv.expanduser().resolve()
    print(f"Creating or reusing QA environment: {env_path}")
    venv.EnvBuilder(with_pip=True, clear=False).create(env_path)
    python = venv_python(env_path)
    command = [str(python), "-m", "pip", "install", "--requirement", str(ROOT / "requirements-dev.lock")]
    if args.offline:
        command[4:4] = ["--no-index"]
    subprocess.run(command, cwd=ROOT, check=True)
    print(f"Bootstrap complete. Run {python} scripts/qa.py validate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
