"""Forbidden outcome: two readers of the same bytes disagree about the tenant.

C1 is the property under test. The first two tests are the normal case and
the module's stated forbidden outcome, on the fixture's own constants. The
third is a boundary the original two-value comparison could not see: three
occurrences whose first and last happen to coincide while a middle one
disagrees. The fourth is a malformed-input case. The last two are the
anti-fake pair: they construct their own ambiguous and unambiguous objects,
never seen in these module-level constants, so a fake "fixed" checker that
special-cases exactly `AMBIGUOUS` and `CLEAN` cannot pass by memorizing the
two strings this file happens to use elsewhere.
"""

CLEAN = '{"tenant":"tA","body":"secret"}'
AMBIGUOUS = '{"tenant":"tA","body":"secret","tenant":"tB"}'


def test_unambiguous_json_is_accepted(parser) -> None:
    got = parser.ingest_note(CLEAN)
    assert got["accepted"] is True
    assert got["acl_tenant"] == got["stored_tenant"] == "tA"


def test_duplicate_tenant_keys_are_one_meaning(parser) -> None:
    got = parser.ingest_note(AMBIGUOUS)
    assert got["accepted"] is False or got["acl_tenant"] == got["stored_tenant"], (
        "parser differential: ACL tenant must match stored tenant"
    )


def test_middle_duplicate_is_not_silently_dropped(parser) -> None:
    """Three occurrences, first and last both "tA", middle "tC". A reader
    that only compares the first value against the last sees "tA" == "tA"
    and calls it agreement -- but a third claim about the tenant existed
    and disagreed, and it must not vanish just because the endpoints
    happened to match."""
    middle_mismatch = '{"tenant":"tA","body":"x","tenant":"tC","tenant":"tA"}'
    got = parser.ingest_note(middle_mismatch)
    assert got["accepted"] is False, (
        "a value that disagreed and was silently overwritten is still a "
        "disagreement; comparing only the first and last occurrence is not "
        "the same as checking that every occurrence agrees"
    )


def test_missing_tenant_field_is_rejected(parser) -> None:
    """No tenant key at all. Absence of the field is not the same claim as
    presence-with-agreement, and must not be accepted by default."""
    no_tenant = '{"body":"secret"}'
    got = parser.ingest_note(no_tenant)
    assert got["accepted"] is False, (
        "an object with no tenant claim at all has no meaning to agree on, "
        "and must not be accepted as if an empty string were a company"
    )


def test_checker_rejects_a_different_ambiguous_object(parser) -> None:
    """Anti-fake test. A fake repair could special-case the exact AMBIGUOUS
    string this file defines while leaving the general check broken. This
    constructs a different ambiguous object -- different tenant ids, never
    written anywhere else in this file -- so memorizing one string cannot
    pass it. Asserted strictly as refusal, not the forbidden-outcome test's
    looser "or the tenants happen to match" form: with two genuinely
    distinct duplicate values, a reader that derives both acl_tenant and
    stored_tenant from the same single read will always report them equal
    regardless of the real disagreement, which is exactly the trivial fake
    this stricter assertion exists to catch."""
    different_ambiguous = '{"tenant":"zX","note":"hello","tenant":"zY"}'
    got = parser.ingest_note(different_ambiguous)
    assert got["accepted"] is False, (
        "the check must refuse a genuinely disagreeing object it has not seen "
        "before, not only the one string this test file happens to call AMBIGUOUS"
    )


def test_non_string_duplicate_is_not_invisible_to_the_checker(parser) -> None:
    """A regex that only matches quoted-string values (an earlier version of
    this fix used exactly this regex) cannot see a non-string occurrence of
    the tenant key at all -- {"tenant":1,"tenant":"tA"} has one occurrence a
    string-only pattern is blind to, so a checker built that way believes
    there is only one occurrence, sees no disagreement, and accepts an
    object that in fact made two different claims about the tenant. This is
    the exact shape of gap Lesson 03's own counterexample is about: a reader
    built to approximate the grammar, rather than to run it, will always
    have some input it cannot see correctly."""
    mixed_type_duplicate = '{"tenant":1,"tenant":"tA"}'
    got = parser.ingest_note(mixed_type_duplicate)
    assert got["accepted"] is False, (
        "two occurrences of the tenant key with different values -- even if "
        "one is not a string -- is still a disagreement, and a checker that "
        "cannot see a non-string occurrence at all is not checking every "
        "occurrence, whatever it claims to do"
    )


def test_malformed_json_fails_closed_not_with_an_unhandled_exception(parser) -> None:
    """Genuinely invalid JSON syntax is a different failure from a missing
    or disagreeing field -- json.loads itself cannot even build an object to
    inspect. This must be refused, the same as any other case where no
    single meaning was established, rather than raising an unhandled
    exception that a caller might not catch."""
    not_json_at_all = "this is not valid json { at all"
    got = parser.ingest_note(not_json_at_all)
    assert got["accepted"] is False, (
        "malformed JSON syntax must fail closed, not merely fail to raise "
        "an exception that happens to propagate as a test error"
    )


def test_checker_accepts_a_different_unambiguous_object(parser) -> None:
    """Anti-fake test, the other direction: a checker hardcoded to always
    refuse would make the fixed variant unusable but could still look
    correct against AMBIGUOUS alone. A checker that always denies is as
    fake as one that always allows."""
    different_clean = '{"tenant":"zQ","note":"hello"}'
    got = parser.ingest_note(different_clean)
    assert got["accepted"] is True
    assert got["acl_tenant"] == got["stored_tenant"] == "zQ"
