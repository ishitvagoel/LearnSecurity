"""Fixed: worker identity is a server-side bind, not a client header (split shared mechanism)."""

NOTES = [
    {"id": "n1", "tenant": "tA", "body": "tenant-A-note"},
    {"id": "n2", "tenant": "tB", "body": "tenant-B-note"},
]


def export_notes(headers: dict, *, worker_bound: bool = False) -> list[dict]:
    del headers  # untrusted side of the boundary; never a TCB input
    if worker_bound:
        return list(NOTES)
    return []
