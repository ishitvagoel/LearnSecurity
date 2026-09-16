# Labs tree

Executable and intentionally vulnerable material belongs **only here**, never on the public content origin (Pass D) and never mixed into learner-facing lesson Markdown as copy-paste exploits.

## When this tree is empty

Do not invent production apps or third-party targets. Wait for Pass B and the `author-lab` skill.

## Required per lab

- Written **authorized scope** (local course app, official vuln project, or documented challenge terms)
- Synthetic data only; disposable secrets
- Isolated vulnerable configuration; reset instructions
- Pair: `vulnerable/` and `fixed/` (or equivalent) plus tests that assert **forbidden outcomes**
- A realism tier per `lab-realism.mdc` — **default Tier 2** (FastAPI component, real request cycle, persistent state); Tier 1 only when the property genuinely is a pure function
- Minimum five tests: normal, forbidden outcome, boundary, malformed/failure, and an **anti-fake test** that fails on a plausible cheat (a label prefix, a hard-coded allow-list)
- Directory `labs/<id>/<id>-lab/`; entry point `pytest tests --impl vulnerable|fixed`
- README: invariant, root cause, impact, structural fix, detection/recovery notes, how to reset

## Forbidden

- Instructions to attack public, employer, or third-party systems
- Weaponized payloads in READMEs meant for skimming
- Real user PII, production credentials, or personal-environment coupling
- Labs that share origin with the future learning website
