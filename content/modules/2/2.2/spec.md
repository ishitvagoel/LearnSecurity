# 2.2 — DNS, transport, HTTP, TLS, proxies, CDNs, and caches

## Identity

- **id:** 2.2
- **slug:** dns-transport-http-tls-proxies-cdns-caches
- **title:** DNS, transport, HTTP, TLS, proxies, CDNs, and caches
- **phase / track / difficulty:** 2 / core / foundation
- **estimatedMinutes:** 300
- **prerequisites:** 2.1 Pass A (parsers); 1.3 boundaries
- **routeTags:** complete, accelerated, web-api
- **releaseMilestone:** M0
- **masteryGate:** 2

## Objective hierarchy

1. Trace a request **end to end** (browser → DNS → TLS → edge/CDN → app → DB) and mark, at every hop, which identity, host, or header value was actually authenticated and which was merely carried.
2. State TLS 1.3 **deployment responsibilities** (certificate/hostname validation, accepted versions, forwarding of client identity) without treating "HTTPS on" as the property.
3. Transfer: add a CDN or reverse proxy and list which of this module's boundaries and cache-key assumptions change.

## Misconceptions

- TLS termination means the app can trust `X-Forwarded-*` and `Host`.
- CDN cache is a performance-only concern.
- RFC 9846 is a checkbox ("TLS 1.3 enabled").
- A certificate that chains to a trusted CA proves the hop reached the intended host, without checking the certificate's hostname.
- Once TLS has terminated at the edge, a client-supplied forwarded-identity header is safe for the origin to trust.

## Concept map

DNS/name → TCP/TLS (RFC 9846) → HTTP hops → cache key → origin app. Each hop may rewrite trust; a passing handshake at one hop says nothing about the hop after it.

## Teaching claims

The module previously taught **one narrow predicate** across all eight lessons: a shared cache must key on the bound company, not the path. That property still holds and is still worth teaching — it is `C1` below — but it is not the whole module its title promises. Two more properties from the same request path (forwarded-identity trust, hop authentication) had never been named as claims, never had a lab assertion, and were mentioned only as misconceptions to avoid. Naming them here makes the coverage contract checkable, following the pattern `4.3` and `2.1` used for the same repair.

1. **C1 — A shared cache entry may be returned only when the key includes the caller's bound company.** For `GET /notes/{note_id}` in SecureCollab's Phase 2 request path, a cache hit may answer a caller only when the cache key includes the company that caller's own server-resolved identity is already bound to — never the path alone, a client `Host`, or an `X-Forwarded-*` value. If the bound company is missing or cannot be resolved, the correct behavior is a cache miss, not a shared slot. Company B reading company A's cached note is a secrecy failure caused by the store, not by a missing login.
2. **C2 — The bound company itself must come only from the caller's own credential.** For the same request path, the company SecureCollab's origin uses to decide which notes a caller may read must come only from the origin's own resolution of that caller's API key or session — never from a client-supplied `X-Forwarded-*`, `X-Company`, `X-Tenant`, or `Host` header value. TLS terminating at the edge authenticates the browser-to-edge hop; it says nothing about who set a header on the request that follows. An origin that lets a forwarded header override the bound company is granting authorization to whatever the caller claims, whether or not the connection used TLS.
3. **C3 — A TLS handshake proves a certificate chained to a trusted CA, not that it is the certificate for the intended peer.** A hop-authentication check must require, together, that the certificate chains to a trusted CA, that its hostname is exactly the hostname this hop meant to reach, and that the negotiated protocol is a currently accepted version. A check that accepts any CA-trusted certificate without comparing hostnames, or that treats a missing or unrecognized trust state as trusted, has confused "a certificate validated" for "the peer I intended is on the other end of this hop."
4. **C4 — TLS proves one hop at a time; it does not chain.** The browser's TLS handshake with the edge says nothing about whether the edge's own connection to the origin, or the origin's connection to a further dependency, is itself authenticated. A request-path diagram that draws one lock icon on the browser-to-edge arrow and calls the whole path secure has not asked, for every later hop, the same question this module opens with: who authenticated this hop's peer, and to which hop does that proof actually apply?
5. **C5 — A code-level fix does not stay true on its own.** A CDN configuration change, a redeployed edge, or an operator error can reintroduce a path-only cache key or a trusted forwarded header without touching the origin's code at all, so C1 and C2's fixes must be paired with a detection signal that names the mismatch — never the cached body — and a purge path that removes the wrongly shared entry. A fix with no accompanying signal is only true until the next infrastructure change nobody notices.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_same_company_reads_its_own_note_after_caching` (normal case, including a `"source"` assertion isolating an actual cache hit from a coincidentally-correct origin-store fallback), `test_other_company_does_not_receive_cached_body` (forbidden outcome), `test_cross_company_lookup_is_scoped_even_before_any_cache_entry_exists` (boundary), two anti-fake tests: `test_anti_fake_cache_key_with_fresh_never_elsewhere_used_company_and_note` (the cache key includes company) and `test_anti_fake_cache_actually_serves_the_second_read` (the cache mechanism participates at all, not only the key it would use if it did) | items.md #1, #4, #6, #7, #8 |
| C2 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_forwarded_company_header_cannot_grant_a_different_companys_note` (forbidden outcome), `test_unregistered_api_key_with_a_company_header_is_denied` (malformed), two anti-fake tests: `test_anti_fake_forwarded_header_with_fresh_never_elsewhere_used_values` (the header is ignored) and `test_anti_fake_credential_shaped_like_a_valid_key_is_still_denied` (identity resolution authenticates against the origin's real credential table, not a credential's shape) | items.md #2, #4, #7 |
| C3 | 1 Property, 4 Build, 5 Verify, 6 Operate | `test_matching_hostname_trusted_ca_current_version_is_trustworthy`, `test_hostname_mismatch_with_trusted_ca_is_rejected` (forbidden outcome), `test_tls_1_2_boundary_is_still_accepted_1_1_is_not` (boundary), `test_unknown_trust_state_fails_closed` and `test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version` (malformed/anti-fake pair), ten anti-fake tests (hostname prefix, hostname substring-anywhere, hostname suffix-without-boundary, hostname Unicode-confusable, hostname zero-width-character, version-string-sorts-high, forward-compatible-allow-list, version-string-parses-in-range, version-string-incidental-whitespace, an eighteen-case version-string near-miss sweep including a Unicode-confusable case and a zero-width-character case) | items.md #3, #7, #8 |
| C4 | 1 Property, 2 Model, 7 Generalize | Not directly code-testable — no second real network hop exists in this fixture, and the lab's own non-goals rule out DNS or live-CDN work. Modeled in `lessons/01-property.md`'s trust-boundary diagram and `lessons/02-model.md`'s per-hop annotation table. | items.md #5, #7 |
| C5 | 6 Operate, 7 Generalize | Not directly code-testable — no CDN or edge process exists in this fixture to drift. Modeled in `lessons/06-operate.md`'s signal/purge design and the transfer task's residual-risk requirement. | items.md #6, #7, #8 |

C1, C2, and C3 each carry genuine lab assertions — three claims, exceeding the module's own ≥2 bar. C4 and C5 are honestly declared non-code-testable rather than mapped to a fabricated test: C4 needs a second real hop this single-process fixture cannot stage without violating the lab's own no-live-CDN, no-DNS non-goals, and C5 needs an actual CDN or edge process to drift, which this course's laboratory policy does not permit standing up.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Identify every point where a shared cache or a forwarded-identity header could substitute a wrong company for the caller's own bound identity | C1, C2 | [`lessons/01-property.md`](lessons/01-property.md) §Two decisions, one shared mistake | [`lessons/03-break.md`](lessons/03-break.md) broken `app.py` fixture | `labs/2.2/2.2-request-path` vulnerable/fixed pair | items.md #1, #2, #4 | [`lessons/07-transfer.md`](lessons/07-transfer.md) clinic cache and header |
| State precisely what a TLS 1.3 handshake does and does not prove about a hop's peer, and name the additional checks a deployment must add | C3, C4 | [`lessons/01-property.md`](lessons/01-property.md) §A validated certificate is not the intended peer | [`lessons/04-build.md`](lessons/04-build.md) `hop_is_trustworthy` repair | [`lessons/05-verify.md`](lessons/05-verify.md) hop-check tests | items.md #3 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Produce a request-path diagram naming, per hop, what was authenticated and the cache-key policy that must hold | C1, C2, C4 | [`lessons/02-model.md`](lessons/02-model.md) §Annotate every hop | [`lessons/02-model.md`](lessons/02-model.md) per-hop table | [`lessons/02-model.md`](lessons/02-model.md) diagram exercise | items.md #5 | [`lessons/07-transfer.md`](lessons/07-transfer.md) |
| Given a new CDN or reverse proxy, predict which assumptions change and design the detection/recovery response | C1, C2, C5 | [`lessons/06-operate.md`](lessons/06-operate.md) §A fix that only lives in one place | [`lessons/06-operate.md`](lessons/06-operate.md) signal table | [`lessons/07-transfer.md`](lessons/07-transfer.md) write-up | items.md #6, #7, #8 | [`lessons/07-transfer.md`](lessons/07-transfer.md) (is the transfer task) |

## Known residuals

- A real multi-hop chain (edge → origin → a further dependency) is C4's subject but is not staged in this fixture; it is named explicitly as a residual in `lessons/01-property.md` and `lessons/02-model.md`, and picked up when a module models a real second network hop.
- Web cache deception (unexpected content types, files that do not exist) is a distinct, harder failure from path-only tenant sharing; ASVS `v5.0.0-14.2.5` is cited at its correct Level 3 and named as a residual in `lessons/05-verify.md`, not folded into C1's Level 2 property.
- DNS answer authenticity (DNSSEC, a poisoned resolver) is out of this module's lab scope by the course's own laboratory policy; it is named as an open question in the invariant prompts and left for a later topic, not silently assumed solved.
- Mutual TLS, HTTP/2 and HTTP/3-specific behavior, and Encrypted Client Hello are named as later surfaces in `lessons/01-property.md`, not claimed as covered here.
- `hop_is_trustworthy`'s hostname and version-string comparisons are exact code-point equality, and the lab's anti-fake tests confirm this holds against two distinct classes of plausible-but-wrong alternate implementation: Unicode canonical-compatibility normalization (a fullwidth-digit version string, a fullwidth-letter hostname — both fold to the ASCII original under NFKC/NFKD) and zero-width/format-character stripping (a version string or hostname with an invisible U+200B spliced in, which neither NFKC/NFKD normalization nor a plain `.strip()` removes). What is NOT covered, and is an explicit, accepted non-goal rather than an open search: real internationalized domain names (IDNA/Punycode), homograph attacks using visually similar but code-point-distinct scripts in a genuinely registered hostname (already out of scope before this class of anti-fake test existed, since no standard-library normalization this module tests against actually folds one script onto another), any normalization a real certificate-validation library might legitimately perform before this predicate ever sees a hostname string, and any further not-yet-constructed Unicode-adjacent comparison technique beyond the two classes named above. This module's claim is narrower and code-level — the check itself must not normalize away a genuine mismatch under either of these two named classes — not a claim that every conceivable string-comparison technique has been tried, and not an invitation to keep adding one more Unicode category per review round indefinitely. A reviewer who wants to spend further adversarial effort on this module should prefer C1, C2, the CA-trust check, or documentation clarity over a further Unicode-normalization variant of `hop_is_trustworthy`'s hostname/version checks, absent a genuinely new angle distinct from both classes already covered.

## Invariant prompts

- Who authenticated the name, and to which hop?
- What is the cache key, and can an attacker influence it?
- After TLS is terminated, what identity is still bound to the request?
- Does a passing TLS handshake at one hop say anything about a hop after it?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 2.2-LO-01 | concept-model | A hop's certificate is not a company; a cache key is not a header | 1 Property |
| 2.2-LO-02 | design-exercise | Annotate every hop with what it authenticated, not what it encrypted | 2 Model |
| 2.2-LO-03 | mechanism-lab | Local fixture: a shared cache and a forwarded header both grant the wrong company | 3 Break |
| 2.2-LO-04 | design-exercise | Bind the cache key, ignore the header, check the whole certificate | 4 Build |
| 2.2-LO-05 | verification-lab | Fail-on-vulnerable then pass-on-fixed for cache keys, headers, and hop trust | 5 Verify |
| 2.2-LO-06 | operations-exercise | Detect a mismatched hit or a mismatched hop; purge and rotate without logging bodies | 6 Operate |
| 2.2-LO-07 | transfer-challenge | Transfer: clinic /patients/me on a shared CDN | 7 Generalize |
| 2.2-LO-08 | code-review | Seeded review of a cache, a header, and a hop check that all stop too early | 5 Verify |

## Lab briefs

**Lab `2.2-request-path`:** local FastAPI fixture only, Tier 2. Invariant: cache-key binding (C1), forwarded-identity trust (C2), hop authentication (C3). Forbidden: attacking real CDNs, third-party sites, or performing a real TLS handshake or DNS resolution.

## Assessment blueprint

Explain what a TLS handshake proves and does not; design a request-path diagram with cache keys and per-hop authentication notes; build an origin that resolves identity only from its own credential and a hop check that binds hostname, CA trust, and version together; break the local cache/header/hop fixture; verify the anti-fake pair for each claim; operate a cache-mismatch and hop-rejection signal plus a certificate-failure drill; communicate residual trust after TLS termination and after adding a CDN.

## Standards references

ASVS 5.0.0 `v5.0.0-4.1.3`, `v5.0.0-12.1.1`, `v5.0.0-12.2.1`, `v5.0.0-12.2.2`, `v5.0.0-12.3.2`, `v5.0.0-14.2.2`, `v5.0.0-14.3.2`, `v5.0.0-14.2.5` (Level 3), `v5.0.0-16.3.4`, all `final`, verified against the live v5.0.0 requirements JSON on 2026-09-22 — see `content/standards/pins.yaml`. IETF RFC 9110 HTTP Semantics (`final`). IETF RFC 9846 TLS 1.3 (`final`, obsoletes RFC 8446).

## Review triggers

New edge, CDN, HTTP/2-3, or mTLS. Change to forwarded-identity trust.

## Time budget

~300 min. Core of M0 observable skeleton.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-09-22 | Deepen pass: teaching claims C1–C5 replacing the single cache-key predicate; coverage contract added; see `module.yaml` changelog for the full defect-ID accounting |
