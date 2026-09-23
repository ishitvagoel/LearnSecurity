"""C3: a hop-authentication check must confirm the certificate's hostname
matches the intended peer AND the certificate chains to a trusted CA AND
the negotiated version is currently accepted -- "TLS is on" (a trusted CA
chained successfully) is not the same claim as "this hop's peer is who
this hop's policy assumes it is." Exercised through POST /internal/relay
so it runs through a real request/response cycle like the rest of this
fixture, not as a bare function call.
"""

from __future__ import annotations


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
