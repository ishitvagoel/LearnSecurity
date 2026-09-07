# Allow-list tools in the runtime

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A system prompt is not the fix. Retrieval is not the fix. "We mapped a famous-bugs list so we shipped it" is not the fix.

The structural change is: `run_tool` **returns `None` unless `name in ALLOWED`**. Fail-safe: unknown tools deny. A denylist of the string `exec_sql` would still be every-other-interpreter. Structural means that membership — not "the prompt forbids SQL," not retrieval, not a famous-bugs mapping.

The lab allow-list is a **stand-in** for runtime membership before invoke. It is not a production agent product. The smallest restore for the notes app's optional summarizer is: `exec_sql` → None, `search_notes` may run. Fail-safe: if you are unsure whether the name is allow-listed, deny. Do not fail open because the model "only summarizes." Do not add `exec_sql` to `ALLOWED` "for debugging."

## Picture: tool-name allow-list gate

```mermaid
flowchart TD
  Call[run_tool] --> In{"name in ALLOWED?"}
  In -->|yes| Run[may run]
  In -->|no| Deny[None]
```

The repaired files require membership in `{"search_notes"}`. Production still needs that allow-list to be the *right* tools — `search_notes` that returns raw HTML is a lying encoding leftover. A coding assistant in CI that can `pip install` is the same allow-list grain on a different object. Cryptographically bound human approvals are extra, advanced work: a human click is not this check.

Industry lists ask for an allow-list before a tool runs. This week's check covers `exec_sql`.

## What the repaired files must show

Read `fixed/tools.py` against this checklist. Do not treat the snippet as a production agent product.

| After the fix | Must be true |
|---|---|
| `exec_sql` | None |
| `search_notes` | ran search_notes |

Fail closed: if you are unsure whether the name is allow-listed, deny. Uncertainty is a **no** on run, not a yes because the prompt looks careful.

## What this is not

- A system prompt.
- Retrieval as trust.
- A famous-bugs dashboard.
- An assurance gate sticker.
- Cryptographically bound approvals (extra, advanced leftover).
- Library defaults.
- A guidance document as the oracle.

## What the tool cannot do

- Allow-listed `search_notes` can still return HTML.
- Hallucinated package names in a coding assistant stay a later leftover.
- Cryptographically bound approvals are not this predicate.
- Agent credentials still need rotation.
- Retrieved chunks are untrusted clients.

## Practice

Name who can edit `ALLOWED`. Run:

```text
python3 -m pytest labs/E1/e1-lab/tests --impl fixed
```

It must pass. Run from the lab directory if a collection at the repo root is polluted. Then write one sentence: which rule is restored, and which leftover you refused to delete.

## Use it somewhere new

Coding assistant: deny shell / install tools in CI the same way — runtime allow-list, not a prompt.

## What can still go wrong

Allow-listed tool returns HTML. Hallucinated packages. Cryptographically bound approvals (extra, advanced). Leftover agent credentials.

## What this page is not doing

Do not call a live model. This page does not mark you as finished. from a famous-bugs screenshot. Do not present a system prompt as the allow-list.
