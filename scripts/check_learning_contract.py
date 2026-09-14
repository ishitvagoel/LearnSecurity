#!/usr/bin/env python3
"""Check that learner-facing module contracts resolve before publishing the site."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "modules"
ROUTE = ROOT / "content" / "route.yaml"
PROJECT = ROOT / "content" / "reference" / "securecollab" / "milestones.yaml"
BRIDGES = ROOT / "content" / "bridges.yaml"


def module_files() -> list[Path]:
    return sorted(CONTENT.glob("*/*/module.yaml"))


def main() -> int:
    errors: list[str] = []
    manifests = module_files()
    module_ids = {str(yaml.safe_load(path.read_text(encoding="utf-8")).get("id")) for path in manifests}
    if not ROUTE.is_file():
        errors.append("content/route.yaml is missing")
    else:
        route = yaml.safe_load(ROUTE.read_text(encoding="utf-8")) or {}
        route_ids: list[str] = []
        for kind, values in (route.get("routes") or {}).items():
            if not isinstance(values, list):
                errors.append(f"route {kind}: expected a list")
                continue
            for value in values:
                value = str(value)
                route_ids.append(value)
                if value not in module_ids:
                    errors.append(f"route {kind}: unknown module {value}")
        if len(route_ids) != len(set(route_ids)):
            errors.append("content/route.yaml contains duplicate module ids")
    if not PROJECT.is_file():
        errors.append("content/reference/securecollab/milestones.yaml is missing")
    else:
        project = yaml.safe_load(PROJECT.read_text(encoding="utf-8")) or {}
        for milestone in project.get("milestones", []):
            milestone_id = str(milestone.get("id", "unknown"))
            module_id = str(milestone.get("moduleId", ""))
            if module_id and module_id not in module_ids:
                errors.append(f"milestone {milestone_id}: unknown module {module_id}")
            lab_path = milestone.get("labPath")
            if lab_path and not (ROOT / str(lab_path)).is_dir():
                errors.append(f"milestone {milestone_id}: missing lab path {lab_path}")
    bridge_ids: set[str] = set()
    if BRIDGES.is_file():
        bridge_data = yaml.safe_load(BRIDGES.read_text(encoding="utf-8")) or {}
        bridge_entries = bridge_data.get("bridges", []) if isinstance(bridge_data, dict) else []
        if not isinstance(bridge_entries, list):
            errors.append("content/bridges.yaml: bridges must be a list")
        else:
            for bridge in bridge_entries:
                if not isinstance(bridge, dict) or not bridge.get("id"):
                    errors.append("content/bridges.yaml: every bridge needs an id")
                    continue
                bridge_id = str(bridge["id"])
                if bridge_id in bridge_ids:
                    errors.append(f"content/bridges.yaml: duplicate bridge id {bridge_id}")
                bridge_ids.add(bridge_id)
                for field in ("title", "task", "success", "retry"):
                    if not str(bridge.get(field, "")).strip():
                        errors.append(f"content/bridges.yaml: {bridge_id} has no {field}")
    else:
        errors.append("content/bridges.yaml is missing")
    for manifest in manifests:
        module = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        module_id = str(module.get("id", manifest.parent.name))
        declared_paths: set[Path] = set()
        for obj in module.get("learningObjects", []):
            rel = obj.get("path")
            if not rel:
                errors.append(f"{module_id}: learning object {obj.get('id')} has no path")
                continue
            target = manifest.parent / rel
            declared_paths.add(target.resolve())
            if not target.is_file():
                errors.append(f"{module_id}: missing learning object {rel}")
            if target.suffix == ".md":
                body = target.read_text(encoding="utf-8")
                if re.search(r"Deferred to Pass [A-E]|Pass A per blueprint|phase1/lab-1\.1-local-hashed", body):
                    errors.append(f"{module_id}: authoring or stale lab reference in {rel}")
                for bridge_id in re.findall(r"\(/bridges/([^/]+)/\)", body):
                    if bridge_id not in bridge_ids:
                        errors.append(f"{module_id}: unknown bridge destination {bridge_id}")
        for prerequisite in module.get("prerequisites", []):
            if "Pass A" in str(prerequisite):
                errors.append(f"{module_id}: production pass leaked into prerequisite: {prerequisite}")
        build_hint = str(module.get("assessmentBlueprint", {}).get("build", ""))
        if "Deferred to Pass" in build_hint:
            errors.append(f"{module_id}: deferred build instruction remains in assessment metadata")
        if module_id == "1.1" and module.get("status") == "published":
            errors.append("1.1: must be independently re-reviewed before returning to published")
        lesson_dir = manifest.parent / "lessons"
        if lesson_dir.is_dir():
            for lesson in lesson_dir.glob("*.md"):
                if lesson.resolve() not in declared_paths:
                    errors.append(f"{module_id}: lesson is not declared in learningObjects: {lesson.name}")
    status_file = ROOT / "content" / "progress" / "STATUS.yaml"
    if status_file.is_file():
        status = yaml.safe_load(status_file.read_text(encoding="utf-8")) or {}
        queue = {str(item) for item in (status.get("revision", {}).get("remaining", []) or [])}
        status_entries = status.get("modules", []) or []
        for entry in status_entries:
            if not isinstance(entry, dict):
                continue
            module_id = str(entry.get("id", ""))
            if entry.get("depth") == "map-complete" and module_id and module_id not in queue:
                errors.append(f"{module_id}: map-complete module missing from revision.remaining")
    if errors:
        print("Learning contract check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Learning contract OK: {len(manifests)} modules, route ids, milestone paths, and all declared learning objects resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
