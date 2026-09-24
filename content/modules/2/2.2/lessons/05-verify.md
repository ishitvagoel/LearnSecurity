# A broken cache, header, or hop check must fail the check that names it

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** ASVS 5.0.0 v5.0.0-4.1.3, v5.0.0-12.1.1, v5.0.0-12.2.1, v5.0.0-12.3.2, v5.0.0-14.2.2, v5.0.0-14.2.5

## What "verified" has to mean here

A status code of 200 on a TLS connection proves the response arrived over an encrypted channel; it proves nothing about whether that response contained the right body. Verification for this module means: on `vulnerable/app.py`, each of `03-break.md`'s two traces produces its forbidden outcome and the matching test observes it; on `fixed/app.py`, every test in `labs/2.2/2.2-request-path/tests` passes, including one or more anti-fake tests per claim that a narrow, half-correct repair cannot satisfy by accident.

## Mapping tests to claims, not to files

| Claim | Normal case | Forbidden outcome | Boundary | Malformed / failure | Anti-fake |
|---|---|---|---|---|---|
| C1 (cache key) | `test_same_company_reads_its_own_note_after_caching` (also asserts the `"source"` field) | `test_other_company_does_not_receive_cached_body` | `test_cross_company_lookup_is_scoped_even_before_any_cache_entry_exists` | shares C2's malformed case | `test_anti_fake_cache_key_with_fresh_never_elsewhere_used_company_and_note`, `test_anti_fake_cache_actually_serves_the_second_read` |
| C2 (forwarded identity) | (shares C1's normal case; same resolution path) | `test_forwarded_company_header_cannot_grant_a_different_companys_note` | (shares C1's boundary case) | `test_unregistered_api_key_with_a_company_header_is_denied` | `test_anti_fake_forwarded_header_with_fresh_never_elsewhere_used_values`, `test_anti_fake_credential_shaped_like_a_valid_key_is_still_denied` |
| C3 (hop authentication) | `test_matching_hostname_trusted_ca_current_version_is_trustworthy` | `test_hostname_mismatch_with_trusted_ca_is_rejected` | `test_tls_1_2_boundary_is_still_accepted_1_1_is_not` | `test_unknown_trust_state_fails_closed` | `test_anti_fake_hostname_prefix_match_is_rejected`, `test_anti_fake_hostname_substring_anywhere_is_rejected`, `test_anti_fake_hostname_suffix_without_boundary_is_rejected`, `test_anti_fake_hostname_unicode_confusable_is_rejected`, `test_anti_fake_hostname_zero_width_character_is_rejected`, `test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version`, `test_anti_fake_version_string_that_sorts_high_is_still_rejected`, `test_anti_fake_forward_compatible_allow_list_still_rejects_an_unaccepted_version`, `test_anti_fake_version_string_that_parses_in_range_is_still_rejected`, `test_anti_fake_version_string_with_incidental_whitespace_is_rejected`, `test_anti_fake_version_near_miss_sweep_is_rejected` (19 parametrized cases) |

Several cells share a case rather than each claim owning five distinct tests, and that sharing is itself a finding worth stating explicitly: C1 and C2 both resolve through the same normal-case request, because a caller reading its own note correctly is evidence that *both* the credential lookup and the cache lookup behaved, not evidence that either one specifically did. A single passing normal case is weak evidence for two claims at once; the forbidden-outcome and anti-fake rows are where each claim earns its own, non-shared proof.

## Picture: evidence flowing from a run to a claim

```mermaid
flowchart LR
  Run["pytest --impl vulnerable"] -->|"8 of 41 pass"| V1["C1 forbidden outcome: FAIL\n(cache leak reproduced)"]
  Run -->|auth: test observed the response body directly| V2["C2 forbidden outcome: FAIL\n(header override reproduced)"]
  Run -->|auth: version/hostname never checked| V3["C3 forbidden outcome + boundary: FAIL"]
  Fixed["pytest --impl fixed"] -->|"41 of 41 pass"| F1["C1, C2, C3 all hold,\nincluding every anti-fake test"]
  V1 --> Claim1["Evidence for C1 as a real, reproducible defect"]
  V2 --> Claim2["Evidence for C2"]
  V3 --> Claim3["Evidence for C3"]
  F1 --> ClaimAll["Evidence the repair is structural,\nnot a memorized special case"]
```

Each arrow's annotation names what the test actually inspected — a returned body, a status code, a rejected relay — not merely "ran successfully." A run that reports "8 passed" for `vulnerable` without checking *which* eight would miss that the eight passing tests are exactly the ones this module predicts should pass on the broken code: the shared normal case, the cases that do not depend on any of the three bugs, the cache-actually-fires anti-fake test (whose property `vulnerable/app.py`'s own cache mechanism happens to satisfy even though its *key* is wrong), and the credential-shape anti-fake test (`vulnerable/app.py`'s identity resolution is a real `API_KEYS` lookup, unmodified by its own header-override bug) — while the thirty-three that should fail do fail for the stated reason.

## Worked example: reading a failure for the reason it names

A test failing is not, by itself, evidence of the claim it was written for — it could be failing because of a typo in the test, a missing import, or an unrelated exception. The assertion message exists so a reviewer can check the *reason*, not just the outcome:

```text
$ python3 -m pytest labs/2.2/2.2-request-path/tests/test_cache_key.py::test_other_company_does_not_receive_cached_body --impl vulnerable
FAILED ... AssertionError: a cache entry filled by company A must never
answer company B's own, differently authenticated request for the same
path
assert 404 == <Response [200 OK]>.status_code
```

The `assert 404 == 200` line, on its own, is compatible with dozens of unrelated bugs — a missing route, a wrong status code convention, an unhandled exception FastAPI happened to translate into a 200. The assertion message, and the test's own docstring, are what tie this specific failure back to the specific claim: company B received a 200 with a body, when the property demands a 404, because the cache handed back company A's cached entry. A reviewer who reads only "8 failed" without reading which eight, and why, has not verified anything — they have counted.

## What would falsify a claim of "fixed"

If any test above passed on `vulnerable/app.py`, that test would not be asserting its claim — a passing vulnerable run means the suite stopped observing the forbidden outcome, not that the outcome stopped occurring. If any test failed on `fixed/app.py`, the repair in `04-build.md` would not be structural, and the failing test names exactly which of the three functions still has a gap. `spec.md`'s coverage-contract table records both directions so a reviewer can check this claim against the actual pytest output rather than against this page's prose describing it.

## Anti-fake tests are not decoration

Fifteen constructed fakes have been verified against this suite before this module trusted it — each one isolating exactly one gap a plausible, good-faith reimplementation could get wrong while still looking correct on a diff, and each one changing real code in the right direction while still leaving a specific, describable input that reaches a forbidden outcome. Three representative shapes, out of the fifteen, make the general pattern concrete:

- **An approximate string match.** `presented_hostname.startswith(expected_hostname)` in place of exact equality agrees with the real check on every hostname that is either genuinely equal or genuinely unrelated — it diverges only on a hostname that merely *starts with* the expected one, which is exactly the input a dedicated anti-fake test constructs to isolate this one signal.
- **A mechanism that never fires, satisfied by a hidden safety net elsewhere.** Removing the one line that ever populates `_CACHE` leaves every request falling through to `_ORIGIN_STORE`, which is already correctly scoped by `(note_id, company)` on its own — so a cache-disabling fix passes every C1/C2 test that checks only the response body, because the origin store's own scoping happens to cover every case those tests try. Only a test asserting the response's own `"source"` field, not just its body, can tell "the cache served this" from "the cache never fires and something else happened to be correct anyway."
- **An identity check that verifies shape instead of provenance.** A `_resolve_company` that pattern-matches a credential string's length and prefix, deriving a company from the credential itself instead of looking it up in `API_KEYS`, agrees with every registered credential this suite happens to send — and accepts a credential the origin never issued at all, as long as it happens to have the right shape. Only a test sending a credential shaped like a real one but never registered isolates this.

The same lesson repeats across the remaining twelve: a hostname or version-string comparison that stops one signal short of exact equality (a substring check, a numeric parse, a Unicode normalization, an invisible-character strip) can satisfy an entire suite built only from ASCII, canonical-form inputs, until a test is written that tries the specific near-miss shape the check quietly allows. A fake's failure count against the *current* suite, not the suite that existed when it was first isolated, is the only count worth trusting — several fakes above were re-derived more than once as later, unrelated additions to the suite happened to interact with them in ways nobody had checked for in advance.

The complete forensic account of all fifteen fakes — exact pass/fail counts, which review round found which, and precisely which test isolates which mechanism — is examiner-only material kept in `content/assessment/keys/2.2.md`, not duplicated here. What a learner needs is the three shapes above and the general claim they support, not a round-by-round audit trail.

## What these checks do not prove

- A real TLS handshake, a real certificate authority, or a real DNS answer — `hop_is_trustworthy` is exercised through `POST /internal/relay` with values the test constructs directly, never a negotiated connection.
- Web cache deception (ASVS `v5.0.0-14.2.5`, Level 3 advanced): this fixture's failure is two authenticated companies sharing a slot, not an unauthenticated request tricking a cache into storing dynamic content under a static-looking path. Treating this module's Level 2 cache-key property as if it already covered Level 3 web cache deception would overstate what fourteen passing tests actually checked.
- Behavior of a real CDN, load balancer, or reverse proxy product — every claim here is verified against a local, single-process fixture.

Record these as residuals, the way `spec.md`'s "Known residuals" section already does, rather than as silent passes a reviewer might mistake for coverage. A residual named in prose and a gap covered by a passing test read identically in a status report that only counts green checkmarks; the difference only shows up to a reviewer willing to open `spec.md` and ask, for each named residual, whether any test in this suite could possibly have exercised it at all.

## Practice

Run both variants and, for the thirty-three tests that fail on `vulnerable`, name which row of the table above each one evidences (the nineteen parametrized near-miss-sweep cases all evidence the same row — treat them as one piece of evidence repeated nineteen ways, not nineteen independent findings):

```bash
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed
```

## Use it somewhere new

For an authenticated CSV export, write the five-case table above from scratch — normal, forbidden outcome, boundary, malformed, anti-fake — before writing a single line of test code, and predict which cases the export's own normal case would share with its company-resolution claim, the way this module's C1 and C2 share one.

## What this page is not doing

This page does not add new traffic beyond the local suite above, does not log a note body under any circumstance, and does not claim coverage of web cache deception or a real TLS deployment. Answer keys are not on this site.
