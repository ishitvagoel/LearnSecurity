# Reject eval in the review check

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A formatter pass does not reject `eval`. A later review bot is later. Writing down that eval is dangerous without rejecting it still returns true.

In plain words, the review asks the interpreter question. `review_ok` must be false when the diff contains `eval(`. That is the **lab stand-in** for “user input is not Python grammar.”

Put this in merge gating: `x = eval(user)` → not approved. Unknown dynamic execution denies in a real review even if this practice’s substring misses it. Do not treat the denylist as the whole avoid-eval rule. CI formatting the file does not approve eval.

## Picture: fail closed on eval

```mermaid
flowchart TD
  Diff[review_ok] --> Ev{"eval paren present?"}
  Ev -->|yes| Deny[reject]
  Ev -->|no| Allow[may approve]
```

The lab’s repaired files use `'eval(' not in diff`. Name the leftover: `exec(`, other expression languages, template filters that mark text as trusted, and generated code are not this check. Writing down that eval is dangerous without rejecting it is a different false assurance. Tests are still required after a human reject (next topic, 9.3).

You need to avoid eval — the lab string.

## What the repaired files must show

Do not treat `fixed/review.py` as a production review product.

| After the fix | Must be true |
|---|---|
| `x = eval(user)` | `review_ok` false |
| `x = int(user)` | `review_ok` true |

When you cannot tell whether the diff grants an interpreter, the answer is reject. A well-formed helper does not grant an interpreter.

## What this is not

A complete review check. A formatter. A later review bot. Writing down that eval is dangerous without rejecting it. A chat bot saying “looks safe.” A draft vocabulary sticker.

## What the tool cannot do

- Substring misses `exec(`, `__import__`, other expression languages, and template filters that mark text as trusted.
- Generated code can put eval back after review.
- Writing down that eval is dangerous without rejecting it.
- Tests still required (9.3).

## Practice

Name the leftover (substring is a stand-in). Run:

```text
python3 -m pytest labs/9.2/9.2-lab/tests --impl fixed
```

## Use it somewhere new

Terraform: reject `local-exec` interpolating untrusted names the same way 6.1 rejects a shell string.

## What can still go wrong

Substring stand-in; generated reintroduction; `exec(` / other expression languages; tests still required (9.3).

## What this page is not doing

Do not weaponize eval. A formatter screenshot is not a check-in. Do not present a draft vocabulary as final.
