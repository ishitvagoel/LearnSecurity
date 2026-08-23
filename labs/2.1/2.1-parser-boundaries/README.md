# Lab: 2.1-parser-boundaries

**Module:** `2.1`  
**Authorized scope:** this directory only.  
**Invariant:** A note ingest that two parsers interpret with **different tenant ids** is not accepted. Bytes→JSON is not “just text.”  
**Root cause class:** parser / interpreter differential  
**Non-goals:** public JSON bombs, live APIs, weaponized Unicode exploits.

## Reset

Restore `vulnerable/` and `fixed/` from git. Synthetic JSON only.

## Vulnerable behavior (local only)

`ingest_note` uses a first-key scanner for ACL and `json.loads` (last key wins in CPython) for storage. Duplicate `"tenant"` keys make bob’s note look like tA to one interpreter and tB to the other.

## Structural fix

Reject when first and last tenant disagree (fail-safe). Canonicalization is the mechanism; “sanitize quotes” is not.

## Verify

```bash
python3 -m pytest tests/test_parser.py --impl vulnerable   # fail duplicate-key test
python3 -m pytest tests/test_parser.py --impl fixed
```

## Operate

Log rejected ambiguous bodies **without** storing the body. Do not treat `JSON.parse` success as the property.

## Transfer

Multipart filename encoding: two parsers (browser vs API) on the same bytes — new 6.4 surface.
