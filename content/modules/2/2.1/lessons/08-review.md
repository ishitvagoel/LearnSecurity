# Review of split JSON parsers

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Treat `labs/2.1/2.1-parser-boundaries/vulnerable/parse_note.py` as an ingest pull request someone on your team has just opened. Your job is to reconstruct, from the code alone, whether the who-is-allowed check and the storage step still end up parsing the same bytes twice with two different results — and to say so precisely, in terms of which two readers disagree and on what input, rather than in terms of a vulnerability class name.

Do not treat a green `test_duplicate_tenant_keys_are_one_meaning` as the whole review. A test passing tells you the object it was run against did not trigger that specific check; it does not tell you the underlying implementation generalizes to every object it will eventually see, which is exactly the gap the anti-fake tests exist to probe and a review has to probe by reading, not by re-running the same fixture.

## Picture: problems to find, but name them yourself first

```mermaid
flowchart TD
  Claim[A code comment or PR description's claim] --> Q{What would prove it false?}
  Q -->|An ingested object with two accepted meanings| Property[This is a rule -- good, if it is actually checked]
  Q -->|A library or scanner name| Mechanism[This is a tool name -- ask which rule it is supposed to enforce]
  Q -->|"JSON cannot have duplicate keys"| False[This is a false assurance -- the spec says "should," not "cannot"]
```

For every claim you find in the code, its comments, or an accompanying PR description, sort it into exactly one of these three bins before deciding whether it changes your review. A claim that lands in the third bin is not merely unhelpful — it is actively worse than no claim at all, because it tells the next reviewer the question is already settled.

Apply this checklist to the actual file yourself, in this order, before reading any further in this lesson or opening the examiner key:

1. Identify every function in `ingest_note`'s call graph that reads the raw `text` argument, or a value derived from it, in a way that could produce a company or tenant identifier. How many distinct readers did you find?
2. For each pair of readers you found, is there a line of code anywhere that compares their two outputs before either output is used? Quote the line, or state plainly that none exists.
3. Does any comment, docstring, or the module's own module-level documentation string assert that duplicate keys "can't happen" or "won't happen" for this data? If so, is that assertion actually enforced anywhere, or merely stated?
4. Is there a test, a fixture corpus, or any other executable evidence backing the claim that this file's behavior has been checked against a deliberately messy object — as opposed to only against a clean, well-formed one?

Write your answer to each question, with a specific line reference, before deciding whether the file passes review. A reviewer who cannot answer question 2 with either a quoted line or a plain "none exists" has not yet actually reviewed the file, regardless of how much time they spent looking at it.

Also reject on sight, regardless of how the rest of a change reads: treating agreement between exactly one pair of readers as proof that every reader in the system agrees; concatenating two readers' outputs as though that were the same as checking they match; "Report-Only" mode on any policy offered as if it were enforcement; closing a review finding without re-running the repaired-files check to confirm the fix actually holds; and any examiner key or answer text appearing in a learner's own review notes, which does not belong there under any circumstance.

## Worked example: reading the vulnerable file the way this review expects

Read `vulnerable/parse_note.py`'s `ingest_note` function line by line, before forming a conclusion:

```python
def ingest_note(text: str) -> dict:
    acl = _first_tenant(text)
    stored = _last_tenant(text)
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": json.loads(text).get("body")}
```

It calls `_first_tenant(text)`, assigns the result to `acl`. It calls `_last_tenant(text)`, assigns the result to `stored`. It then returns a dictionary with `accepted: True` — hardcoded, not computed from anything — plus both `acl` and `stored` values, whichever they happen to be. Trace what a reviewer who stops at "it calls two functions and returns their results" would miss: the function computes both values and then discards the comparison between them entirely, because no comparison was ever written anywhere in this four-line body. A skim that confirms "there are two readers here, as the module's naming suggests there should be" would approve this file, because the two readers genuinely are both present and both correctly implemented on their own terms — `_first_tenant` really does find the first occurrence, and `_last_tenant` really does return CPython's own last-key-wins value. The defect is not in either reader; it is in the sentence that never got written: something equivalent to `if acl != stored: refuse`. A reviewer who checks "are both readers present and individually correct" without asking "is their agreement ever verified" will sign off on exactly this diff.

## Common mix-ups this module refuses

- Treating encoding as a cryptography problem, when encoding and cryptography solve entirely different problems for entirely different threats.
- Assuming one JSON reader's correct behavior is evidence that a second, independently implemented reader behaves the same way on the same input.
- Treating validation and canonicalization as interchangeable steps that can be reordered or merged without consequence.

## Use it somewhere new

GraphQL and REST both ingest data about the same clinic appointment. A GraphQL request's `variables` field is itself a JSON object, sent over the same wire as a REST body — not a second grammar, but the same one this review has been about. Validating JSON correctly on only the REST path still leaves a two-meaning ingest if the `variables` JSON was never checked the same way; write the specific check that would catch a duplicate key in that payload, in the same shape as this module's `test_duplicate_tenant_keys_are_one_meaning`.

## What this page is not doing

Do not approve a merge on the reasoning that RFC 8259 says JSON object names *should* be unique. "Should," in an RFC's own terminology, is a recommendation a compliant implementation may still violate — it is not the same claim as `test_duplicate_tenant_keys_are_one_meaning` passing, and citing the specification is not a substitute for running the check.
