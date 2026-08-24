# E1 — AI, LLM, and agentic application security (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Agent executes exec_sql because the model asked |
| Failure | Fail closed: Allow-list; no exec_sql; human approval for high impact |

Lab tests: `test_property.py` under `labs/E1/e1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Agent executes exec_sql because the model asked`
- `--impl fixed`: **pass**

exec_sql denied.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Copilot in CI.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
