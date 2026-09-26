"""SecureCollab's Phase 3 CI threat-model gate (FIXED), as a local fixture.

Same two endpoints as `vulnerable/app.py`, but `evaluate_gate` now opens the
stored threat-model document on every call and checks five properties of
it directly, regardless of `scanner_green`. See `../README.md` for the
invariant and how to run both variants, and `SECURITY.md` for what this
file changes.

Five properties this file restores, each named in
`content/modules/3/3.2/spec.md`'s teaching claims:

1. **A green scanner does not replace the always-name set (C1).**
   `cross-tenant-read`, `hostile-browser`, and `stolen-worker` must be
   present with a named owner and review trigger, whatever `scanner_green`
   says. Scanner findings are additive -- returned as
   `scanner_extra_findings` -- never a substitute.

2. **An incomplete trust-boundary diagram lets an untraced path stand in
   for "checked" (C2).** `REQUIRED_FLOWS` names every flow the always-name
   threats depend on. A model whose `declared_flows` omits the
   worker-redelivery path fails even if every threat id nominally exists,
   because a threat row with no traced flow behind it is a label, not a
   checked boundary.

3. **A threat row is checkable only with an owner, a trigger, and a
   priority (C3).** Missing any of the three is a failure, not a
   completed row.

4. **Priority without a real mitigation is not prioritization (C5).** The
   mandatory threat with the lowest (most urgent) priority number must
   carry a mitigation string that is not a placeholder.

5. **A fired review trigger demands a recorded re-review, not a rewritten
   date (C4).** For every trigger name in `trigger_events`, every threat
   whose own `trigger` matches must list that name in `revisited_after`.
   This is deliberately independent of any timestamp field: a model can
   claim to be "recently updated" and still fail this check, because
   staleness here is measured by what was actually re-reviewed, not by
   what a submitter typed into a date field.

What this file does **not** claim to prove: that `revisited_after` records
an honest re-review rather than a rubber stamp is outside what an automated
gate can check from the outside; see `content/modules/3/3.2/lessons/05-verify.md`
for that limit stated as part of the property, not hidden here.
"""

from __future__ import annotations

from fastapi import FastAPI

MANDATORY_IDS: tuple[str, ...] = ("cross-tenant-read", "hostile-browser", "stolen-worker")

REQUIRED_FLOWS: frozenset[str] = frozenset(
    {"browser-share-request", "member-note-read", "worker-share-redelivery"}
)

_PLACEHOLDER_MITIGATIONS = {"", "tbd", "todo", "pending", "n/a", "later"}

_MODEL: dict = {}


def reset() -> None:
    _MODEL.clear()


def _threats_by_id(model: dict) -> dict[str, dict]:
    return {t.get("id"): t for t in model.get("threats", []) if t.get("id")}


def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    reasons: list[str] = []
    by_id = _threats_by_id(model)

    # (1) The always-name set, whatever the scanner says.
    missing_mandatory = [tid for tid in MANDATORY_IDS if tid not in by_id]
    if missing_mandatory:
        reasons.append(f"missing mandatory threat id(s): {sorted(missing_mandatory)}")

    for tid in MANDATORY_IDS:
        threat = by_id.get(tid)
        if threat is None:
            continue
        if not threat.get("owner"):
            reasons.append(f"threat '{tid}' has no owner")
        if not threat.get("trigger"):
            reasons.append(f"threat '{tid}' has no review trigger")

    # (2) Every required flow must actually be traced on the diagram.
    declared_flows = set(model.get("declared_flows", []))
    missing_flows = REQUIRED_FLOWS - declared_flows
    if missing_flows:
        reasons.append(f"declared flows do not trace: {sorted(missing_flows)}")

    # (3) / (4) Priority is required; the top-priority mandatory threat
    # needs a mitigation that is not a placeholder.
    mandatory_present = [by_id[tid] for tid in MANDATORY_IDS if tid in by_id]
    missing_priority = [t["id"] for t in mandatory_present if not isinstance(t.get("priority"), int)]
    if missing_priority:
        reasons.append(f"threat(s) missing an integer priority: {sorted(missing_priority)}")

    prioritized = [t for t in mandatory_present if isinstance(t.get("priority"), int)]
    if prioritized:
        top = min(prioritized, key=lambda t: t["priority"])
        mitigation = str(top.get("mitigation", "")).strip().lower()
        if mitigation in _PLACEHOLDER_MITIGATIONS:
            reasons.append(f"top-priority threat '{top['id']}' has no real mitigation")

    # (5) A fired trigger demands a recorded re-review of every threat it
    # names as its trigger -- not a rewritten "last updated" date.
    fired = list(model.get("trigger_events", []))
    for event_name in fired:
        for threat in model.get("threats", []):
            if threat.get("trigger") == event_name:
                revisited = threat.get("revisited_after", [])
                if event_name not in revisited:
                    reasons.append(
                        f"trigger '{event_name}' fired but threat "
                        f"'{threat.get('id')}' was not revisited"
                    )

    extra_findings = [f for f in scanner_findings if f not in by_id]

    return {
        "gate": "pass" if not reasons else "fail",
        "reasons": reasons,
        "scanner_extra_findings": extra_findings,
        "scanner_green": scanner_green,
    }


def create_app() -> FastAPI:
    app = FastAPI()

    @app.put("/threat-model")
    def put_threat_model(payload: dict) -> dict:
        _MODEL.clear()
        _MODEL.update(payload)
        return {"stored": True}

    @app.get("/threat-model")
    def get_threat_model() -> dict:
        return dict(_MODEL)

    @app.post("/ci/gate")
    def ci_gate(payload: dict) -> dict:
        scanner_green = bool(payload.get("scanner_green", False))
        scanner_findings = list(payload.get("scanner_findings", []))
        return evaluate_gate(_MODEL, scanner_green, scanner_findings)

    return app
