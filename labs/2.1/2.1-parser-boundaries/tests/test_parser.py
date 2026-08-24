AMBIGUOUS = '{"tenant":"tA","body":"secret","tenant":"tB"}'
CLEAN = '{"tenant":"tA","body":"secret"}'


def test_unambiguous_json_is_accepted(parser) -> None:
    got = parser.ingest_note(CLEAN)
    assert got["accepted"] is True
    assert got["acl_tenant"] == got["stored_tenant"] == "tA"


def test_duplicate_tenant_keys_are_one_meaning(parser) -> None:
    got = parser.ingest_note(AMBIGUOUS)
    assert got["accepted"] is False or got["acl_tenant"] == got["stored_tenant"], (
        "parser differential: ACL tenant must match stored tenant"
    )
