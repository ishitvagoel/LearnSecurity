#!/usr/bin/env python3
"""Stable command surface for the LearnSecurity QA contract."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT_PYTHON = sys.executable
VENV_PYTHON = ROOT / ("Scripts/python.exe" if sys.platform == "win32" else ".venv/bin/python")
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.is_file() else CURRENT_PYTHON


def run(command: list[str]) -> int:
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def clean_site_build() -> None:
    # `.next` is generated cache/output, never authored content.
    shutil.rmtree(ROOT / "site" / ".next", ignore_errors=True)


def run_site(*, lint: bool, build: bool) -> int:
    if not (ROOT / "site" / "node_modules" / ".bin" / "next").is_file():
        code = run(["npm", "--prefix", "site", "ci"])
        if code:
            return code
    if lint:
        code = run(["npm", "--prefix", "site", "run", "lint"])
        if code:
            return code
    if not build:
        return 0
    clean_site_build()
    code = run(["npm", "--prefix", "site", "run", "build"])
    if code:
        return code
    clean_site_build()
    return run(["npm", "--prefix", "site", "run", "build:webpack"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("bootstrap", help="create the pinned disposable Python environment")
    doctor = sub.add_parser("doctor", help="report tool and dependency availability")
    doctor.add_argument("--profile", default="all", choices=("repo", "labs", "site", "mobile", "all"))
    doctor.add_argument("--strict", action="store_true")

    sub.add_parser("validate", help="validate curriculum metadata, links, pins, status, and exports")
    lab = sub.add_parser("lab-matrix", help="run vulnerable/fixed lab contracts")
    lab.add_argument("--module", action="append")
    lab.add_argument("--changed-only", action="store_true")
    lab.add_argument("--base-ref", default="origin/main")

    site = sub.add_parser("site", help="run the site lint and production build")
    site.add_argument("--lint-only", action="store_true")
    site.add_argument("--build-only", action="store_true")

    changed = sub.add_parser("changed", help="validate and run deep checks for changed modules")
    changed.add_argument("--base-ref", default="origin/main")
    sub.add_parser("full", help="run the complete local QA contract")
    args = parser.parse_args()

    if args.command == "bootstrap":
        return run([CURRENT_PYTHON, "scripts/bootstrap.py"])
    if args.command == "doctor":
        command = [PYTHON, "scripts/doctor.py", "--profile", args.profile]
        if args.strict:
            command.append("--strict")
        return run(command)
    if args.command == "validate":
        return run([PYTHON, "scripts/validate_repo.py", "--strict"])
    if args.command == "lab-matrix":
        command = [PYTHON, "scripts/run_lab_matrix.py"]
        for module in args.module or []:
            command.extend(["--module", module])
        if args.changed_only:
            command.extend(["--changed-only", "--base-ref", args.base_ref])
        return run(command)
    if args.command == "site":
        return run_site(lint=not args.build_only, build=not args.lint_only)
    if args.command == "changed":
        code = run([PYTHON, "scripts/validate_repo.py", "--strict"])
        if code:
            return code
        return run([PYTHON, "scripts/run_lab_matrix.py", "--changed-only", "--base-ref", args.base_ref])
    if args.command == "full":
        for command in ([PYTHON, "scripts/validate_repo.py", "--strict"], [PYTHON, "scripts/run_lab_matrix.py"]):
            code = run(command)
            if code:
                return code
        return run_site(lint=True, build=True)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
