from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

from scripts.run_lab_matrix import discover_labs


ROOT = Path(__file__).resolve().parents[1]


def test_status_and_manifests_agree_on_the_published_reference_set() -> None:
    status = yaml.safe_load((ROOT / "content/progress/STATUS.yaml").read_text())
    published_from_status = {
        str(entry["id"])
        for entry in status["modules"]
        if entry.get("depth") == "publishable"
    }
    published_from_manifests = set()
    for path in (ROOT / "content/modules").glob("*/**/module.yaml"):
        data = yaml.safe_load(path.read_text())
        if data.get("status") == "published":
            published_from_manifests.add(str(data["id"]))
    assert published_from_status == {"1.1", "1.2", "1.3"}
    assert published_from_status == published_from_manifests


def test_next_queue_points_to_the_first_remaining_module() -> None:
    status = yaml.safe_load((ROOT / "content/progress/STATUS.yaml").read_text())
    assert status["revision"]["remaining"]
    assert status["next"]["id"] == status["revision"]["remaining"][0] == "1.4"


def test_module_review_metadata_does_not_turn_pending_requests_into_completed_reviews() -> None:
    for path in (ROOT / "content/modules").glob("*/**/module.yaml"):
        data = yaml.safe_load(path.read_text())
        if data["status"] == "published":
            assert data["reviewStatus"] == "completed"
            assert data["reviewer"]
            assert data["lastReviewedAt"]
        else:
            assert data["reviewStatus"] in {"requested", "not-requested"}
            assert data["reviewer"] is None
            assert data["lastReviewedAt"] is None
            assert data["nextReviewAt"] is None


def test_module_1_3_is_in_the_lab_regression_matrix() -> None:
    labs = discover_labs()
    assert "1.3" in labs
    assert (labs["1.3"] / "tests").is_dir()


def test_generator_is_dry_run_by_default_and_protects_1_3() -> None:
    generator = ROOT / "scripts/emit_publishable_lessons.py"
    preview = subprocess.run(
        [sys.executable, str(generator), "--module", "1.4"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert preview.returncode == 0
    assert "No files changed" in preview.stdout

    protected = subprocess.run(
        [sys.executable, str(generator), "--module", "1.3"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert protected.returncode != 0
    assert "published module" in (protected.stdout + protected.stderr)


def test_lab_readmes_use_path_scoped_restore_guidance() -> None:
    for readme in (ROOT / "labs").rglob("README.md"):
        text = readme.read_text()
        assert "git checkout --" not in text
        assert "git reset --hard" not in text
