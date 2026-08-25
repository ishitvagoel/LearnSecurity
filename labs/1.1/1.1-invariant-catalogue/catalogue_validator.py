"""Semantic linting for the local Module 1.1 invariant-catalogue lab.

This validator evaluates whether a catalogue is shaped for review. It cannot prove
that an application satisfies the catalogue; Module 1.1 has no product runtime.
"""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

ALLOWED_HOSTS = {"localhost", "127.0.0.1", "lab.securecollab.test"}
ID_PATTERN = re.compile(r"^SC-[A-Z]{3,5}-[0-9]{2}$")
URL_PATTERN = re.compile(r"https?://[^\s,)>\]]+", re.IGNORECASE)
SECRET_PATTERNS = (
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
MECHANISM_ONLY_PHRASES = (
    "we are secure because",
    "secure because",
    "we use tls",
    "uses tls",
    "we use jwt",
    "uses jwt",
    "passwords are hashed so",
    "scanner is green",
    "fully secure",
)
REQUIRED_EVIDENCE_MODES = ("normal", "negative", "abuse", "failure")
REQUIRED_DETECTION_FIELDS = (
    "signal",
    "threshold",
    "eventFields",
    "prohibitedFields",
    "failureBehavior",
)


def _text(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(f"{_text(k)} {_text(v)}" for k, v in value.items())
    if isinstance(value, list):
        return " ".join(_text(item) for item in value)
    return str(value)


def find_live_target_urls(value: Any) -> list[str]:
    """Return HTTP(S) URLs whose hostname is outside the authorized local set."""

    unsafe: list[str] = []
    for raw in URL_PATTERN.findall(_text(value)):
        url = raw.rstrip(".;")
        host = (urlparse(url).hostname or "").lower()
        if host not in ALLOWED_HOSTS:
            unsafe.append(url)
    return unsafe


def find_secret_markers(value: Any) -> list[str]:
    blob = _text(value)
    return [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(blob)]


def is_mechanism_only(property_text: str) -> bool:
    normalized = " ".join(property_text.lower().split())
    return any(phrase in normalized for phrase in MECHANISM_ONLY_PHRASES)


def _require_text(
    mapping: dict[str, Any], key: str, location: str, errors: list[str]
) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{location}.{key}: required non-empty text")
        return ""
    return value.strip()


def _require_list(
    mapping: dict[str, Any],
    key: str,
    location: str,
    errors: list[str],
    minimum: int = 1,
) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list) or len(value) < minimum:
        errors.append(f"{location}.{key}: required list with at least {minimum} item(s)")
        return []
    if any(not _text(item).strip() for item in value):
        errors.append(f"{location}.{key}: blank list items are not allowed")
    return value


def validate_catalogue(data: Any) -> list[str]:
    """Return review-shape errors. An empty list means the fixture passes this lab."""

    errors: list[str] = []
    if not isinstance(data, dict):
        return ["catalogue: expected a mapping"]

    if data.get("system") != "SecureCollab":
        errors.append("catalogue.system: must identify the SecureCollab synthetic model")
    scope = _require_text(data, "authorizedScope", "catalogue", errors).lower()
    if scope and not any(word in scope for word in ("local", "course", "synthetic")):
        errors.append("catalogue.authorizedScope: must name local/course/synthetic scope")
    if data.get("syntheticDataOnly") is not True:
        errors.append("catalogue.syntheticDataOnly: must be true")

    claims = data.get("claims")
    if not isinstance(claims, list):
        errors.append("catalogue.claims: expected a list of invariant records")
        claims = []
    elif len(claims) < 5:
        errors.append("catalogue.claims: at least five invariant records are required")

    seen_ids: set[str] = set()
    for index, claim in enumerate(claims):
        location = f"claims[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{location}: expected a mapping")
            continue

        claim_id = _require_text(claim, "id", location, errors)
        if claim_id and not ID_PATTERN.fullmatch(claim_id):
            errors.append(f"{location}.id: expected SC-NAME-00 stable identifier")
        if claim_id in seen_ids:
            errors.append(f"{location}.id: duplicate identifier {claim_id}")
        seen_ids.add(claim_id)

        property_text = _require_text(claim, "property", location, errors)
        assets = _require_list(claim, "assets", location, errors)
        attackers = _require_list(claim, "attackers", location, errors)
        trust = _require_list(claim, "trust", location, errors)
        untrusted = _require_list(claim, "untrusted", location, errors)
        _require_text(claim, "timeHorizon", location, errors)
        _require_list(claim, "preconditions", location, errors)
        _require_list(claim, "mechanisms", location, errors)
        _require_list(claim, "mechanismLimits", location, errors)
        forbidden = _require_list(claim, "forbiddenOutcomes", location, errors)
        _require_list(claim, "recovery", location, errors, minimum=2)
        _require_text(claim, "residualRisk", location, errors)
        _require_list(claim, "nonGoals", location, errors)
        _require_list(claim, "reviewTriggers", location, errors)

        if property_text:
            if is_mechanism_only(property_text):
                errors.append(f"{location}.property: mechanism slogan is not an invariant")
            normalized = property_text.lower().replace("_", " ")
            if not any(word in normalized for word in ("must", "only", "never", "cannot", "remain")):
                errors.append(
                    f"{location}.property: use an observable constraint such as must/only/never/remain"
                )
            asset_terms = {
                token
                for asset in assets
                for token in re.findall(r"[a-z]{4,}", _text(asset).lower().replace("_", " "))
            }
            if asset_terms and not any(term in normalized for term in asset_terms):
                errors.append(f"{location}.property: must name at least one listed asset")

        if attackers and trust and set(map(_text, attackers)) == set(map(_text, trust)):
            errors.append(f"{location}: attacker and trusted-base lists cannot be identical")
        if not untrusted:
            errors.append(f"{location}.untrusted: explicitly identify an untrusted component")
        if forbidden and all("secure" in _text(item).lower() for item in forbidden):
            errors.append(f"{location}.forbiddenOutcomes: name an observable system outcome")

        evidence = claim.get("evidence")
        if not isinstance(evidence, dict):
            errors.append(f"{location}.evidence: expected normal/negative/abuse/failure mapping")
        else:
            for mode in REQUIRED_EVIDENCE_MODES:
                values = evidence.get(mode)
                if not isinstance(values, list) or not values:
                    errors.append(f"{location}.evidence.{mode}: at least one item is required")
                elif any(
                    phrase in _text(values).lower()
                    for phrase in ("scanner is green", "middleware exists", "configured correctly")
                ):
                    errors.append(
                        f"{location}.evidence.{mode}: control presence is not property evidence"
                    )

        detection = claim.get("detection")
        if not isinstance(detection, dict):
            errors.append(f"{location}.detection: expected a structured detection plan")
        else:
            for field in REQUIRED_DETECTION_FIELDS:
                if not detection.get(field):
                    errors.append(f"{location}.detection.{field}: required")
            prohibited = _text(detection.get("prohibitedFields", [])).lower()
            for sensitive in ("note body", "password", "token"):
                if sensitive not in prohibited:
                    errors.append(
                        f"{location}.detection.prohibitedFields: explicitly prohibit {sensitive}"
                    )

    unsafe_urls = find_live_target_urls(data)
    if unsafe_urls:
        errors.append("catalogue: live or third-party targets are forbidden: " + ", ".join(unsafe_urls))
    secret_markers = find_secret_markers(data)
    if secret_markers:
        errors.append("catalogue: credential/private-key marker detected")

    return errors
