"""Vulnerable assembler: a green scan is treated as an empty threat model."""

from __future__ import annotations


def assemble_threat_model(
    scanner_green: bool, scanner_findings: list[str] | None = None
) -> dict:
    if scanner_green:
        return {"threats": []}
    findings = list(scanner_findings or ["generic"])
    return {"threats": [{"id": item} for item in findings]}


def threats_from_scan(
    scanner_green: bool, scanner_findings: list[str] | None = None
) -> list[str]:
    model = assemble_threat_model(scanner_green, scanner_findings)
    return [row["id"] for row in model["threats"]]
