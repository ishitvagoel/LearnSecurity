"""Seeded review fixture -- NOT wired into pytest, NOT the shipped fix.

This is a snapshot of a hypothetical pull request against `fixed/app.py`,
written to be read and reviewed, per lessons/08-review.md. The author
describes it as: "Closed the missing-cross-tenant-read gap the auditor
flagged last sprint, and added the new client-portal request flow to the
required-flow list." It is deliberately NOT `fixed/app.py`: it seeds
several issues at differing severity, plus one detail a reviewer might
flag that is not actually a defect for this module's property. Do not
import or run this file; it exists for lessons/08-review.md's reading
exercise only.
"""
from __future__ import annotations

MANDATORY_IDS: tuple[str, ...] = ("cross-tenant-read", "hostile-browser", "stolen-worker")

REQUIRED_FLOWS: frozenset[str] = frozenset(
    {"browser-share-request", "member-note-read", "client-portal-request"}
)

_CURRENT_MODEL: dict = {}


def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    reasons: list[str] = []

    if scanner_green:
        return {"gate": "pass", "reasons": [], "scanner_extra_findings": list(scanner_findings)}

    if all(tid in str(model) for tid in MANDATORY_IDS):
        pass
    else:
        reasons.append("missing one or more mandatory threat ids")

    declared_flows = set(model.get("declared_flows", []))
    missing_flows = REQUIRED_FLOWS - declared_flows
    if missing_flows:
        reasons.append(f"declared flows do not trace: {sorted(missing_flows)}")

    return {
        "gate": "pass" if not reasons else "fail",
        "reasons": reasons,
        "scanner_extra_findings": list(scanner_findings),
    }
