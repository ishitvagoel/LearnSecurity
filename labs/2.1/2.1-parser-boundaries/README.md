# Lab: 2.1-parser-boundaries

**Module:** `2.1`
**Authorized scope:** this directory only. No other hosts, no live APIs, no public JSON bombs.
**Invariant (C1):** A note ingest that two readers interpret with **different tenant ids** is not accepted. Bytes → JSON is not "just text," and every occurrence of the tenant key must agree, not merely the first and the last.
**Root cause class:** parser / interpreter differential — the vulnerable checker also has a quieter second defect: it compares only the first and last occurrence, so a middle value that disagrees while the endpoints coincide is silently dropped rather than flagged.
**Tier:** 1 (predicate). `ingest_note` is a pure function over a JSON string with no request cycle or persisted state this claim depends on. See `lab-realism.mdc`.
**Non-goals:** public JSON bombs, live APIs, weaponized Unicode exploits, real patient or company identifiers.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/2.1/2.1-parser-boundaries`.

## Vulnerable behavior (local only)

`ingest_note` uses a first-key regex scan for the who-is-allowed check and `json.loads` (CPython's last-key-wins) for storage, then returns `accepted: True` unconditionally, never checking whether the two readers agree. Duplicate `"tenant"` keys make one company's note look like a different company's to one reader than to the other.

## Structural fix

Refuse when any two occurrences of `"tenant"` disagree — not merely when the first and the last disagree. Checking only the endpoints has a real gap: `{"tenant":"tA", ..., "tenant":"tC", ..., "tenant":"tA"}` has first == last == `"tA"`, so an endpoints-only check calls it agreement even though a middle claim of `"tC"` was made and silently overwritten. The fixed reader collects every occurrence and refuses unless the full set has exactly one value.

## Verify

```bash
python3 -m pytest tests/test_parser.py --impl vulnerable   # 4 of 6 fail
python3 -m pytest tests/test_parser.py --impl fixed         # 6 of 6 pass
```

From the repository root:

```bash
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl vulnerable
python3 -m pytest labs/2.1/2.1-parser-boundaries/tests --impl fixed
```

Six tests: the normal case; the module's forbidden outcome (two-key disagreement); a boundary case (three occurrences whose endpoints coincide while the middle disagrees); a malformed-input case (no tenant key at all); and a two-test anti-fake pair that constructs its own ambiguous and unambiguous objects — never seen in the module-level `CLEAN`/`AMBIGUOUS` constants — so a fake repair that special-cases those two exact strings cannot pass by memorizing them.

## Operate

Log rejected ambiguous bodies **without** storing the body or the raw text. Do not treat "`json.loads` succeeded" as evidence the property holds — it only proves one reader accepted the bytes, not that every reader agrees on their meaning.

## Transfer

Clinic REST and GraphQL both carrying `patient_id`: two grammars are two readers of the same logical field. Multipart filename encoding is a second acceptable sketch (a browser reader and an API reader on the same bytes) pointing at a later upload topic — still local, still fake data. See `lessons/07-transfer.md`.
