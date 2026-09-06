# E1 — AI, LLM, and agentic application security

Pass A specification. Lesson prose lives in `lessons/`. A model-proposed tool name is not authorization. Do not mark Gate 7 or M2 complete.

## Identity

- **id:** E1
- **slug:** ai-llm-and-agentic-application-security
- **title:** AI, LLM, and agentic application security
- **phase / track / difficulty:** 7 / elective / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Opens after Phase 7; 1.2 mediation; 6.1 interpreters; 8.1 hostile client; 9.2 generated-code review; 10.2 hallucinated packages.
- **routeTags:** complete, elective
- **releaseMilestone:** M2
- **masteryGate:** 7

## Objective hierarchy

1. Produce a **tool predicate** so `run_tool("exec_sql", {})` is `None`.
2. Name attacker capabilities (prompt injection in a note; poisoned retrieval) and trust assumptions (local `run_tool`; the model is outside the TCB).
3. Transfer: clinic summarizer over charts; Copilot in CI — without treating an LLM Top 10 list as ASVS.

## Prerequisite concepts

8.1 the client is hostile; 6.1 the interpreter believes the string; 7.4 leftover credentials; 10.2 name is not a digest.

## Misconceptions

- LLM Top 10 is ASVS for AI.
- RAG is safe because it is “our data.”
- The model is in the TCB.
- A system prompt is complete mediation.

## Concept map

Always-true `run_tool` (break) → allowlist (this module) → human approval for high impact (AISVS C9.2) → retrieved docs untrusted (5.1) → hallucinated packages (10.2). Residual: prompt-only “never call exec_sql.”

## Invariant prompts

- What must remain true for `run_tool("exec_sql")`?
- What fails if policy lives only in the system prompt?

## Threat-model prompts

- What can a note body make the agent do?
- What residual remains if search_notes is allowlisted but returns untrusted HTML (6.2)?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/E1/e1-lab`. Forbidden: agent executes `exec_sql` because the model asked. No live LLM APIs.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP AISVS 1.0 (final, 2026-06-24): `v1.0-C9.5.3` policy never by the model (Level 2); `v1.0-C9.3.7` allow-list before invoke (Level 2); `v1.0-C9.2.8` cryptographically bound approvals is **Level 3, labeled advanced**.
- OWASP ASVS 5.0.0 (final): `v5.0.0-8.2.1` authorization on every access; `v5.0.0-13.2.1` backend service accounts — the agent is another principal.
- OWASP GenAI LLM Top 10 2026 (awareness, published 2026-08-04): LLM03 Excessive Agency after the allowlist cause, not the syllabus.
- NIST AI 600-1 GenAI Profile (final, 2024-07-26) and NIST SP 800-218A (final, 2024-07-26): guidance, not the lab oracle.

## Review triggers

`exec_sql` available; policy only in the system prompt; no denied-tool test; retrieved docs trusted.

## Time budget and SecureCollab

Optional summarizer agent. Evidence: tool allowlist tests. Elective — not a core gate.

## Operational considerations

`tool_denied`. Revoke agent creds (7.4). Hallucinated packages (10.2) in copilot use.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: model is not TCB; AISVS C9.5.3; LLM Top 10 awareness |
