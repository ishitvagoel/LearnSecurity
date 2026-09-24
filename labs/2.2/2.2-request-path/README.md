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
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable   # 8 of 41 pass
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed        # 41 of 41 pass
```

If `fastapi`/`httpx` are not already installed: `pip install -r labs/2.2/2.2-request-path/requirements.txt`.

Forty-one tests across two files: `test_cache_key.py` (C1, C2 — normal case, both forbidden outcomes, a malformed-credential case, a boundary case, and anti-fake tests isolating the cache key, the header-override defense, whether the cache mechanism itself ever fires (checked via the response's own `"source"` field, not only its body), and whether identity resolution authenticates against a real, issued credential rather than a string merely shaped like one) and `test_tls_hop.py` (C3 — normal case, the hostname-mismatch forbidden outcome, a TLS-version boundary at 1.2, two distinct failure cases for an untrusted certificate, five hostname anti-fake tests, four dedicated version-string anti-fake tests, and one eighteen-case parametrized sweep covering ASCII and Unicode-adjacent version-string near-misses in one pass).

**Anti-fake tests are not decoration.** Fifteen constructed fakes were verified against this suite before this module trusted it, each isolating exactly one gap a plausible, good-faith reimplementation could get wrong while still looking correct on a diff — every one changes real code in the right direction, and every one still leaves a specific, describable input that reaches a forbidden outcome. Two representative examples: `presented_hostname.startswith(expected_hostname)` in place of exact equality passes every case that doesn't specifically probe for a hostname sharing only a prefix with the real one, closed by a dedicated anti-fake test built for exactly that shape. And removing the one line that ever populates `_CACHE` leaves every request falling through to the already-correctly-scoped `_ORIGIN_STORE` — passing every C1/C2 test that checks only a response body, because the origin store's own scoping happens to cover every case those tests try; this one needed a test asserting the response's own `"source"` field before it could be caught at all. The general pattern repeats across all fifteen: a check that stops one signal short of the real one (an approximate string match, a normalization step, a mechanism that silently never fires, an identity check that verifies shape instead of provenance) can satisfy an entire suite built only from outcome assertions, until a test is written that asks not just "was the answer right" but "did it get there the way this module teaches."

The complete forensic account of all fifteen fakes — exact pass/fail counts, which review round found which, and precisely which test isolates which mechanism — is examiner-only material kept in `content/assessment/keys/2.2.md`, not duplicated here. A learner needs the pattern above, not a round-by-round audit trail.

## Operate

Signal a cache hit whose logged company does not match the bound company (`cdn_hit_company_mismatch`), and a rejected relay (`hop_rejected reason=hostname_mismatch|version|untrusted`), carrying path/hostname and company ids but never a note body. See [`lessons/06-operate.md`](../../../content/modules/2/2.2/lessons/06-operate.md).

## Transfer

A clinic portal caching `GET /patients/me` behind the same kind of edge. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/2/2.2/lessons/07-transfer.md).
