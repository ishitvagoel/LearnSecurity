"""Forbidden outcome: browser-supplied internal header dumps all tenants' notes."""


def test_untrusted_caller_gets_nothing(surface) -> None:
    assert surface.export_notes({}) == []


def test_client_internal_header_is_not_worker_identity(surface) -> None:
    leaked = surface.export_notes({"X-SecureCollab-Internal": "1"})
    assert leaked == [], "header is on the untrusted side of the API boundary"


def test_bound_worker_may_export(surface) -> None:
    got = surface.export_notes({}, worker_bound=True)
    assert len(got) == 2
