# E1 — AI, LLM, and agentic application security (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | denied_tool. |
| Signal (no bodies) | tool_denied{exec_sql}. |
| Revoke / recover | Revoke agent creds (7.4). |
| Residual | Hallucinated packages (10.2) in copilot use. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/E1/e1-lab`.

## Transfer

Copilot in CI.

## Usability

Human approval UI for tools must be accessible; otherwise operators auto-approve.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
