# E1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready. Gate 7 and M2 stay **not-attempted**. Elective.

## Module

AI, LLM, and agentic application security

## Evidence checklist

- [ ] Tool-allowlist map; model/prompt/RAG labeled as not policy
- [ ] Transfer task (clinic summarizer; Copilot in CI named)
- [ ] Lab `labs/E1/e1-lab`: forbidden outcome **agent executes exec_sql because the model asked**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without transcripts: `tool_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “RAG / LLM03 / prompt” slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-LLM/Gate-7 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **E1**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/E1.md`.
