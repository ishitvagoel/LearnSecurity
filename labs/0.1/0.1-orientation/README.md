# Lab 0.1 — reachability is not authorization

**Module:** `0.1`
**Authorized scope:** this directory only. Local course fixture. No public or third-party targets.
**Tier:** 1 (predicate). `target_is_authorized` is a single-value parser and comparison — it parses one URL's hostname and checks set membership, with no request cycle, no persisted state, and no caller whose correctness this claim depends on. That is the tier-1 exemption named in `lab-realism.mdc` and `upgrade-lab/references/lab-tiers.md` ("a single-value parser" is explicitly legitimate); it is not the same shape as a two-line stand-in for authorization *decisions in general*, which is what the rest of the course tests at Tier 2.

**Invariant (C1):** `target_is_authorized("https://example.com/")` is false. Only `127.0.0.1`, `localhost`, and `lab.securecollab.test` may be true.
**Invariant (C3):** a URL this function cannot parse — or that is not a string at all — denies. It never raises out of `target_is_authorized`, and a missing verdict is never treated as an allowed one.
**Invariant (C5):** membership is exact-string equality against the three names, never a prefix, suffix, or substring test.
**Root cause class (vulnerable):** authorization collapsed into reachability — every URL is treated as in-scope, so "the computer answered" and "a person wrote this host down" become the same fact.
**Non-goals:** live token replay, real DNS, a real HTTP client, following redirects, `/etc/hosts` aliasing.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/0.1/0.1-orientation`.

## Vulnerable behavior (local only)

`target_is_authorized` returns `True` unconditionally. The forbidden outcome is a non-allowlisted host — most concretely a public one — treated as authorized.

## Structural fix

`fixed/scope.py` parses the URL with `urllib.parse.urlparse`, lower-cases the extracted hostname, and checks it for exact membership in `ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}`. Two properties, not one, make this the structural fix rather than a patch:

1. There is no code path that returns `True` for a host outside that three-item set, under any input — not a denylist of one known-bad name checked and then fallen through.
2. A parse failure is caught and denies. `urlparse` can raise `ValueError` on a malformed authority (an unmatched IPv6 bracket) and can raise `AttributeError`/`TypeError` on non-string input; the fixed function catches exactly those and returns `False`, so "I don't know" and "no" are the same outcome for a caller, never "I don't know" and "yes."

## Verify

```bash
python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable   # 4 of 7 fail
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed        # 7 of 7 pass
```

From the repository root, the same two commands resolve to this directory.

Seven tests, covering three of this module's five teaching claims (C1, C3, C5 — see `content/modules/0/0.1/spec.md` §Teaching claims):

- `test_localhost_lab_is_in_scope`, `test_named_lab_domain_is_in_scope` — the normal case, both allowed hosts (C1).
- `test_public_host_is_out_of_scope` — the module's forbidden outcome (C1).
- `test_lookalike_hosts_are_not_authorized` — a boundary case: hosts that contain an allowed name as a prefix or suffix, but are not that host (C5).
- `test_malformed_and_non_string_url_fails_closed` — the malformed/failure case: an unmatched IPv6 bracket and non-string input must deny, not raise (C3).
- `test_case_and_scheme_do_not_change_the_public_verdict` — a second boundary case: changing case or scheme on a public host must not flip the verdict.
- `test_anti_fake_generalizes_beyond_the_three_literal_example_urls` — the anti-fake test.

**Anti-fake test, verified against two concrete fakes.** A "fixed" implementation that hard-codes the exact URL strings used elsewhere in this file (`url in {"http://127.0.0.1:8000/notes", "https://lab.securecollab.test:4443/export"}`) passes every other test — the memorized set happens to cover them — and fails only `test_anti_fake_generalizes_beyond_the_three_literal_example_urls`, because that test supplies allowed-host URLs with a port, case, and path that appear nowhere else in the file: 6 of 7, not 7 of 7. A different "fixed" implementation that compares with `host.endswith(allowed)` instead of exact set membership passes every other test and fails only `test_lookalike_hosts_are_not_authorized`, because `"evillab.securecollab.test".endswith("lab.securecollab.test")` is `True`: also 6 of 7. Each fake is caught by a different, specifically-aimed test, which is why this lab carries two boundary-shaped tests rather than folding both checks into one.

## Operate

Signal `out_of_scope` with `host` and `reason` only — never a response body, never a screenshot. See [`lessons/06-operate.md`](../../../content/modules/0/0.1/lessons/06-operate.md).

## Transfer

Contractor asked to "quickly test our customer's WordPress." Prompt only — do not hit that host. See [`lessons/07-transfer.md`](../../../content/modules/0/0.1/lessons/07-transfer.md).
