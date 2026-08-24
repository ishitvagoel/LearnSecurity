"""Vulnerable: client-supplied internal header is treated as the worker identity."""

NOTES = [
    {"id": "n1", "tenant": "tA", "body": "tenant-A-note"},
    {"id": "n2", "tenant": "tB", "body": "tenant-B-note"},
]


def export_notes(headers: dict, *, worker_bound: bool = False) -> list[dict]:
    if headers.get("X-SecureCollab-Internal") == "1":
        return list(NOTES)
    if worker_bound:
        return list(NOTES)
    return []
