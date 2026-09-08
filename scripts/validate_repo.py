#!/usr/bin/env python3
"""Validate the repository contracts that make curriculum claims reproducible."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - exercised by the clean-bootstrap check
    raise SystemExit(
        "QA dependencies are missing. Run `python scripts/bootstrap.py` or "
        "`python -m pip install -r requirements-dev.lock` first."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
MODULE_ROOT = CONTENT / "modules"
STATUS_PATH = CONTENT / "progress" / "STATUS.yaml"
PINS_PATH = CONTENT / "standards" / "pins.yaml"
SCHEMA_PATH = CONTENT / "schema" / "module.schema.json"
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
LAB_RESET_RE = re.compile(r"git restore --source=HEAD -- labs/[^\s`]+")


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def load_yaml(path: Path, reporter: Reporter) -> object | None:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        reporter.error(f"{path.relative_to(ROOT)}: YAML could not be loaded: {exc}")
        return None


def relative_path_is_safe(path: str) -> bool:
    candidate = Path(path)
    return not candidate.is_absolute() and ".." not in candidate.parts


def module_path(module_id: str) -> Path:
    if module_id == "11":
        return MODULE_ROOT / "11" / "11"
    if module_id.startswith("E"):
        return MODULE_ROOT / "e" / module_id
    return MODULE_ROOT / module_id.split(".", 1)[0] / module_id


def lab_path(module_id: str, slug: str) -> Path:
    return ROOT / "labs" / module_id / slug


def review_artifacts(module_id: str) -> list[Path]:
    return sorted((CONTENT / "progress" / "reviews").glob(f"{module_id}-*.md"))


def source_tokens(value: object) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", str(value or "").lower()))


def canonical_pin(standard: dict, pins: list[dict]) -> tuple[dict | None, bool]:
    """Resolve a module reference to one canonical pin.

    Module references may use a deep requirement URL or a shorter display name,
    so identity is resolved by URL, well-known pin IDs, and source/version
    tokens. Version/status drift remains an error; a deep URL is reported as a
    warning by the caller rather than being mistaken for a different source.
    """
    url = standard.get("url")
    exact = [pin for pin in pins if pin.get("url") == url]
    if exact:
        return (exact[0] if len(exact) == 1 else None), True

    source = str(standard.get("source") or "").lower()
    aliases = {
        "asvs": "asvs",
        "masvs": "masvs",
        "mastg": "mastg",
        "slsa": "slsa",
        "osps": "osps",
        "cvss": "cvss",
        "cwe": "cwe",
        "nice": "nice",
    }
    for marker, pin_marker in aliases.items():
        if marker in source:
            candidates = [pin for pin in pins if pin_marker in str(pin.get("id", "")).lower()]
            if len(candidates) == 1:
                return candidates[0], False

    version = str(standard.get("version"))
    candidates = [pin for pin in pins if str(pin.get("version")) == version]
    ranked = sorted(
        [
            (
                len(source_tokens(standard.get("source")) & source_tokens(pin.get("source"))),
                pin,
            )
            for pin in candidates
        ],
        key=lambda item: item[0],
    )
    if ranked and ranked[-1][0] >= 2:
        best_score = ranked[-1][0]
        best = [pin for score, pin in ranked if score == best_score]
        if len(best) == 1:
            return best[0], False
    return None, False


def validate_module(
    path: Path,
    data: dict,
    schema_validator: Draft202012Validator,
    pins: list[dict],
    reporter: Reporter,
) -> None:
    relative = path.relative_to(ROOT)
    for issue in schema_validator.iter_errors(data):
        location = ".".join(str(item) for item in issue.absolute_path) or "<root>"
        reporter.error(f"{relative}: schema {location}: {issue.message}")

    module_id = data.get("id")
    expected_dir = path.parent.name
    if module_id != expected_dir:
        reporter.error(f"{relative}: id {module_id!r} does not match directory {expected_dir!r}")

    for learning_object in data.get("learningObjects", []) or []:
        object_path = learning_object.get("path")
        if not object_path:
            reporter.error(f"{relative}: learning object {learning_object.get('id')} has no path")
            continue
        if not relative_path_is_safe(object_path):
            reporter.error(f"{relative}: learning object path escapes its module: {object_path}")
            continue
        target = path.parent / object_path
        if not target.is_file():
            reporter.error(f"{relative}: missing learning object path {target.relative_to(ROOT)}")

    lab_spec = data.get("labSpec")
    if lab_spec:
        slug = lab_spec.get("slug")
        if not slug:
            reporter.error(f"{relative}: labSpec has no slug")
        else:
            lab = lab_path(str(module_id), slug)
            for required in ("README.md", "vulnerable", "fixed", "tests"):
                target = lab / required
                if not target.exists():
                    reporter.error(f"{relative}: missing lab artifact {target.relative_to(ROOT)}")

    for required in (path.parent / "spec.md", path.parent / "assessment" / "rubric.md"):
        if not required.is_file():
            reporter.error(f"{relative}: missing required artifact {required.relative_to(ROOT)}")
    key = CONTENT / "assessment" / "keys" / f"{module_id}.md"
    if not key.is_file():
        reporter.error(f"{relative}: missing examiner key {key.relative_to(ROOT)}")

    review_status = data.get("reviewStatus")
    status = data.get("status")
    artifacts = review_artifacts(str(module_id))
    if status == "published":
        if review_status != "completed":
            reporter.error(f"{relative}: published module must have reviewStatus=completed")
        if not data.get("reviewer") or not data.get("lastReviewedAt"):
            reporter.error(f"{relative}: published module is missing completed review metadata")
        if not artifacts:
            reporter.error(f"{relative}: published module has no dated review artifact")
    elif status in {"draft", "spec", "stub"}:
        if review_status not in {"not-requested", "requested"}:
            reporter.error(f"{relative}: draft-like module must have reviewStatus=requested or not-requested")
        if data.get("reviewer") is not None:
            reporter.error(f"{relative}: draft-like module cannot present a reviewer as completed metadata")
        if data.get("lastReviewedAt") is not None or data.get("nextReviewAt") is not None:
            reporter.error(f"{relative}: draft-like module cannot present review dates as completed review metadata")
    if data.get("lastReviewedAt") is not None and not artifacts:
        reporter.error(f"{relative}: lastReviewedAt is set without a dated review artifact")

    coverage = data.get("assessmentBlueprint") or {}
    required_coverage = {"explain", "design", "build", "break", "verify", "operate", "communicate"}
    missing_coverage = sorted(required_coverage - set(coverage))
    if missing_coverage:
        reporter.error(f"{relative}: outcome coverage is missing {', '.join(missing_coverage)}")
    if len(data.get("evidenceRequired") or []) < 3:
        reporter.error(f"{relative}: evidenceRequired must contain at least three artifacts")

    for standard in data.get("standardsRefs", []) or []:
        pin, exact_url = canonical_pin(standard, pins)
        if pin is None:
            reporter.error(
                f"{relative}: standardsRefs entry cannot resolve to a canonical pin: "
                f"{standard.get('source')} {standard.get('version')}"
            )
            continue
        if str(standard.get("version")) != str(pin.get("version")):
            reporter.error(
                f"{relative}: standardsRefs version drift for {standard.get('source')}: "
                f"module={standard.get('version')} pin={pin.get('version')}"
            )
        # `final` pins can be used as contextual `seminal` or `awareness`
        # references. Draft and unverified pins cannot be promoted by prose.
        allowed_contextual = pin.get("status") == "final" and standard.get("status") in {
            "final",
            "seminal",
            "awareness",
        }
        if not allowed_contextual and standard.get("status") != pin.get("status"):
            reporter.error(
                f"{relative}: standardsRefs status drift for {standard.get('source')}: "
                f"module={standard.get('status')} pin={pin.get('status')}"
            )
        if not exact_url:
            reporter.warning(
                f"{relative}: deep or alias standards URL/name resolved to canonical pin {pin.get('id')}; "
                "prefer the canonical pin URL in a future content pass"
            )


def validate_status(manifests: dict[str, dict], reporter: Reporter) -> None:
    status = load_yaml(STATUS_PATH, reporter)
    if not isinstance(status, dict):
        return
    entries = status.get("modules")
    if not isinstance(entries, list):
        reporter.error("content/progress/STATUS.yaml: modules must be a list")
        return
    # STATUS keeps the capstone and electives in their own historical sections;
    # they are still part of the same canonical module inventory.
    entries = list(entries)
    capstone = status.get("capstone")
    if isinstance(capstone, dict):
        entries.append(capstone)
    electives = status.get("electives")
    if isinstance(electives, list):
        entries.extend(electives)
    status_map = {str(entry.get("id")): entry for entry in entries if isinstance(entry, dict)}
    if len(status_map) != len(entries):
        reporter.error("content/progress/STATUS.yaml: module IDs must be unique")
    manifest_ids = set(manifests)
    if set(status_map) != manifest_ids:
        reporter.error(
            "content/progress/STATUS.yaml: module IDs do not match manifests: "
            f"missing={sorted(manifest_ids - set(status_map))}, "
            f"extra={sorted(set(status_map) - manifest_ids)}"
        )

    published_by_status = {mid for mid, entry in status_map.items() if entry.get("depth") == "publishable"}
    published_by_manifest = {mid for mid, data in manifests.items() if data.get("status") == "published"}
    if published_by_status != published_by_manifest:
        reporter.error(
            "publication invariant mismatch: STATUS depth=publishable "
            f"{sorted(published_by_status)} != module.yaml status=published {sorted(published_by_manifest)}"
        )

    next_config = status.get("next") or {}
    remaining = [str(item) for item in (status.get("revision") or {}).get("remaining", [])]
    next_id = next_config.get("id")
    if remaining and next_id != remaining[0]:
        reporter.error(
            "content/progress/STATUS.yaml: next.id must match revision.remaining[0] "
            f"({remaining[0]!r}); got {next_id!r}"
        )
    if remaining and not next_id:
        reporter.error("content/progress/STATUS.yaml: an active revision queue cannot have next.id=null")


def validate_links(reporter: Reporter) -> None:
    markdown_files = [ROOT / "README.md"] + sorted(CONTENT.rglob("*.md")) + sorted((ROOT / "labs").rglob("*.md"))
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "/")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                reporter.error(f"{source.relative_to(ROOT)}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                reporter.error(f"{source.relative_to(ROOT)}: broken relative link {raw_target}")


def validate_site_boundaries(reporter: Reporter) -> None:
    site_sources = sorted((ROOT / "site" / "app").rglob("*.tsx")) + sorted(
        (ROOT / "site" / "components").rglob("*.tsx")
    ) + sorted((ROOT / "site" / "lib").rglob("*.ts"))
    for source in site_sources:
        text = source.read_text(encoding="utf-8")
        if "content/assessment/keys" in text or "content\\assessment\\keys" in text:
            reporter.error(f"{source.relative_to(ROOT)}: examiner-key path appears in learner site source")

    reflection_forbidden = (
        'title="Assessments"',
        'label: "Assessments"',
        "assessment worksheet",
        "assessment worksheets",
        "Assessment —",
    )
    for source in site_sources:
        text = source.read_text(encoding="utf-8")
        for phrase in reflection_forbidden:
            if phrase.lower() in text.lower():
                reporter.error(f"{source.relative_to(ROOT)}: ungraded worksheet still labeled {phrase!r}")


def validate_lab_reset_wording(reporter: Reporter) -> None:
    for readme in sorted((ROOT / "labs").rglob("README.md")):
        text = readme.read_text(encoding="utf-8")
        if "git checkout --" in text or "git reset --hard" in text:
            reporter.error(f"{readme.relative_to(ROOT)}: destructive reset wording is not allowed")
        if "restore only this lab directory from version control" in text and not LAB_RESET_RE.search(text):
            reporter.error(f"{readme.relative_to(ROOT)}: reset guidance must include an exact git restore path")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="return non-zero for every recorded error")
    args = parser.parse_args()

    reporter = Reporter()
    if not SCHEMA_PATH.is_file():
        reporter.error(f"missing schema: {SCHEMA_PATH.relative_to(ROOT)}")
        return 1
    try:
        schema = __import__("json").loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        reporter.error(f"schema could not be loaded: {exc}")
        return 1
    pins_data = load_yaml(PINS_PATH, reporter) or {}
    pins = pins_data.get("pins", []) if isinstance(pins_data, dict) else []
    if not isinstance(pins, list):
        reporter.error("content/standards/pins.yaml: pins must be a list")
        pins = []

    manifests: dict[str, dict] = {}
    validator = Draft202012Validator(schema)
    for path in sorted(MODULE_ROOT.glob("*/**/module.yaml")):
        data = load_yaml(path, reporter)
        if not isinstance(data, dict):
            continue
        module_id = str(data.get("id"))
        if module_id in manifests:
            reporter.error(f"duplicate module id: {module_id}")
        manifests[module_id] = data
        validate_module(path, data, validator, pins, reporter)

    validate_status(manifests, reporter)
    validate_links(reporter)
    validate_site_boundaries(reporter)
    validate_lab_reset_wording(reporter)

    print(f"Validated {len(manifests)} module manifests")
    for warning in reporter.warnings:
        print(f"WARNING: {warning}")
    for error in reporter.errors:
        print(f"ERROR: {error}")
    if reporter.errors:
        print(f"Validation failed with {len(reporter.errors)} error(s)")
        return 1 if args.strict else 0
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
