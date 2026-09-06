"""Fixed assembler: mandatory design threats survive a green scan."""

from __future__ import annotations

MANDATORY: tuple[tuple[str, str, str], ...] = (
    ("cross-tenant-read", "authz", "new-share-path"),
    ("hostile-browser", "web", "new-client-surface"),
    ("stolen-worker", "platform", "queue-or-worker-identity"),
)


def assemble_threat_model(
    scanner_green: bool, scanner_findings: list[str] | None = None
) -> dict:
    threats: list[dict[str, str]] = []
    seen: set[str] = set()
    for threat_id, owner, trigger in MANDATORY:
        threats.append(
            {
                "id": threat_id,
                "owner": owner,
                "trigger": trigger,
                "source": "mandatory",
            }
        )
        seen.add(threat_id)
    for threat_id in scanner_findings or []:
        if threat_id in seen:
            continue
        threats.append(
            {
                "id": threat_id,
                "owner": "scanner",
                "trigger": "finding-closed",
                "source": "scanner",
            }
        )
        seen.add(threat_id)
    return {"threats": threats, "scanner_green": scanner_green}


def threats_from_scan(
    scanner_green: bool, scanner_findings: list[str] | None = None
) -> list[str]:
    model = assemble_threat_model(scanner_green, scanner_findings)
    return [row["id"] for row in model["threats"]]
