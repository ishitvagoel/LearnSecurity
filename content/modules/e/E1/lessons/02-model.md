# E1 — AI, LLM, and agentic application security (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | model, user, tool exec_sql |
| Objects | tool name |
| Actions | run_tool |
| Channels | prompt, tool router |
| TCB | Allow-list in code, not in the prompt text. |
| Untrusted | System prompt, retrieved notes, model output |
| State / time | One agent turn. |
| 1.1 cell | Authorization of tools — complete mediation for the agent. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| agent | summarize | run | allow |
| agent | exec_sql | run | deny |
| note body | prompt | steer | untrusted |
| human | high-impact tool | approve | HITL |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/E1/e1-lab` file `tools.py`.

## Transfer

Copilot in CI.

## Residual risk

Hallucinated packages (10.2) in copilot use.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
