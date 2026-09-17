# Review a session-parsing change before it merges

**Kind:** code-review
**Loop step:** 5 Verify (seeded review)

## What you are reviewing

`labs/4.3/4.3-lab/vulnerable/token.py` is presented to you as a pull request: "Session parsing, with idle-timeout support." The PR description says the change adds `session_is_active` for idle timeout and keeps the existing query/cookie/header parsing from an earlier release, and asks for a quick approval since the underlying parsing logic is described as unchanged. Your job is to decide whether that description is a complete and accurate account of what the code in front of you actually does, using only the four questions below and the file itself — not by reading `fixed/token.py`, and not by reading this module's other lessons as though they were an answer key someone left open for you.

## The four questions

1. **What would falsify the PR's own claim?** The PR claims `session_from_request` handles query/cookie/header parsing and that this is "existing, unchanged" behavior. State the exact call and expected return value that would prove or disprove that this function currently treats a query-string token as invalid, rather than accepting the age of the code as a substitute for checking it. Run that call, or trace it by hand against the actual source in front of you, before moving to the next question — a prediction you never checked against the file is a guess, not a review finding.

2. **What does the new function actually check, versus what its name and the PR description imply?** `session_is_active` is described as adding "idle-timeout support." List every timestamp the function reads, every comparison it makes, and every return path, in the order the code actually executes them, not in the order the description mentions them. Then ask: does the function's actual behavior match "idle timeout" as a complete lifetime policy, or does the name promise something the code does not fully deliver? A function can be accurately named for exactly what it does and still be dangerously incomplete for what a session lifetime policy as a whole needs — deciding which of those two failures applies here, precisely, is the point of this question, and "the name sounds right" is not an answer to it.

3. **Is there a case where the described behavior and the actual behavior disagree?** Construct a specific session record — pick concrete `issued_at` and `last_seen_at` values and a `now` value, not "an old session" as a vague description that cannot be traced through code — and trace both `session_from_request` and `session_is_active` on it by hand, line by line. Does either function's actual output match what a reasonable reader of the PR description would expect from it? If you find a disagreement, write down the exact inputs that produce it; "this seems risky" is a feeling, not a finding, and a finding without the exact inputs that reproduce it cannot be verified by anyone else who reads your review afterward.

4. **What would you ask the author to change, and what test would prove the change is real?** For each finding from question 3, state the specific code change you would request and the specific test call — inputs and expected output — that would fail today, against the file exactly as it stands, and pass after that specific change and no other. A requested change with no accompanying test is a request the author can satisfy by making the code merely look fixed without actually being fixed, which is precisely the trap this module's own anti-fake tests exist to close for its lab, and precisely the trap a review that skips this question reopens for every other change it approves.

## What a rushed review accepts, and why each one fails question 3

Rejecting these requires actually running or tracing the code, not recognizing them as familiar phrases:

- "It's existing code, so it must already be correct" — treats prior existence as its own proof; question 1 asks you to falsify it, not to trust its age.
- "We use JWTs, so a query-string parameter is just a convenience" — restates [Lesson 01](01-property.md)'s refuted belief; format does not decide channel safety.
- "TLS covers the transport, so this is fine" — answers a question about the wire, not about access logs, `Referer`, history, or screenshots, none of which the wire protects.
- "The function name says idle timeout, so it must implement idle timeout correctly" — a name is a claim, not evidence; question 2 exists because a function can implement one clock correctly while a policy needs two.
- Closing a finding because "we'll move to a real session store later" without a test that currently fails — a promise about a future change is not evidence about the code in front of you right now.

## Practice

Write your answers to questions 1 through 4 before running any command. Then run:

```text
python3 -m pytest labs/4.3/4.3-lab/tests --impl vulnerable
```

Compare the actual failures to your question-3 predictions. A finding you predicted that the suite does not actually test is a gap in the lab, worth naming; a failure the suite reports that you did not predict is a gap in your review, worth naming for the opposite reason.

## Use it somewhere new

Apply the same four questions to a PR description for a clinic's magic-link redemption handler that claims "exchanges the one-time code for a session, following the standard pattern." [Lesson 07](07-transfer.md)'s five claims are exactly the list of things "the standard pattern" needs to actually mean before that sentence is evidence rather than a slogan.

## What this page is not doing

Do not dump live logs, replay a real session, or treat this exercise's findings as complete before you have written the exact inputs that reproduce each one. Assign an owner to any finding you cannot immediately fix, and do not close it on a promise alone. Answer keys are not on this site.
