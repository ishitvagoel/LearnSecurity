# E1 — AI, LLM, and agentic application security (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
**Mechanism (not the property):** LangChain default tools are not your matrix.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For E1 |
|---|---|
| Root cause | Model output treated as policy. |
| Preconditions | run_tool('exec_sql') executes. |
| Impact (1.1 cell) | Authorization of tools — complete mediation for the agent. — Interpreter 6.1 via English. |
| Prevention | Allow-list; no exec_sql; human approval for high impact. |
| Detection | denied_tool. |
| Recovery | Revoke agent creds (7.4). |

## Framework defaults vs application guarantees

LangChain default tools are not your matrix.

## Mechanism limits and bypasses

Prompt “never call exec_sql” is not mediation.

Indirect injection via 5.1 analytics copy.

## Residual risk

Hallucinated packages (10.2) in copilot use.

## Practice

List tools and who may call them.

Run `labs/E1/e1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Copilot in CI.

Clinic summarizer over charts.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Human approval UI for tools must be accessible; otherwise operators auto-approve.
