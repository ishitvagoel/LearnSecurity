"""C1: a shared cache entry must be keyed on the bound company, not the
path alone. C2: the bound company itself must come only from the
caller's own credential, never from a client-supplied X-Company (or any
other forwarded-identity) header. The two defects live in different
functions and are each independently exploitable, so most cases below
touch only one of them; the anti-fake pair uses company and note-id
values never written anywhere else in this file, so a fix that special-
cased the earlier literals cannot pass by memorizing them.
"""

from __future__ import annotations


def _auth(key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {key}"}


def test_same_company_reads_its_own_note_after_caching(client) -> None:
    """Normal case. Company A stores a note, reads it once (priming
    whatever cache the origin keeps), then reads it again. Both reads
    must return company A's own body."""
    client.put("/notes/n1", json={"body": "alice-n1"}, headers=_auth("key-A"))
    first = client.get("/notes/n1", headers=_auth("key-A"))
    second = client.get("/notes/n1", headers=_auth("key-A"))
    assert first.status_code == 200
    assert first.json()["body"] == "alice-n1"
    assert second.json()["body"] == "alice-n1"


def test_other_company_does_not_receive_cached_body(client) -> None:
    """C1 forbidden outcome. Company A's note is read once, priming the
    cache for that path. Company B then asks for the exact same path with
    its own valid credential and no forged header of any kind -- a cache
    keyed on path alone must still hand company B company A's body,
    because the key never recorded which company filled the slot."""
    client.put("/notes/n1", json={"body": "alice-n1"}, headers=_auth("key-A"))
    client.get("/notes/n1", headers=_auth("key-A"))  # primes the cache
    got = client.get("/notes/n1", headers=_auth("key-B"))
    assert got.status_code == 404, (
        "a cache entry filled by company A must never answer company B's "
        "own, differently authenticated request for the same path"
    )


def test_forwarded_company_header_cannot_grant_a_different_companys_note(client) -> None:
    """C2 forbidden outcome. Company B stores a note that has never been
    read -- no cache entry exists for it, so this exercises identity
    resolution alone, not caching. A caller who holds only company A's own
    API key then asks for it while sending a client-supplied X-Company
    header claiming to be company B. TLS terminating at the edge says
    nothing about who set this header; only the caller's own credential
    may decide which company they are."""
    client.put("/notes/n2", json={"body": "bob-n2"}, headers=_auth("key-B"))
    got = client.get("/notes/n2", headers={**_auth("key-A"), "X-Company": "companyB"})
    assert got.status_code == 404, (
        "a client-supplied X-Company header must never override the "
        "company bound to the caller's own API key"
    )


def test_unregistered_api_key_with_a_company_header_is_denied(client) -> None:
    """Malformed / failure case. A caller with no valid credential at all
    must be denied outright, even while sending an X-Company header naming
    a real company. An unknown caller is not evidence of any company,
    however confidently a header claims one."""
    got = client.get(
        "/notes/n1",
        headers={"Authorization": "Bearer key-does-not-exist", "X-Company": "companyA"},
    )
    assert got.status_code == 401


def test_cross_company_lookup_is_scoped_even_before_any_cache_entry_exists(client) -> None:
    """Boundary case. Company Z asks for a note company Q stored, using
    its own valid credential and no forged header, for a note that was
    never read before -- the cache is empty, so this exercises only the
    origin store's own per-company scoping. Both variants must deny this:
    the two structural bugs live in the cache key and in header handling,
    not in the origin store's baseline scoping, and a fixture that also
    failed this case would be broken in a way this module does not teach."""
    client.put("/notes/n3", json={"body": "quinn-n3"}, headers=_auth("key-Q"))
    got = client.get("/notes/n3", headers=_auth("key-Z"))
    assert got.status_code == 404


def test_anti_fake_cache_key_with_fresh_never_elsewhere_used_company_and_note(client) -> None:
    """Anti-fake, C1. A fake repair could special-case the exact note id
    or company strings the forbidden-outcome test above happens to use --
    for example an allow-list keyed on those literals -- while leaving the
    general cache lookup keyed on path alone. This uses company Z and Q
    and a note id never written anywhere else in this file."""
    client.put("/notes/n4", json={"body": "zed-n4"}, headers=_auth("key-Z"))
    client.get("/notes/n4", headers=_auth("key-Z"))  # primes the cache
    got = client.get("/notes/n4", headers=_auth("key-Q"))
    assert got.status_code == 404, (
        "the cache key must bind company for every note and company pair, "
        "not only the ones this file's other cases happen to use"
    )


def test_anti_fake_forwarded_header_with_fresh_never_elsewhere_used_values(client) -> None:
    """Anti-fake, C2. A fake repair could special-case the exact header
    value the forbidden-outcome test above sends -- for example refusing
    only that one literal string -- while leaving every other client-
    supplied company claim in effect. This uses a header value and note id
    never written anywhere else in this file."""
    client.put("/notes/n5", json={"body": "quinn-n5"}, headers=_auth("key-Q"))
    got = client.get("/notes/n5", headers={**_auth("key-Z"), "X-Company": "companyQ"})
    assert got.status_code == 404, (
        "every client-supplied company header must be ignored for "
        "authorization, not only the one value this file's other case "
        "happens to send"
    )
