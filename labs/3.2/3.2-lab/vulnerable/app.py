"""SecureCollab's Phase 3 CI threat-model gate (VULNERABLE), as a local fixture.

This is not a website to attack. `create_app()` builds a small FastAPI
service with two endpoints: one to store a versioned threat-model document
(the thing a team would actually keep in git) and one that plays the part
of a merge-time CI check -- the gate a pull request has to pass before the
model is trusted. See `../README.md` for the invariant and how to run both
variants, and `SECURITY.md` for what is wrong with this file specifically.

The defect: `evaluate_gate` reads exactly one field of the request --
`scanner_green` -- and, when it is `True`, returns `pass` without opening
the stored threat-model document at all. A SAST/DAST/package-scan result
becomes a stand-in for the model itself. Every other property a real gate
would have to check (are the three threats SecureCollab must always name
present; does the declared flow list actually cover the worker-redelivery
path; did anyone re-review a row after its named trigger fired; does the
top-priority threat have a real mitigation) goes unchecked whenever the
scanner happens to be green, which is most of the time a scanner is
running at all.
"""

from __future__ import annotations

from fastapi import FastAPI

# The three threats SecureCollab's Phase 3 threat model must always be able
# to name, independent of anything a scanner can see, because none of the
# three is a pattern a SAST/DAST/package rule matches: a member of another
# company reading a note by id, a browser client no server code should
# trust, and a worker that redelivers a share grant after the fact.
MANDATORY_IDS: tuple[str, ...] = ("cross-tenant-read", "hostile-browser", "stolen-worker")

# The three trust-boundary-crossing flows Phase 3's data-flow diagram must
# trace for the always-name threats above to mean anything: a public
# request path, a same-company read path, and the worker path a plain HTTP
# scan will never exercise.
REQUIRED_FLOWS: frozenset[str] = frozenset(
    {"browser-share-request", "member-note-read", "worker-share-redelivery"}
)

_MODEL: dict = {}


def reset() -> None:
    _MODEL.clear()


def evaluate_gate(model: dict, scanner_green: bool, scanner_findings: list[str]) -> dict:
    if scanner_green:
        return {"gate": "pass", "reasons": [], "scanner_extra_findings": list(scanner_findings)}
    threats = model.get("threats", [])
    if threats:
        return {"gate": "pass", "reasons": [], "scanner_extra_findings": list(scanner_findings)}
    return {
        "gate": "fail",
        "reasons": ["no threats recorded and scanner is not green"],
        "scanner_extra_findings": list(scanner_findings),
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
