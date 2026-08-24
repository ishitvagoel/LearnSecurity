# E1 — AI, LLM, and agentic application security (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.

## Property (start here)

The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.

## Attacker capabilities and trust assumptions

- **Attacker:** Prompt injection in a note body; malicious retrieved doc.
- **Trust:** Local run_tool(name).
exec_sql => None.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
ALLOWED={'search_notes'}
def run_tool(name, args):
    if name not in ALLOWED:
        return None
    return f'ran {name}'
```

## Why this restores the cell

Allow-list; no exec_sql; human approval for high impact.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

LangChain default tools are not your matrix.

Prompt “never call exec_sql” is not mediation.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Copilot in CI.

## Residual risk

Hallucinated packages (10.2) in copilot use.
