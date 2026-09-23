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
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable   # 6 of 14 pass
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed        # 14 of 14 pass
```

If `fastapi`/`httpx` are not already installed: `pip install -r labs/2.2/2.2-request-path/requirements.txt`.

Fourteen tests across two files: `test_cache_key.py` (C1, C2 — normal case, both forbidden outcomes, a malformed-credential case, a boundary case, and one anti-fake test per claim using company and note-id values never written elsewhere in the file) and `test_tls_hop.py` (C3 — normal case, the hostname-mismatch forbidden outcome, a TLS-version boundary at 1.2, an unknown-trust-state failure case, an explicitly-untrusted-CA failure case distinct from the unknown-state case, and two hostname anti-fake tests: a prefix fake and a substring-anywhere fake).

Verified against five constructed fakes, each isolating exactly one gap: keying the cache correctly while leaving the `X-Company` override in place passes 12 of 14 and fails exactly the C2 forbidden-outcome test and its anti-fake pair; removing the header override while leaving the cache keyed on path alone passes 12 of 14 and fails exactly the C1 forbidden-outcome test and its anti-fake pair; `presented_hostname.startswith(expected_hostname)` in place of equality passes 13 of 14 and fails only its own anti-fake test; `expected_hostname in presented_hostname` passes 12 of 14 and fails both hostname anti-fake tests; and `if cert_trusted_ca is None: return False` in place of `if cert_trusted_ca is not True: return False` — a plausible reading of "fails closed on an unrecognized trust state" that only checks for the *unknown* case and lets an explicitly-resolved-untrusted certificate (`False`) fall through to the hostname/version checks — passes 13 of 14 and fails only `test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version`, the test added specifically because the original four fakes never isolated that one signal on its own.

## Operate

Signal a cache hit whose logged company does not match the bound company (`cdn_hit_company_mismatch`), and a rejected relay (`hop_rejected reason=hostname_mismatch|version|untrusted`), carrying path/hostname and company ids but never a note body. See [`lessons/06-operate.md`](../../../content/modules/2/2.2/lessons/06-operate.md).

## Transfer

A clinic portal caching `GET /patients/me` behind the same kind of edge. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/2/2.2/lessons/07-transfer.md).
