#!/usr/bin/env python3
"""Run local vulnerable/fixed lab contracts with setup failures separated."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
MODULE_RE = re.compile(r"(?:content/modules/[^/]+/([^/]+)/|labs/([^/]+)/)")


@dataclass
class Result:
    module: str
    variant: str
    state: str
    returncode: int
    command: list[str]
    output: str


def discover_labs() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for tests in sorted(LABS.glob("*/**/tests")):
        if not tests.is_dir() or not (tests.parent / "conftest.py").is_file():
            continue
        module_id = tests.parts[-3]
        found[module_id] = tests.parent
    return found


def changed_modules(base_ref: str) -> set[str]:
    command = ["git", "diff", "--name-only", f"{base_ref}...HEAD"]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.returncode:
        result = subprocess.run(["git", "diff", "--name-only", "HEAD^", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False)
    modules: set[str] = set()
    for path in result.stdout.splitlines():
        match = MODULE_RE.search(path)
        if match:
            modules.add(match.group(1) or match.group(2))
    return modules


def command_for(lab: Path, variant: str) -> list[str]:
    tests = lab / "tests"
    if (lab / "conftest.py").read_text(encoding="utf-8").find("--claim") >= 0:
        claim = lab / variant / "security_claim.yaml"
        return [sys.executable, "-m", "pytest", str(tests), "--claim", str(claim)]
    return [sys.executable, "-m", "pytest", str(tests), "--impl", variant]


def is_setup_failure(result: subprocess.CompletedProcess[str]) -> bool:
    if result.returncode == 5:
        return True
    output = f"{result.stdout}\n{result.stderr}".lower()
    markers = (
        "error collecting",
        "importerror",
        "modulenotfounderror",
        "file or directory not found",
        "unrecognized arguments",
        "no tests ran",
    )
    return any(marker in output for marker in markers)


def run_variant(module_id: str, lab: Path, variant: str) -> Result:
    command = command_for(lab, variant)
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    output = (completed.stdout + completed.stderr).strip()
    if is_setup_failure(completed):
        state = "setup-failure"
    elif variant == "fixed":
        state = "fixed-pass" if completed.returncode == 0 else "fixed-failure"
    else:
        state = "vulnerable-detected" if completed.returncode != 0 else "vulnerable-not-detected"
    return Result(module_id, variant, state, completed.returncode, command, output[-4000:])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", action="append", help="run only this module; repeat for multiple modules")
    parser.add_argument("--changed-only", action="store_true")
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    labs = discover_labs()
    selected = set(args.module or labs)
    if args.changed_only:
        selected &= changed_modules(args.base_ref)
    missing = sorted(selected - set(labs))
    results: list[Result] = []
    for module_id in sorted(selected):
        if module_id in missing:
            continue
        lab = labs[module_id]
        results.append(run_variant(module_id, lab, "vulnerable"))
        results.append(run_variant(module_id, lab, "fixed"))

    if args.as_json:
        print(json.dumps([asdict(item) for item in results], indent=2))
    else:
        print(f"Lab matrix: {len(selected)} module(s)")
        for result in results:
            print(f"[{result.state:22}] {result.module} {result.variant}")
            if result.state not in {"vulnerable-detected", "fixed-pass"}:
                print(result.output)

    if missing:
        print(f"ERROR: no lab discovered for module(s): {', '.join(missing)}")
        return 1
    failures = [item for item in results if item.state not in {"vulnerable-detected", "fixed-pass"}]
    if failures:
        print(f"Lab matrix failed with {len(failures)} unexpected result(s)")
        return 1
    print("Lab matrix passed: every vulnerable fixture was detected and every fixed fixture passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
