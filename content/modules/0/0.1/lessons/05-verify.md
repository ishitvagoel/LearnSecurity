# Verify the fail-safe check, not just its scoreboard

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** NIST CSF 2.0 (final) GV/ID as outcome vocabulary, not evidence of a passing test. OWASP WSTG 4.2 (final) names candidate test *methods*; this lesson owns the forbidden-outcome *shape* those methods still have to satisfy. NIST SP 800-181r1 NICE (final) role language does not change what a test asserts.

## Two failing counts, and only one of them matters

`labs/0.1/0.1-orientation` carries seven tests, and running them against `vulnerable/scope.py` should show four failing and three passing — but the number three is not evidence of anything, and treating it as partial credit is the specific mistake this lesson exists to head off. The three tests that pass against the vulnerable file are the two normal-case checks for `127.0.0.1` and `lab.securecollab.test`, plus the anti-fake test, and all three pass for the same uninteresting reason: the vulnerable function returns `True` unconditionally, and each of those three tests happens to assert that the result should be `True`. A function that always says yes will agree with every test that expects yes and disagree with every test that expects no; the passing count tells you nothing about whether the function reasons about its input, only that some of this file's tests happen to want the answer this particular broken function always gives. The four *failing* tests are where the real information is: `test_public_host_is_out_of_scope`, `test_lookalike_hosts_are_not_authorized`, `test_malformed_and_non_string_url_fails_closed`, and `test_case_and_scheme_do_not_change_the_public_verdict` each expect `False`, and each one is where this module's actual claims live.

```
python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable -v
```

Running that command should print four `FAILED` lines matching the four tests named above, and three `PASSED` lines for the rest. If your own run shows a different split — say, all seven passing, or a different four failing — the fixture itself is miswired for your environment, and the correct response is to find and fix that wiring, never to edit an assertion until the numbers you expected appear. An assertion that was loosened to make a broken implementation pass is not evidence the implementation works; it is evidence the test suite no longer checks the thing it was named for.

## What passing did not prove

```
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed -v
```

All seven tests should pass against `fixed/scope.py`, and the honest question to ask immediately afterward is what, specifically, that scoreboard does and does not establish. It establishes that this exact function, called with these exact inputs, returns the values these tests expect — nothing about redirects, `/etc/hosts` aliasing, DNS behavior, or any host this file's authors did not think to write a test for. It does not establish that following a redirect from an allowed host to an unallowed one is safe (it is not, and this fixture takes no position on it, because it never follows a redirect); it does not establish that the written scope artifact this course expects a human to produce actually exists for any given learner's situation; and passing does not establish that a testing-guide chapter, once read, grants anything, because no test here has any way to represent "a chapter was read" as an input in the first place. A green run of this suite is evidence about this predicate, on these inputs, and claiming it as evidence about anything broader — "the first check-in is done," "scope is handled," "we're covered" — is exactly the kind of scoreboard-reading this lesson is verifying you can resist.

## Reading a failed anti-fake test as if it were real

The most important failure mode to rehearse here is not the vulnerable file's failure — that one is obvious once you have read three lines of `return True` — it is the failure of a *plausible-looking fix* that nonetheless does not deserve to pass. Two such fixes are worth running by hand against this suite, because each one gets caught by a different, specifically-aimed test rather than by the suite as a whole, and seeing which specific test catches which specific mistake is what makes "verify" mean something more than "run pytest and check the exit code." A fix that hard-codes the exact URL strings the earlier tests use — `url in {"http://127.0.0.1:8000/notes", "https://lab.securecollab.test:4443/export"}` — passes the two normal-case tests, the forbidden-outcome test, the lookalike test, and the malformed-input test: six of seven. It fails only `test_anti_fake_generalizes_beyond_the_three_literal_example_urls`, because that test deliberately supplies allowed-host URLs with a port and path that appear nowhere else in the file, and a lookup table built from memorized strings has nothing to match against something it has never seen. A different fix that compares with `host.endswith(allowed)` instead of exact-set membership also passes six of seven — the same six — and fails only `test_lookalike_hosts_are_not_authorized`, because `"evillab.securecollab.test"` genuinely ends with `"lab.securecollab.test"` and the `endswith` version cannot tell the difference. Neither fake produces an all-seven-pass run, but neither one is caught by a *generic* sense that "something feels off" either — each is caught by exactly one test built for exactly that shape of shortcut, which is the entire argument for writing an anti-fake test instead of trusting that a broad-enough test suite will accidentally stumble into catching a cheat it was not designed for.

## Practice

Run this only inside `labs/0.1/0.1-orientation/`. Do not add a live network call to any of these tests, and do not fetch `example.com` to "confirm" a denial the test string already proves.

Implement the `endswith` fake described above directly in a scratch copy of `fixed/scope.py`, run `python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed -v` against your scratch copy (point `conftest.py`'s `--impl` at a temporary directory if needed, or simply overwrite and revert), and confirm by reading the actual output — not by predicting it — which single test fails. Then run `git checkout -- labs/0.1/0.1-orientation/fixed/scope.py` to restore the real fix before continuing.

## Check yourself

- Why is "three tests passed against the vulnerable file" not partial evidence that the vulnerable file is partially correct?
- Name the exactly one test each of the two fakes described above fails, and explain in one sentence why that specific test is the one built to catch that specific shortcut.
- What would you have to add to this test file to make it also verify the redirect-following behavior this lesson explicitly says it does not cover?
