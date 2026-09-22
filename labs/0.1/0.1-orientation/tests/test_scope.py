"""Tests for target_is_authorized.

Claim map (see content/modules/0/0.1/spec.md "Teaching claims"):

  C1 -- an allow-listed local host is in scope; every other host is not,
        regardless of whether it answers to a connection.
  C3 -- a URL this function cannot parse, or that is not even a string,
        denies rather than raising or defaulting to allowed.
  C5 -- allow-list membership is exact-string; a host that merely starts
        with, ends with, or contains an allowed name is not that host.

Run:
    python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable
    python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed
"""


def test_localhost_lab_is_in_scope(scope) -> None:
    """Normal case (C1): the named loopback lab host may be true."""
    assert scope.target_is_authorized("http://127.0.0.1:8000/notes") is True


def test_named_lab_domain_is_in_scope(scope) -> None:
    """Normal case (C1), with a port and path never used by any other test
    in this file. A fake that hard-codes the exact URL strings the other
    tests use, instead of genuinely comparing the parsed host, has nothing
    memorized here to fall back on.
    """
    assert scope.target_is_authorized("https://lab.securecollab.test:4443/export") is True


def test_public_host_is_out_of_scope(scope) -> None:
    """Forbidden outcome (C1): course work is not authorization to attack
    the public internet."""
    assert scope.target_is_authorized("https://example.com/") is False, (
        "course work is not authorization to attack the public internet"
    )


def test_lookalike_hosts_are_not_authorized(scope) -> None:
    """Boundary case (C5): a host that contains, starts with, or ends with
    an allowed name is not that allowed name. Each of these would be
    wrongly authorized by a substring, prefix, or suffix comparison instead
    of exact-string set membership.
    """
    lookalikes = [
        "http://lab.securecollab.test.evil.com/",  # allowed name as a prefix of a longer host
        "https://evillab.securecollab.test/",       # allowed name as a suffix of a longer host
        "https://notlab.securecollab.test/",        # allowed name as a suffix, different lead-in
        "http://127.0.0.1.evil.com/",                # allowed IP literal as a prefix of a longer host
    ]
    for url in lookalikes:
        assert scope.target_is_authorized(url) is False, (
            f"{url!r} contains an allowed host as a substring; it is not that host"
        )


def test_malformed_and_non_string_url_fails_closed(scope) -> None:
    """Malformed/failure case (C3): a URL this function cannot parse denies
    rather than raising. An unmatched IPv6 bracket raises ValueError inside
    urlparse(); a non-string argument raises AttributeError or TypeError.
    Neither should propagate out of target_is_authorized, and neither
    should be treated as authorized because no verdict came back.
    """
    for bad_url in ["http://[::1/path", 12345, None, ""]:
        assert scope.target_is_authorized(bad_url) is False, (
            f"unparseable input {bad_url!r} must deny, not raise or default to allowed"
        )


def test_case_and_scheme_do_not_change_the_public_verdict(scope) -> None:
    """Boundary case (C1/C5): changing case or scheme on a public host must
    not flip the verdict. If the fix only matched the lowercase form used in
    the module's own examples, this catches it.
    """
    assert scope.target_is_authorized("HTTPS://EXAMPLE.COM/") is False
    assert scope.target_is_authorized("http://Example.Com:8080/path") is False


def test_anti_fake_generalizes_beyond_the_three_literal_example_urls(scope) -> None:
    """Anti-fake test. A plausible fake repair hard-codes the exact URL
    strings this file's other tests use (a lookup table of whole URLs)
    instead of parsing the hostname and comparing it to ALLOWED_HOSTS. That
    fake passes every test above, because every allowed URL above is one of
    a small memorized set. This test supplies allowed-host URLs with a
    port, path, and case combination that appears nowhere else in this
    file or in scope.py's own module docstring, so a hard-coded table has
    nothing to match, while a genuine host-comparison implementation
    passes without change.
    """
    never_elsewhere_used = [
        "http://127.0.0.1:51823/reports/quarterly",
        "http://LOCALHOST:9001/",
        "https://lab.securecollab.test/admin/export?id=7",
    ]
    for url in never_elsewhere_used:
        assert scope.target_is_authorized(url) is True, (
            f"{url!r} names an allowed host; a genuine host comparison must accept it "
            "even though this exact URL appears nowhere else"
        )
