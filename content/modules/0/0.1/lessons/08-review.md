# Would you merge this "basic scope checking" PR?

**Kind:** code-review
**Loop step:** 8 Review

## Four questions that work on any PR claiming a security check

Reviewing a security-relevant change by reading its description and skimming the diff for anything alarming is how a name that only *sounds* like a check gets merged, because a plausible description and an absence of obviously alarming lines are both compatible with code that does nothing at all. This lesson uses one fixed checklist instead, applied the same way regardless of how confident the PR description sounds:

1. **What would falsify the PR's claim?** State a concrete input and the output the claim implies, before looking at whether the code actually produces it.
2. **What does the code actually check, versus what the description implies?** Read the code as if the description did not exist, and only then compare.
3. **The disagreement, with a concrete input.** If steps 1 and 2 differ, name the exact call and its exact return value that proves it.
4. **The requested change and the test that proves it.** Say what has to change, and which specific test — by name, in this repository — should flip from failing to passing once it does.

## The review: "basic scope checking"

A PR lands in this course's own tooling repository, described as "adds basic scope checking so labs can't accidentally hit real hosts." The diff is `vulnerable/scope.py` as it exists today:

```python
def target_is_authorized(url: str) -> bool:
    """Vulnerable: any URL is treated as in-scope."""
    return True
```

Apply the checklist before reading any further. **What would falsify the claim?** If this is "basic scope checking," `target_is_authorized("https://example.com/")` should return `False` — a public host is exactly the case any scope check worth the name exists to catch. **What does the code actually check?** Nothing: there is no reference to `url` anywhere in the function body, no comparison, no parsing, no allow-list. **The disagreement, concretely:** calling `target_is_authorized("https://example.com/")` on this exact file returns `True`, directly contradicting the claim the PR description makes about its own purpose. **The requested change and its test:** replace the body with a hostname parse and an exact-membership check against a written local allow-list, denying on any parse failure; the test that should flip from failing to passing is `test_public_host_is_out_of_scope`, and once the fix also handles malformed input and lookalike hosts correctly, `test_malformed_and_non_string_url_fails_closed` and `test_lookalike_hosts_are_not_authorized` should flip too.

The counterexample worth sitting with is how unremarkable this diff looks in review tooling. It is three lines, it has a docstring, the function signature matches what every caller expects, and nothing in it triggers a static analyzer looking for obviously dangerous patterns — no `eval`, no string concatenation into a query, no obviously missing null check. A reviewer skimming for red flags, rather than asking "does this function's behavior match its name," will very plausibly approve this PR, because the defect here is not a dangerous-looking pattern; it is the complete absence of any relationship between the function's stated purpose and its actual logic, which a pattern-matching review style is specifically bad at catching.

## The transfer submission: "we now validate hostnames properly"

A second PR, from a different colleague, responds to a bug report about `evillab.securecollab.test` being wrongly authorized. Its description reads "fixed — we now validate hostnames properly instead of the old broken check." The diff:

```python
def target_is_authorized(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return any(host.endswith(allowed) for allowed in ALLOWED_HOSTS)
```

Run the same four questions yourself before checking the key. Pay particular attention to question two: "we now validate hostnames properly" is a description of *effort applied* — parsing the URL, extracting the hostname, comparing it to something — and effort applied is not the same claim as "the comparison is correct for every input that matters," which is the actual thing a merge decision depends on. A description that sounds like a fix, backed by code that genuinely does more work than the version it replaces, can still be wrong in a way that only shows up once you supply the one input the author did not happen to try.

Notice what makes this second PR harder to review than the first, even though both are wrong. The first PR's function ignores its argument entirely, which a reviewer can catch by tracing exactly one call by hand. The second PR's function reads its argument, calls a real standard-library parser, lowercases the result, and iterates over a real allow-list — every individual line is doing something a correct implementation would also do, and the only thing wrong is which string method connects them. A reviewer who checks "does this touch `urlparse`, does it reference `ALLOWED_HOSTS`, does it return a boolean derived from the hostname" will answer yes to all three and move on, because those are the surface features a correct fix and this fake share. The distinguishing fact is buried one level down, in the specific semantics of `str.endswith` versus set membership, which is exactly the kind of detail a description like "we now validate hostnames properly" invites a reviewer to take on faith rather than trace by hand.

The general version of this mistake, worth carrying past this specific function: a change that replaces an obviously-absent check with a plausible-looking one shifts the reviewer's attention from "is there a check" to "does the description match the vibe of the diff," and the second question is measurably easier to answer well without actually being the right question. Every PR in this course's later modules that claims to add validation, sanitization, authorization, or verification deserves the same four-question treatment this lesson applies to three lines of Python, because the size of the diff has no relationship to how easy the defect is to miss.

## Practice

Do not fetch, scan, or otherwise contact any host named in either diff above; both reviews are conducted entirely by reading code and predicting outputs.

Write your own answers to all four checklist questions for the second PR above, before reading `content/assessment/keys/0.1.md`. State explicitly which test in `labs/0.1/0.1-orientation/tests` would catch the gap you found, by name.

## Check yourself

- Why does "the PR has a docstring and a clean diff" provide no information about whether `target_is_authorized`'s behavior matches its name?
- For the second PR, can you state the one concrete hostname that exposes the gap, and why a reviewer who only re-ran the pre-existing three passing tests would have approved it anyway?
- What is the general version of the mistake both PRs make, stated as a rule that applies beyond this specific function?
