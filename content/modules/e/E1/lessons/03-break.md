# E1 — AI, LLM, and agentic application security (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
**Forbidden outcome:** Agent executes exec_sql because the model asked

**Authorized scope:** `labs/E1/e1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable tools.py allows exec_sql.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: run_tool('exec_sql') executes.

## Vulnerable fixture (local)

```python
def run_tool(name, args):
    return f'ran {name}'
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Model output treated as policy. |
| Impact | Interpreter 6.1 via English. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/E1/e1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Copilot in CI.

## Non-goals

No live-target instructions. Synthetic data only.
