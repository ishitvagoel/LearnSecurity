# Would you merge this always-run run_tool?

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

Look at `labs/E1/e1-lab/vulnerable/` as a summarizer-agent PR. Does `run_tool("exec_sql", {})` still run?

Start with `run_tool` and the `exec_sql` row. A famous-bugs screenshot is the wrong evidence. Until `test_exec_sql_tool_is_denied` passes, "will allow-list later" is unfinished work.

## Picture: exec_sql available

**`exec_sql` available**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|exec_sql runs| Property["Rule - good if tested"]
  Q -->|prompt forbids SQL| Mechanism[Tool - string]
  Q -->|famous-bugs mapped| False[False assurance]
```

`exec_sql` is still None. If the change never checks allow-list membership, that always-run leftover is still open. A prompt screenshot does not replace that check.

Retrieved docs are untrusted. Coding-assistant install tools are a later leftover. Name them, do not skip `test_exec_sql_tool_is_denied`. This page does not mark you as finished. Do not call a live model to prove the finding.

## Problems to find (name them yourself)

- `exec_sql` available
- Policy only in the system prompt
- No denied-tool test
- Retrieved docs trusted

Also reject: live model attacks; shipping without re-running `test_exec_sql_tool_is_denied`; keys in learner notes; treating this model-tool lesson as a check-in.

## Common mix-ups

- A famous-bugs list is the rulebook for AI
- Retrieval is safe because it is "our data"
- The model is what you trust
- A system prompt is complete mediation
- A famous-bugs mapping is `run_tool`

## Use it somewhere new

A system prompt and a famous-bugs mapping, without an allow-list, do not gate the tool. A safe prompt is not an allow-list — write the `exec_sql` deny.

## Can people still use it

A denied tool must say why it stayed out (`exec_sql` not allow-listed), not only "will allow-list later."

## What this page is not doing

Do not ship always-run `exec_sql` because a comment promises an allow-list later. Do not jailbreak a public model to prove the finding.
