#!/usr/bin/env python3
"""Report the tools needed to work on LearnSecurity.

The doctor distinguishes required tools for a selected workflow from optional
platform tools. It never installs anything and is safe to run from any cwd.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Check:
    name: str
    command: str | None
    required: bool
    available: bool
    detail: str


def command_detail(command: str) -> tuple[bool, str]:
    executable = shutil.which(command)
    if not executable:
        return False, "not found on PATH"
    try:
        result = subprocess.run(
            [executable, "--version"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return True, f"{executable} (version check failed: {exc})"
    output = (result.stdout or result.stderr).strip().splitlines()
    return True, f"{executable} ({output[0] if output else 'version unavailable'})"


def module_detail(module: str) -> tuple[bool, str]:
    spec = importlib.util.find_spec(module)
    if spec is None:
        return False, "not installed in this Python environment"
    return True, str(spec.origin or "available")


def build_checks(profile: str) -> list[Check]:
    wants_repo = profile in {"repo", "labs", "all"}
    wants_site = profile in {"site", "all"}
    wants_mobile = profile in {"mobile", "all"}
    checks: list[Check] = []

    python_ok = sys.version_info >= (3, 11)
    checks.append(
        Check(
            "Python >= 3.11",
            None,
            True,
            python_ok,
            f"{sys.executable} ({sys.version.split()[0]})",
        )
    )
    if wants_repo or wants_site or wants_mobile:
        try:
            pip = subprocess.run(
                [sys.executable, "-m", "pip", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            pip_ok = pip.returncode == 0
            pip_detail = (pip.stdout or pip.stderr).strip() or "pip unavailable"
        except (OSError, subprocess.SubprocessError) as exc:
            pip_ok, pip_detail = False, str(exc)
        checks.append(Check("pip", f"{sys.executable} -m pip", True, pip_ok, pip_detail))

    if wants_repo or wants_site:
        for command, required in (("node", wants_site), ("npm", wants_site)):
            available, detail = command_detail(command)
            checks.append(Check(command, command, required, available, detail))

    optional_commands = (("psql", "PostgreSQL client"), ("java", "Java"))
    for command, label in optional_commands:
        available, detail = command_detail(command)
        checks.append(Check(label, command, False, available, detail))

    browsers = ("chromium", "chromium-browser", "google-chrome", "firefox")
    browser = next((candidate for candidate in browsers if shutil.which(candidate)), None)
    checks.append(
        Check(
            "Browser",
            browser,
            False,
            browser is not None,
            shutil.which(browser) if browser else "no supported browser found",
        )
    )

    if wants_mobile:
        for command, label in (("adb", "Android adb"), ("sdkmanager", "Android sdkmanager")):
            available, detail = command_detail(command)
            checks.append(Check(label, command, True, available, detail))
    else:
        for command, label in (("adb", "Android adb"), ("sdkmanager", "Android sdkmanager")):
            available, detail = command_detail(command)
            checks.append(Check(label, command, False, available, detail))

    if wants_repo or wants_site:
        for module in ("yaml", "jsonschema", "pytest"):
            available, detail = module_detail(module)
            checks.append(Check(f"Python package: {module}", None, wants_repo, available, detail))
    if wants_repo:
        available, detail = module_detail("cryptography")
        checks.append(Check("Python package: cryptography", None, False, available, detail))

    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile",
        choices=("repo", "labs", "site", "mobile", "all"),
        default="all",
        help="workflow to check; optional platform tools remain informational",
    )
    parser.add_argument("--strict", action="store_true", help="fail when a required check is unavailable")
    parser.add_argument("--json", action="store_true", dest="as_json", help="emit machine-readable JSON")
    args = parser.parse_args()

    checks = build_checks(args.profile)
    if args.as_json:
        print(json.dumps([asdict(check) for check in checks], indent=2))
    else:
        print(f"LearnSecurity doctor — profile={args.profile}")
        print(f"repository: {ROOT}")
        for check in checks:
            marker = "OK" if check.available else ("MISSING" if check.required else "optional")
            print(f"[{marker:8}] {check.name}: {check.detail}")

    failures = [check for check in checks if check.required and not check.available]
    if failures and args.strict:
        print("\nMissing required prerequisites:")
        for failure in failures:
            print(f"- {failure.name}: {failure.detail}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
