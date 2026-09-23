# A broken cache, header, or hop check must fail the check that names it

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** ASVS 5.0.0 v5.0.0-4.1.3, v5.0.0-12.1.1, v5.0.0-12.2.1, v5.0.0-12.3.2, v5.0.0-14.2.2, v5.0.0-14.2.5

## What "verified" has to mean here

A status code of 200 on a TLS connection proves the response arrived over an encrypted channel; it proves nothing about whether that response contained the right body. Verification for this module means: on `vulnerable/app.py`, each of `03-break.md`'s two traces produces its forbidden outcome and the matching test observes it; on `fixed/app.py`, every test in `labs/2.2/2.2-request-path/tests` passes, including a pair of anti-fake tests per claim that a narrow, half-correct repair cannot satisfy by accident.

## Mapping tests to claims, not to files

| Claim | Normal case | Forbidden outcome | Boundary | Malformed / failure | Anti-fake |
|---|---|---|---|---|---|
| C1 (cache key) | `test_same_company_reads_its_own_note_after_caching` | `test_other_company_does_not_receive_cached_body` | `test_cross_company_lookup_is_scoped_even_before_any_cache_entry_exists` | shares C2's malformed case | `test_anti_fake_cache_key_with_fresh_never_elsewhere_used_company_and_note` |
| C2 (forwarded identity) | (shares C1's normal case; same resolution path) | `test_forwarded_company_header_cannot_grant_a_different_companys_note` | (shares C1's boundary case) | `test_unregistered_api_key_with_a_company_header_is_denied` | `test_anti_fake_forwarded_header_with_fresh_never_elsewhere_used_values` |
| C3 (hop authentication) | `test_matching_hostname_trusted_ca_current_version_is_trustworthy` | `test_hostname_mismatch_with_trusted_ca_is_rejected` | `test_tls_1_2_boundary_is_still_accepted_1_1_is_not` | `test_unknown_trust_state_fails_closed` | `test_anti_fake_hostname_prefix_match_is_rejected`, `test_anti_fake_hostname_substring_anywhere_is_rejected`, `test_explicitly_untrusted_ca_is_rejected_even_with_matching_hostname_and_version` |

Several cells share a case rather than each claim owning five distinct tests, and that sharing is itself a finding worth stating explicitly: C1 and C2 both resolve through the same normal-case request, because a caller reading its own note correctly is evidence that *both* the credential lookup and the cache lookup behaved, not evidence that either one specifically did. A single passing normal case is weak evidence for two claims at once; the forbidden-outcome and anti-fake rows are where each claim earns its own, non-shared proof.

## Picture: evidence flowing from a run to a claim

```mermaid
flowchart LR
  Run["pytest --impl vulnerable"] -->|"6 of 14 pass"| V1["C1 forbidden outcome: FAIL\n(cache leak reproduced)"]
  Run -->|auth: test observed the response body directly| V2["C2 forbidden outcome: FAIL\n(header override reproduced)"]
  Run -->|auth: version/hostname never checked| V3["C3 forbidden outcome + boundary: FAIL"]
  Fixed["pytest --impl fixed"] -->|"14 of 14 pass"| F1["C1, C2, C3 all hold,\nincluding every anti-fake test"]
  V1 --> Claim1["Evidence for C1 as a real, reproducible defect"]
  V2 --> Claim2["Evidence for C2"]
  V3 --> Claim3["Evidence for C3"]
  F1 --> ClaimAll["Evidence the repair is structural,\nnot a memorized special case"]
```

Each arrow's annotation names what the test actually inspected — a returned body, a status code, a rejected relay — not merely "ran successfully." A run that reports "6 passed" for `vulnerable` without checking *which* six would miss that the six passing tests are exactly the ones this module predicts should pass on the broken code (the shared normal case and the cases that do not depend on any of the three bugs), while the eight that should fail do fail for the stated reason.

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

`labs/2.2/2.2-request-path/README.md` documents five constructed fakes verified against this suite before this module trusted it: a cache-only fix that leaves the header override open (caught by C2's forbidden-outcome test and its anti-fake pair, both fail; 12 of 14 still pass); a header-only fix that leaves the cache keyed on path alone (caught symmetrically by C1's pair); a hostname check using `.startswith()` (caught by exactly one anti-fake test, the prefix one); a hostname check using `in` (caught by both hostname anti-fake tests, since a substring match is a superset of a prefix match); and a trust-state check that reads "fails closed on an unrecognized state" as "checks only for `None`" — `if cert_trusted_ca is None: return False` in place of `if cert_trusted_ca is not True: return False` — which still fails closed on the unknown case but wrongly treats an explicitly-resolved `False` (a chain check that completed and failed) the same as `True` once hostname and version pass; 13 of 14 still pass, and only the test built specifically to isolate that one signal catches it. Each of these five fakes would look complete to a reviewer who only read the diff and not the tests — every one changes real code in the right direction, and every one still leaves a specific, describable input that reaches the forbidden outcome. The fifth fake is also the reason this page does not claim "unknown trust state fails closed" and "untrusted CA fails closed" are the same test: a check that never completed and a check that completed and failed are different facts about the world, and a suite that only exercises the first has not verified the second.

## What these checks do not prove

- A real TLS handshake, a real certificate authority, or a real DNS answer — `hop_is_trustworthy` is exercised through `POST /internal/relay` with values the test constructs directly, never a negotiated connection.
- Web cache deception (ASVS `v5.0.0-14.2.5`, Level 3 advanced): this fixture's failure is two authenticated companies sharing a slot, not an unauthenticated request tricking a cache into storing dynamic content under a static-looking path. Treating this module's Level 2 cache-key property as if it already covered Level 3 web cache deception would overstate what fourteen passing tests actually checked.
- Behavior of a real CDN, load balancer, or reverse proxy product — every claim here is verified against a local, single-process fixture.

Record these as residuals, the way `spec.md`'s "Known residuals" section already does, rather than as silent passes a reviewer might mistake for coverage. A residual named in prose and a gap covered by a passing test read identically in a status report that only counts green checkmarks; the difference only shows up to a reviewer willing to open `spec.md` and ask, for each named residual, whether any test in this suite could possibly have exercised it at all.

## Practice

Run both variants and, for the eight tests that fail on `vulnerable`, name which row of the table above each one evidences:

```bash
python3 -m pytest labs/2.2/2.2-request-path/tests --impl vulnerable
python3 -m pytest labs/2.2/2.2-request-path/tests --impl fixed
```

## Use it somewhere new

For an authenticated CSV export, write the five-case table above from scratch — normal, forbidden outcome, boundary, malformed, anti-fake — before writing a single line of test code, and predict which cases the export's own normal case would share with its company-resolution claim, the way this module's C1 and C2 share one.

## What this page is not doing

This page does not add new traffic beyond the local suite above, does not log a note body under any circumstance, and does not claim coverage of web cache deception or a real TLS deployment. Answer keys are not on this site.
