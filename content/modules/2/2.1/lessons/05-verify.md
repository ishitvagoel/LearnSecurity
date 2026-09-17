# The broken files must fail for the right reason

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** OWASP ASVS 5.0.0 **V1.5.3** (Level 3 — different parsers for the same data type must parse consistently, which is exactly what these nine tests check between the vulnerable file's two readers, and what the fixed file's single-reader design makes true by construction), **V1.1.1** (canonicalization happens once, before validation, not after). IETF RFC 8259 §4 (uniqueness of object member names is a "should," not an enforced guarantee every reader honors).

## Check it

HTTP 200 on a clean object does not finish this module's check, and neither does confirming that `ingest_note` returns a dictionary with the expected keys. Last-key-wins, and the quieter endpoints-only comparison Lesson 03 constructs a counterexample against, both have to fail on the broken files and pass on the repaired ones — and the check has to fail for the security reason the module names, not for an incidental one like a malformed input crashing the parser before the real comparison ever runs.

## Picture: broken files must fail, for the right reason

Asserting only that `ingest_note` runs without raising an exception is a much weaker claim than asserting it returns a result this specific rule accepts, and the gap between those two claims is exactly where a fake fix hides.

```mermaid
flowchart TD
  V[vulnerable/parse_note.py] --> T1[ingest_note on its own fixture objects]
  F[fixed/parse_note.py] --> T1
  T1 -->|vulnerable| Fail1[Must report a disagreement, or accepted=False]
  T1 -->|fixed| Pass1[Must correctly agree, or correctly refuse]
  Bad[Hand-built ambiguous object, never seen in this file's constants] --> T2[ingest_note, called directly]
  Good[Hand-built unambiguous object, never seen in this file's constants] --> T2
  T2 --> Fail2[Bad input: must refuse on both variants' own logic]
  T2 --> Pass2[Good input: must accept on the fixed variant]
```

The right side of the diagram is the anti-fake pair, and it exists for the same reason Lesson 03's counterexample exists: if a "fixed" implementation special-cased the exact `AMBIGUOUS` and `CLEAN` strings this test file happens to define, the left side alone would pass without the underlying rule actually being implemented. Constructing fresh input the checker has never seen closes that hole.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | A clean, unique-key object is accepted, with the ACL and stored tenants matching |
| Boundary — two occurrences | A two-key disagreement is refused, or the two readers happen to agree |
| Boundary — three occurrences | A middle value that disagrees while the first and last coincide is still refused — checking only the endpoints is not the same claim as checking every occurrence |
| Malformed field | An object with no tenant field at all is refused, not silently treated as an empty or default company |
| Malformed value / syntax | A non-string tenant value is not invisible to the checker, and syntactically invalid JSON fails closed rather than raising an unhandled exception |
| Nesting | A tenant key inside a different, unrelated field is not mistaken for the note's own top-level claim |
| Abuse / different objects | A checker built against this test file's own two constants must still correctly judge objects it has never seen |
| When things break | Uncertainty about which value is correct never results in a body being persisted |

Nine tests live in `labs/2.1/2.1-parser-boundaries/tests/test_parser.py`: the normal case, the module's stated forbidden outcome, the middle-duplicate boundary, the missing-field case, a non-string-value case, a malformed-JSON-syntax case, a nested-tenant case, and the two-test anti-fake pair. None of them opens a network socket, reads a file, or depends on which machine runs them — every one is a direct call to `ingest_note` with a hand-written string.

## Worked example: tracing why the middle-duplicate test needed to exist

Run `python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl vulnerable -v` and read the failure for `test_middle_duplicate_is_not_silently_dropped` rather than skipping to the summary line. The input is `{"tenant":"tA","body":"x","tenant":"tC","tenant":"tA"}`. Trace it through the vulnerable reader by hand: the regex scan for `_first_tenant` finds the first match in the raw text and stops, returning `"tA"`. CPython's `json.loads` for `_last_tenant` builds the full dictionary, and because Python dicts keep the last assignment to a repeated key, the resulting `tenant` value is also `"tA"` — the middle `"tC"` was overwritten by the third and final occurrence in the source text before `json.loads` ever returned. Both readers report `"tA"`. They agree. `ingest_note` returns `accepted: True`. Nothing about this is a bug in either reader; both did exactly what their documentation says they do, and the disagreement still happened — it happened in a place neither reader was even asked to look.

Now trace the same input through the fixed reader, which no longer runs the vulnerable file's regex scan at all. `_root_tenant_occurrences` calls `json.loads` with `object_pairs_hook=collect`, and `collect` fires once per object literal in the document, appending every `("tenant", value)` pair it sees at that level to a running list, in source order: for this input, one invocation, with three pairs recorded, giving `["tA", "tC", "tA"]` (the root object here has no nested objects, so this is also the hook's only invocation, which by definition is the last one). The set of those three values is `{"tA", "tC"}`, which has two elements rather than one, and the fixed logic refuses whenever that set's size is anything other than exactly one. The fix did not need to compare two readers' summaries at all; it needed to ask the one real parser for the full, unabridged list of what the document actually contained.

This is worth restating plainly, because it is the actual lesson the trace above was building toward: the vulnerable file's two readers each reported the identical value, `"tA"`, and by any comparison that only inspects what each reader's own summary returns, that agreement looks total. The disagreement was never in what the two readers reported to each other; it was in a third claim the raw bytes made that neither reader's own summary preserved, because both readers had already discarded it before returning anything. A verification strategy that only compares two readers' final answers, without asking whether either answer already discarded information on the way there, will never catch this class of gap — which is exactly why the fix does not compare summaries at all. It asks the parser itself, once, for everything, before any summarizing happens.

## What the checks do not prove

- Agreement between CPython's JSON handling and PostgreSQL's `jsonb` column type — untested by this fixture, and explicitly not assumed.
- GraphQL variable parsing, or agreement between a GraphQL reader and a REST reader for the same logical field.
- Unicode lookalike or normalization-based identifier spoofing.
- Authorization for an honest, unique-key object — that is a separate who-is-allowed question this module deliberately does not test, because parser agreement and authorization are different claims.

## Practice

```text
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl vulnerable
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl fixed
```

Run from `labs/2.1/2.1-parser-boundaries` directly if running from the repository root causes a collection error picking up unrelated files under `site/`. Map each of the six failing tests on the vulnerable run to a specific row in Lesson 02's design table. A setup error that prevents the tests from running at all is not evidence that the rule holds — if you cannot get a clean run, the practice is miswired, and the wiring is what needs fixing, never the assertions.

## Use it somewhere new

GraphQL and REST both ingest the same clinic appointment. Asserting HTTP 200 on a `/graphql` endpoint is not evidence of parser agreement between that endpoint and a parallel REST path — it only shows the GraphQL server accepted the request, which says nothing about whether a REST reader of the same logical field would reach the same conclusion. Write, in words rather than code, what a middle-duplicate-style test would look like for a GraphQL request whose `variables` JSON carries three occurrences of a duplicated `patient_id` key — three claims about one field, in the same JSON grammar as this lesson's three-occurrence object, arriving through a `variables` field instead of a note body. Do not test this against a live GraphQL target.

## What this page is not doing

Do not add live network traffic anywhere in this exercise, and do not log the messy object's contents as part of "improving" a test. Answer keys are not on this site; they live only in `content/assessment/keys/2.1.md`.
