# Practice: declared_len plus 8

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Try it

The practice is not a website you attack. It is a tiny in-process `copy_into(bufsize, src, declared_len)`. It does not compile a C overflow, spray a heap, or fuzz a third-party binary. The failure is already in the object: the copy uses `declared_len` plus 8. That is a **failed rule**, not extra slack you needed.

The rule under test:

> `len(copy_into(4, b"abcdefgh", 4))` must be ≤ 4. A short honest copy may fit. Checking every path here means the copy is bounded by destination size.

## Where you may practice

Only `labs/E4/e4-lab` is in scope. Fake bytes: `abcdefgh`. Restore the broken and repaired folders when you are done.

Do not compile a C overflow. Do not spray a heap. Do not fuzz a third-party binary, an employer codec, or anyone else’s unpacker.

What must not happen: copy into a 4-byte lab buffer returns more than 4 bytes. `len(copy_into(4, b"abcdefgh", 4)) > 4`.

Who could do this: a hostile header `declared_len`. That stands in for “the app is mostly Kotlin so copies are safe,” a sanitizer in CI treated as the rule, or an awareness-list mapping treated as this rule. What is supposed to stop this: `copy_into` bounds the copy by **destination size**. Python slicing, a company language roadmap, and FastAPI are not enough.

## Picture: extra eight bytes are not a gift

```mermaid
sequenceDiagram
  participant H as header declared_len 4
  participant S as src 8 bytes
  participant V as broken copy
  H->>V: copy 4 plus 8
  S->>V: abcdefgh
  V-->>V: destination length 8
```

The broken files copy `src[: declared_len + 8]`. For an 8-byte source that is the whole buffer — longer than `bufsize` 4. Do not treat the `+ 8` as a C exploit size. What has to be true first: declared length is trusted over destination size. You do not need a compiler. You must not ship a native walkthrough.

An earlier topic already said path length is checking every path for *which file*. This rule is **spatial length at the copy**. This page does not finish a check-in.

## What to look at: the cause, not a trophy

Read `vulnerable/copy.py`. It returns more than `bufsize` bytes. Checks:

- `test_copy_does_not_exceed_buffer`
- `test_short_copy_may_fit` — short honest copy may pass on both

You do not need a new source. The failure of `test_copy_does_not_exceed_buffer` *is* the evidence.

## Why it happens, what it costs, how you stop it, how you notice, how you recover

| Slice | This practice |
|---|---|
| The rule | `len(copy_into(4, b"abcdefgh", 4)) <= 4` |
| Why it happens | Declared length trusted over destination size |
| What has to be true first | Copy uses `declared_len` plus 8 |
| Trigger | Header claims 4; payload is 8 |
| What it costs | Destination longer than bufsize |
| How you stop it | `min(bufsize, declared_len, len(src))` |
| How you notice | `copy_length_denied`; never file bytes |
| How you recover | Reject the blob; patch the parser |
| Not the lesson | A C exploit, an awareness-list dashboard, or a course gate |

## What the framework does vs what you still have to check

Python slicing will not save a C copy. A memory-safe language reduces this overwrite class **in that language**. Helpers that call C, and leftover codecs, still copy. What this practice is supposed to show: length ≤ 4.

## Practice

```text
python3 -m pytest labs/E4/e4-lab/tests --impl vulnerable
```

Run from `labs/E4/e4-lab` if a repo-root collection picks up `site/`. Record `test_copy_does_not_exceed_buffer`. Do not compile native walkthroughs. A setup error is not proof the rule holds.

## Use it somewhere new

Clinic image parser: predict the oversize copy without leaving this directory. Do not fuzz a third-party codec.

## What this page is not doing

No public-binary, production-unpacker, or weaponized overflow instructions. Do not claim a course gate. An awareness-list name stays awareness after the cause.
