# E1 — AI, LLM, and agentic application security (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
Review `labs/E1/e1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): exec_sql available
- Seeded smell (label it yourself): Policy only in the system prompt
- Seeded smell (label it yourself): No denied-tool test
- Seeded smell (label it yourself): Retrieved docs trusted

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- LLM Top 10 is ASVS for AI
- RAG is safe because it is “our data”
- The model is in the TCB

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Copilot in CI.

## HITL / WCAG 2.2

Human approval UI for tools must be accessible; otherwise operators auto-approve.
