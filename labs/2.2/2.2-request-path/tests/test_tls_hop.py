"""C3: a hop-authentication check must confirm the certificate's hostname
matches the intended peer AND the certificate chains to a trusted CA AND
the negotiated version is currently accepted -- "TLS is on" (a trusted CA
chained successfully) is not the same claim as "this hop's peer is who
this hop's policy assumes it is." Exercised through POST /internal/relay
so it runs through a real request/response cycle like the rest of this
fixture, not as a bare function call.
"""

from __future__ import annotations

import pytest


def _relay(client, expected: str, presented: str, trusted_ca, version: str):
    return client.post(
        "/internal/relay",
        json={
            "expected_hostname": expected,
            "presented_hostname": presented,
            "cert_trusted_ca": trusted_ca,
            "tls_version": version,
        },
    )


def test_matching_hostname_trusted_ca_current_version_is_trustworthy(client) -> None:
    """Normal case: everything the check asks for holds."""
    r = _relay(client, "notes-origin.securecollab.internal",
               "notes-origin.securecollab.internal", True, "1.3")
    assert r.status_code == 200


def test_hostname_mismatch_with_trusted_ca_is_rejected(client) -> None:
    """Forbidden outcome. A CA-trusted certificate for the WRONG name --
    for example a misrouted edge node presenting a different backend's own
    certificate -- must not be treated as this hop, even though the chain
    validates and the handshake succeeded. This is the exact "TLS is on"
    fallacy this module names as a misconception, made concrete: the
    connection is genuinely encrypted and genuinely chains to a CA
    everyone in this fixture trusts, and it is still the wrong peer."""
    r = _relay(client, "notes-origin.securecollab.internal",
               "billing-origin.securecollab.internal", True, "1.3")
    assert r.status_code == 502, (
        "a certificate that chains to a trusted CA for the WRONG hostname "
        "must still be rejected as this hop's peer"
    )


def test_tls_1_2_boundary_is_still_accepted_1_1_is_not(client) -> None:
    """Boundary case at the oldest currently accepted version. 1.2 must
    still pass (ASVS V12.1.1 names 1.2 and 1.3 as the latest recommended
    versions together); 1.1 must not."""
    ok = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.2")
    old = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.1")
    assert ok.status_code == 200
    assert old.status_code == 502


def test_unknown_trust_state_fails_closed(client) -> None:
    """Malformed / failure case. A trust state that is neither True nor
    False -- a certificate-chain check that could not complete, rather
    than one that completed and failed -- must not be read as trusted.
    Not knowing is not the same evidence as having verified."""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", None, "1.3")
    assert r.status_code == 502


def test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version(client) -> None:
    """Anti-fake, distinct from the unknown-trust-state case above. A
    plausible fake fix reads 'fails closed on an unrecognized trust
    state' as 'checks for None' and stops there -- for example
    `if cert_trusted_ca is None: return False` in place of
    `if cert_trusted_ca is not True: return False` -- which fails closed
    on the unknown case but wrongly falls through to the hostname/version
    checks for a trust state that was explicitly resolved to untrusted
    (False), rather than merely unresolved. Hostname and version are both
    otherwise valid here, isolating exactly this one signal: a completed
    chain-trust check that failed must be rejected on its own, not only
    when the check never completed at all."""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", False, "1.3")
    assert r.status_code == 502, (
        "an explicitly untrusted CA (cert_trusted_ca=False) must be "
        "rejected even when the hostname matches and the version is "
        "accepted -- 'not yet known to be trusted' and 'known to be "
        "untrusted' both fail closed, not only the former"
    )


def test_anti_fake_hostname_prefix_match_is_rejected(client) -> None:
    """Anti-fake. A plausible fake fix checks
    presented_hostname.startswith(expected_hostname) instead of exact
    equality, which would wrongly accept a hop presenting a certificate
    for an attacker-controlled name that merely begins with the real one."""
    r = _relay(
        client,
        "notes-origin.securecollab.internal",
        "notes-origin.securecollab.internal.attacker.example",
        True,
        "1.3",
    )
    assert r.status_code == 502, (
        "a presented hostname that only starts with the expected hostname "
        "is not the same hostname"
    )


def test_anti_fake_hostname_substring_anywhere_is_rejected(client) -> None:
    """Anti-fake, the other direction. A fake fix checks `expected_hostname
    in presented_hostname`, which the prefix case above would also pass,
    so this places the expected name in the MIDDLE of an attacker-chosen
    string -- never a prefix, never a suffix -- so a substring-anywhere
    fake still wrongly accepts it while exact equality correctly refuses."""
    r = _relay(client, "origin.internal", "evil-origin.internal-mirror.example", True, "1.3")
    assert r.status_code == 502, (
        "the expected hostname appearing anywhere inside the presented "
        "hostname is not the same claim as the two hostnames being equal"
    )


def test_anti_fake_version_string_that_sorts_high_is_still_rejected(client) -> None:
    """Anti-fake, for the version check specifically. A plausible fake fix
    reads 'only 1.2 and 1.3 are accepted' as a lexicographic lower bound
    (`tls_version < "1.2"` returns rejected) instead of exact set
    membership against `_ACCEPTED_TLS_VERSIONS`. Every other test in this
    file only ever sends a version that is either genuinely accepted
    ("1.2", "1.3") or genuinely older ("1.1"), and "1.1" also sorts below
    "1.2" as a string, so a lower-bound fake passes every one of them.
    "1.9" is not an accepted version, but the string "1.9" sorts ABOVE the
    string "1.2" (because "9" > "2"), so a lower-bound check wrongly
    treats it as new enough. Hostname and trust are both otherwise valid
    here, isolating exactly this one signal: exact membership in the
    accepted set, not "sorts high enough as text\""""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.9")
    assert r.status_code == 502, (
        "a version string that merely sorts lexicographically above the "
        "oldest accepted version is not the same claim as being a member "
        "of the accepted version set"
    )


def test_anti_fake_forward_compatible_allow_list_still_rejects_an_unaccepted_version(client) -> None:
    """Anti-fake, the same claim from the opposite direction. The
    lexicographic-lower-bound fake above reads "accept 1.2 and 1.3" as
    "accept anything not older than 1.2." A different plausible fake
    reads it as "accept 1.2, 1.3, and whatever comes next" and writes
    its own literal set, `{"1.2", "1.3", "1.4"}`, guessing ahead of what
    `_ACCEPTED_TLS_VERSIONS` actually contains. "1.4" is not an accepted
    version in this fixture -- no test elsewhere in this file sends it,
    so a hand-written set that happens to include it passes every other
    test here, including the lower-bound anti-fake above, which never
    sends anything above "1.9" either. Hostname and trust are both
    otherwise valid, isolating exactly this one signal: the accepted set
    is `_ACCEPTED_TLS_VERSIONS` itself, not any other set a fix's author
    might guess is equivalent to it."""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.4")
    assert r.status_code == 502, (
        "a version not present in _ACCEPTED_TLS_VERSIONS must be rejected "
        "even if it looks like a plausible next version to allow"
    )


def test_anti_fake_version_string_that_parses_in_range_is_still_rejected(client) -> None:
    """Anti-fake, a third and distinct shape for the version check. A
    plausible fake fix reads `_ACCEPTED_TLS_VERSIONS = {"1.2", "1.3"}` as
    "accept protocol versions from 1.2 through 1.3" and implements that as
    a NUMERIC range comparison -- parsing tls_version to a float and
    checking `1.2 <= version_num <= 1.3` -- instead of exact string-set
    membership. Every version string the two anti-fake tests above send
    ("1.9", "1.4") happens to parse to a float outside that numeric range
    too, so a numeric-range fake passes both of them for the wrong reason.
    "1.30" is not a member of _ACCEPTED_TLS_VERSIONS as a string, but
    float("1.30") == 1.3, so it falls INSIDE the numeric range a
    range-based fake accepts. Hostname and trust are both otherwise valid
    here, isolating exactly this one signal: the accepted set is the two
    strings "1.2" and "1.3" themselves, not any version string that
    happens to parse to a float between them."""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.30")
    assert r.status_code == 502, (
        "a version string that merely parses to a float numerically "
        "between the accepted versions is not the same claim as being "
        "one of the two accepted version strings itself"
    )


def test_anti_fake_version_string_with_incidental_whitespace_is_rejected(client) -> None:
    """Anti-fake, a fourth and distinct shape for the version check. A
    plausible fake fix defensively strips incidental whitespace before
    checking membership -- `tls_version.strip() not in
    _ACCEPTED_TLS_VERSIONS` in place of the bare membership test -- the
    kind of defensive habit many header-adjacent codebases apply reflexively
    to any string that arrived over the wire. Every version string every
    other test in this file sends ("1.1", "1.2", "1.3", "1.4", "1.9",
    "1.30") is already whitespace-free, so `.strip()` is a no-op on all of
    them and a strip-then-check fake passes every one. "1.2\\n" is NOT one
    of the two accepted strings -- `_ACCEPTED_TLS_VERSIONS` contains the
    canonical strings "1.2" and "1.3" only, with no whitespace variant --
    but its stripped form IS, so a fake that strips first wrongly accepts
    it. Hostname and trust are both otherwise valid here, isolating
    exactly this one signal: the accepted set contains two specific,
    already-canonical strings, not "any string that reduces to one of them
    after discarding whitespace\""""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, "1.2\n")
    assert r.status_code == 502, (
        "a version string that is not itself one of the two accepted "
        "strings is not made accepted by incidental leading or trailing "
        "whitespace -- the accepted set holds two canonical strings, not "
        "every string that trims down to one of them"
    )


def test_anti_fake_hostname_suffix_without_boundary_is_rejected(client) -> None:
    """Anti-fake, a third shape for the hostname check. The prefix fake
    above places the expected name at the START of an attacker string,
    and the substring-anywhere fake places it in the MIDDLE; this places
    it at the END, with no separator -- `presented_hostname.endswith(
    expected_hostname)` in place of exact equality. Neither of the other
    two hostname anti-fake tests catches this: the prefix fake's
    presented hostname does not end with the expected one, and the
    substring-anywhere fake's presented hostname is chosen so the
    expected name sits in the middle, not glued to the end. A presented
    name ending in the expected name with no `.` or other boundary
    character immediately before it is not a real subdomain relationship
    -- "evil-origin.internal" is not a subdomain of "origin.internal",
    it merely happens to share a trailing character run with it -- so
    accepting it on an endswith check is the same category of mistake
    the prefix and substring tests already name, one boundary
    position over."""
    r = _relay(client, "origin.internal", "evil-origin.internal", True, "1.3")
    assert r.status_code == 502, (
        "a presented hostname that merely ends with the expected hostname, "
        "with no boundary character separating them, is not the same "
        "hostname and is not a legitimate subdomain of it"
    )


# The four anti-fake tests above each isolate one specific, historically
# real alternate implementation of the version check (a lexicographic
# bound, a hand-written wider allow-list, a numeric-range parse, a
# whitespace strip) -- one per independent review round that found it.
# That pattern is itself evidence the check needed broader coverage than
# "one narrow test per gap someone happens to construct next": four
# structurally distinct near-misses in the same two-line check, each
# missed by every test that existed before it was found, means the next
# near-miss shape is more likely than not to exist too. Rather than wait
# for a fifth review round to find it by hand, this single parametrized
# test asserts rejection across a broad, systematically-chosen set of
# near-miss version strings in one pass -- covering whitespace in more
# positions than the one already-isolated case, leading/trailing zeros in
# either version position, an extra version segment, a sign prefix,
# exponential notation, a version-like substring embedded in a longer
# string, and a non-ASCII representation of a digit. It does not replace
# the four tests above, each of which documents a specific historical
# finding by name; it exists to catch the NEXT shape before another
# review round has to isolate it one at a time.
#
# "１.２" (rendered "1.2" but each character is a FULLWIDTH
# Unicode code point, U+FF11/U+FF0E/U+FF12, not ASCII) was added after a
# review round found that a Unicode-normalizing comparison --
# unicodedata.normalize("NFKC", tls_version) before checking membership,
# a defensive habit standard Unicode security guidance actively
# recommends for untrusted strings -- passed every ASCII-only case above,
# because NFKC normalization is a no-op on all of them. The accepted set
# is the two specific ASCII strings "1.2" and "1.3", not any string that
# normalizes to one of them under NFKC or any other Unicode equivalence.
_VERSION_NEAR_MISSES = [
    " 1.2",
    "1.2 ",
    "\t1.2",
    "1.3\t",
    "1.2\r\n",
    "01.2",
    "1.02",
    "1.20",
    "1.2.0",
    "+1.3",
    "1.2e0",
    "1.23",
    "1.234",
    "TLSv1.2",
    "v1.3",
    "1.2 or 1.3",
    "１.２",
]


@pytest.mark.parametrize("near_miss_version", _VERSION_NEAR_MISSES)
def test_anti_fake_version_near_miss_sweep_is_rejected(client, near_miss_version: str) -> None:
    """Anti-fake, a broad sweep rather than one more hand-picked shape.
    None of these strings is "1.2" or "1.3" -- each is a plausible way an
    alternate, incorrect implementation might still treat it as one of
    them: incidental whitespace in a position the dedicated whitespace
    test does not cover, a leading or trailing zero a numeric parse would
    normalize away, an extra version segment, a sign character a numeric
    parse would accept, exponential notation, an accepted-looking
    substring embedded in a longer string a regex or substring check
    might match, or a non-ASCII digit a Unicode-normalizing comparison
    would fold onto an accepted string. Hostname and trust are both
    otherwise valid here, isolating exactly this one signal, repeated
    across many inputs at once: the accepted set is exactly the two
    canonical ASCII strings "1.2" and "1.3", not any string a plausible
    normalization or partial match -- Unicode normalization included --
    would treat as equivalent to one of them."""
    r = _relay(client, "a.securecollab.internal", "a.securecollab.internal", True, near_miss_version)
    assert r.status_code == 502, (
        f"tls_version={near_miss_version!r} is not the string \"1.2\" or "
        f"\"1.3\" and must be rejected, regardless of how close a "
        f"plausible normalization or partial match would place it to one "
        f"of the two accepted strings"
    )


def test_anti_fake_hostname_unicode_confusable_is_rejected(client) -> None:
    """Anti-fake, a fourth shape for the hostname check and the same
    class as the version sweep's non-ASCII case above. A plausible fake
    fix Unicode-normalizes both hostnames before comparing --
    unicodedata.normalize("NFKC", presented_hostname) ==
    unicodedata.normalize("NFKC", expected_hostname) in place of the
    bare `==` -- a defensive habit standard Unicode security guidance
    actively recommends for untrusted strings in general, and therefore
    at least as plausible a good-faith choice as the whitespace-strip
    fake already closed for the version check. The presented hostname
    below is built entirely from FULLWIDTH Unicode code points (U+FF21
    etc.) standing in for the expected hostname's ASCII letters -- it
    renders visually as something close to the expected name but is not
    equal to it as a string, and NFKC-normalizes to a string that IS
    equal to it, which is exactly what a normalizing fake would fold
    over. None of this module's other hostname anti-fake tests (prefix,
    substring-anywhere, suffix-without-boundary) uses a non-ASCII
    character, so none of them catches this. Trust and version are both
    otherwise valid here, isolating exactly this one signal: the
    presented hostname must be the same sequence of code points as the
    expected one, not a sequence that some plausible Unicode
    normalization would fold onto it."""
    presented = "ａ.ｓｅｃｕｒｅｃｏｌｌａｂ.ｉｎｔｅｒｎａｌ"
    r = _relay(client, "a.securecollab.internal", presented, True, "1.3")
    assert r.status_code == 502, (
        "a presented hostname built from non-ASCII code points that "
        "Unicode-normalizes to the expected hostname is not the same "
        "sequence of code points as the expected hostname, and is not "
        "the same claim as the two hostnames being equal"
    )
