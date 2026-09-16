# Lab: 2.1-parser-boundaries

**Module:** `2.1`
**Authorized scope:** this directory only. No other hosts, no live APIs, no public JSON bombs.
**Invariant (C1):** A note ingest that two readers interpret with **different tenant ids** is not accepted. Bytes → JSON is not "just text," and every occurrence of the tenant key **at the top level of the note object** must agree, not merely the first and the last, and not any occurrence nested inside a different field.
**Root cause class:** parser / interpreter differential. The vulnerable checker has two defects: it never compares its two readers' outputs at all, and its first-key regex scan does not distinguish a top-level occurrence from one nested inside another field.
**Tier:** 1 (predicate). `ingest_note` is a pure function over a JSON string with no request cycle or persisted state this claim depends on. See `lab-realism.mdc`.
**Non-goals:** public JSON bombs, live APIs, weaponized Unicode exploits, real patient or company identifiers.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/2.1/2.1-parser-boundaries`.

## Vulnerable behavior (local only)

`ingest_note` uses a first-key regex scan for the who-is-allowed check and `json.loads` (CPython's last-key-wins) for storage, then returns `accepted: True` unconditionally, never checking whether the two readers agree. Duplicate `"tenant"` keys make one company's note look like a different company's to one reader than to the other.

## Structural fix

The fix went through two designs before landing on the one shipped here, and both earlier attempts are worth knowing about because each closed one gap while leaving another open.

The first attempt kept the two-reader structure and had the regex-based reader compare every occurrence it found against every other occurrence, refusing on any disagreement — closing the case a first-versus-last comparison alone misses: `{"tenant":"tA", ..., "tenant":"tC", ..., "tenant":"tA"}` has first == last == `"tA"`, so an endpoints-only check calls it agreement even though a middle claim of `"tC"` was made and silently overwritten. That attempt still used a regex to find occurrences, and a regex matching only quoted-string values cannot see a non-string occurrence (`{"tenant":1,"tenant":"tA"}` has one occurrence a string-only pattern is blind to) or a key spelled with a Unicode escape sequence.

The shipped fix abandons the second reader entirely. `fixed/parse_note.py` asks `json.loads`'s own `object_pairs_hook` for every key/value pair in the note object, which is driven by the real JSON grammar rather than an approximation of it, and so correctly sees every occurrence regardless of value type or key escaping. This is Lesson 04's Candidate B in its single-reader form: rather than checking that two independently-implemented readers agree, restructure so only one reader — the real one — ever produces a value anyone consumes.

That fix introduced its own gap, caught by independent review before it shipped: `object_pairs_hook` fires for every object literal in the document, at every nesting depth, not only the top-level note object. Collecting "every occurrence of tenant, anywhere in the document" let a note with **no top-level tenant field at all** be accepted, using a company id scraped from a nested object the submitter fully controlled. The final fix collects occurrences only from the hook's *last* invocation, which is always the root object — every object nested inside it is fully resolved before the root's own pairs are handed to the hook.

## Verify

```bash
python3 -m pytest tests/test_parser.py --impl vulnerable   # 6 of 9 fail
python3 -m pytest tests/test_parser.py --impl fixed         # 9 of 9 pass
```

From the repository root:

```bash
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl vulnerable
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl fixed
```

Nine tests: the normal case; the module's forbidden outcome (two-key disagreement); a boundary case (three occurrences whose endpoints coincide while the middle disagrees); a malformed-field case (no tenant key at all); a non-string-value case (a regex-only reader is blind to it); a malformed-JSON-syntax case; a nested-tenant case (a tenant key inside a different field must not be mistaken for the top-level claim); and a two-test anti-fake pair that constructs its own ambiguous and unambiguous objects — never seen in the module-level `CLEAN`/`AMBIGUOUS` constants — so a fake repair that special-cases those two exact strings cannot pass by memorizing them.

## Operate

Log rejected ambiguous bodies **without** storing the body or the raw text. Do not treat "`json.loads` succeeded" as evidence the property holds — it only proves the bytes were valid JSON, not that the note object made exactly one top-level claim about its tenant.

## Transfer

Clinic REST and GraphQL both carrying `patient_id`: a GraphQL request's `variables` field is itself JSON, sent over the same wire as a REST body — the same grammar this lab is about, not a second one. Multipart filename encoding is a second acceptable sketch (a browser reader and an API reader on the same bytes) pointing at a later upload topic — still local, still fake data. See `lessons/07-transfer.md`.
