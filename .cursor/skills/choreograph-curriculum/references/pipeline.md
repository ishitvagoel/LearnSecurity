# Ordered skill pipeline

Conductor: `choreograph-curriculum`. Inner skills own the procedure.

```text
next-iteration
  -> standards-pin
  -> author-module-spec          # Pass A
  -> quality-gate                 # spec bar
  -> author-lesson                # Pass B (after pilot rules)
  -> author-lab                   # Pass B
  -> author-assessment            # Pass C
  -> spiral-revisit
  -> quality-gate                 # publishability bar
  -> coverage-audit               # end of a completed phase only
```

Slash-only helpers the conductor may call as a **mode**, not as a hidden extra loop:

- `pilot-phase-1` — Pass A for 1.1–1.4 then stop
- `coverage-audit` — map vs ASVS/MASVS/awareness lists

Post-generation revision is a **separate** conductor: [`deepen-curriculum`](../../deepen-curriculum/SKILL.md).
