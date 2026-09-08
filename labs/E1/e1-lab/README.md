# Lab E1 — a model proposal is not authorization

**Module:** `E1`
**Authorized scope:** this directory only. Local course fixture. No live model APIs, production agents, or third-party LLM hosts.
**Invariant:** `run_tool("exec_sql", {})` is `None`. Allowlisted `search_notes` may run.
**Root cause class:** model output treated as policy
**Non-goals:** LLM Top 10 as the syllabus; claiming Gate 7 or M2.

The allowlist is a **teaching stand-in** for AISVS `v1.0-C9.5.3` (policy never by the model). It is not LangChain.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/E1/e1-lab`, then run `git restore --source=HEAD -- labs/E1/e1-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`run_tool` runs any name. Forbidden outcome: agent executes `exec_sql` because the model asked.

## Structural fix

Require `name in ALLOWED`. A system-prompt “never call exec_sql” is not this cell.

## Verify

```
python3 -m pytest labs/E1/e1-lab/tests --impl vulnerable
python3 -m pytest labs/E1/e1-lab/tests --impl fixed
```

The first command must fail on `exec_sql`. The second must pass. Honest `search_notes` may pass on both.

## Operate

Signal: `tool_denied`. Do not log note bodies or model transcripts. Do not claim Gate 7.

## Transfer

Clinic summarizer over charts. Copilot in CI. Prompt only.
