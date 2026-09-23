# Lab: 2.2-request-path

**Module:** `2.2`
**Authorized scope:** this directory only. Local FastAPI fixture; no live CDN, no DNS resolution, no real TLS handshake, no third-party target.
**Tier:** 2 (component). A real FastAPI request/response cycle through `fastapi.testclient.TestClient`, with server-side state (`_ORIGIN_STORE`, `_CACHE`) that persists across calls within one test and resets between tests. The TLS-hop check (`hop_is_trustworthy`, C3) is a pure predicate colocated in the same app and exercised through `POST /internal/relay` rather than a bare function call, because this fixture never performs an actual TLS handshake — see `lab-realism.mdc`; a real handshake is out of this module's local-fixture scope, so the check it would gate is tested as a request instead.

**Invariant (C1):** A shared cache entry may be returned only when the key includes the company the caller is bound to, not the path alone.
**Invariant (C2):** The company used for an authorization decision must come only from the caller's own credential, never from a client-supplied `X-Company` (or other forwarded-identity) header.
**Invariant (C3):** A hop-authentication check must require a trusted CA, an exact hostname match, and an accepted TLS version together; a missing or unrecognized input fails closed.
**Root cause class:** trust (C2: identity read from a client-controlled channel) and shared mechanism (C1: a cache with no company dimension in its key; C3: a check that stops at "some cert validated").
**Non-goals:** live CDNs, DNS hijacking, a real TLS handshake, poisoning a public cache.

## Reset

No persistent state between tests. `conftest.py` loads a fresh module and calls `reset()` before every test. Optional: `git checkout -- labs/2.2/2.2-request-path`.

## Vulnerable behavior (local only)

`_resolve_company` returns a client-supplied `X-Company` header when present, instead of only the company `API_KEYS[api_key]` names. `_CACHE` is a `dict[str, str]` keyed on `note_id` alone. `hop_is_trustworthy` returns `cert_trusted_ca is True` and nothing else — it never looks at `presented_hostname` or `tls_version`.

## Structural fix

`_resolve_company` never reads `x_company`. `_CACHE` becomes `dict[tuple[str, str], str]` keyed on `(note_id, company)`. `hop_is_trustworthy` requires `cert_trusted_ca is True` **and** `presented_hostname == expected_hostname` **and** `tls_version` in `{"1.2", "1.3"}`.

## Verify

```bash
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable   # 6 of 19 pass
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed        # 19 of 19 pass
```

If `fastapi`/`httpx` are not already installed: `pip install -r labs/2.2/2.2-request-path/requirements.txt`.

Nineteen tests across two files: `test_cache_key.py` (C1, C2 — normal case, both forbidden outcomes, a malformed-credential case, a boundary case, and one anti-fake test per claim using company and note-id values never written elsewhere in the file) and `test_tls_hop.py` (C3 — normal case, the hostname-mismatch forbidden outcome, a TLS-version boundary at 1.2, an unknown-trust-state failure case, an explicitly-untrusted-CA failure case distinct from the unknown-state case, three hostname anti-fake tests (a prefix fake, a substring-anywhere fake, and a suffix-without-boundary fake), and four version-string anti-fake tests (a sorts-lexicographically-high fake, a hand-written forward-compatible allow-list fake, a parses-to-a-float-in-range fake, and an incidental-whitespace fake)).

Verified against ten constructed fakes, each isolating exactly one gap, every count checked by reconstructing the exact fake and running the real suite rather than incrementing an old number: keying the cache correctly while leaving the `X-Company` override in place, matching `vulnerable/app.py`'s own check order (API key validity decided first, then the header) — passes 17 of 19 and fails exactly the C2 forbidden-outcome test and its anti-fake pair; the malformed-credential case (an unregistered key with a company header) still passes, because the key check runs and fails before the header is ever consulted. Removing the header override while leaving the cache keyed on path alone passes 17 of 19 and fails exactly the C1 forbidden-outcome test and its anti-fake pair. `presented_hostname.startswith(expected_hostname)` in place of equality passes 18 of 19 and fails only its own anti-fake test. `expected_hostname in presented_hostname` passes 16 of 19 and fails all three hostname anti-fake tests, not only the two it was originally built against — "origin.internal" is a substring of "evil-origin.internal" exactly as it is a substring of a prefix or middle-placed attacker string, so a check that only asks "does the expected name appear anywhere" cannot tell any of the three shapes apart. `presented_hostname.endswith(expected_hostname)` in place of equality — the same mistake from the third boundary position, catching a name glued onto the end with no separator — passes 18 of 19 and fails only its own anti-fake test. `if cert_trusted_ca is None: return False` in place of `if cert_trusted_ca is not True: return False` — a plausible reading of "fails closed on an unrecognized trust state" that only checks for the *unknown* case and lets an explicitly-resolved-untrusted certificate (`False`) fall through to the hostname/version checks — passes 18 of 19 and fails only `test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version`. `tls_version < "1.2"` in place of exact membership in `_ACCEPTED_TLS_VERSIONS` — a plausible reading of "1.2 and 1.3 are the accepted versions" as a lexicographic lower bound — passes 15 of 19 and fails all FOUR version anti-fake tests, not only the one it was originally built against: "1.9" sorts above "1.2" as text (the gap that first test was built for), but so does "1.4" (`"1.4" < "1.2"` is `False` in Python, since `"4" > "2"` character-by-character), so does "1.30" (the digit-by-digit comparison never reaches the third character), and so does "1.2\n" (a string that shares every character "1.2" has and then some is never lexicographically smaller than "1.2" itself), so this same fake also wrongly accepts the forward-compatible, parses-in-range, and incidental-whitespace tests' input, for three further, unrelated reasons. A hand-written `{"1.2", "1.3", "1.4"}` in place of `_ACCEPTED_TLS_VERSIONS` itself — a plausible "let's allow the next version too" guess that adds a version this fixture has never actually accepted — passes 18 of 19 and fails only `test_anti_fake_forward_compatible_allow_list_still_rejects_an_unaccepted_version`. Parsing `tls_version` as a float and checking `1.2 <= version_num <= 1.3` in place of exact string-set membership — a plausible reading of "1.2 through 1.3" as a numeric interval rather than two opaque strings — passes 17 of 19 and fails BOTH the parses-in-range anti-fake test it was originally built against and the incidental-whitespace anti-fake test, not only the first: `float("1.30") == 1.3` places "1.30" inside the numeric range even though it is not a member of `{"1.2", "1.3"}` as a string, and `float("1.2\n")` is also `1.2`, because Python's `float()` strips incidental whitespace before parsing — a second, independent reason for the identical numeric-range mistake to accept a string that should be rejected. And a version check that strips incidental whitespace before comparing — `tls_version.strip() not in _ACCEPTED_TLS_VERSIONS` in place of the bare membership test, a defensive habit many header-adjacent codebases apply reflexively — passes 18 of 19 and fails only `test_anti_fake_version_string_with_incidental_whitespace_is_rejected`, since `"1.2\n".strip() == "1.2"` is a member of the accepted set even though `"1.2\n"` itself is not.

## Operate

Signal a cache hit whose logged company does not match the bound company (`cdn_hit_company_mismatch`), and a rejected relay (`hop_rejected reason=hostname_mismatch|version|untrusted`), carrying path/hostname and company ids but never a note body. See [`lessons/06-operate.md`](../../../content/modules/2/2.2/lessons/06-operate.md).

## Transfer

A clinic portal caching `GET /patients/me` behind the same kind of edge. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/2/2.2/lessons/07-transfer.md).
