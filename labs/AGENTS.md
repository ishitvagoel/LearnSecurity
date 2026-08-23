# Labs tree

Executable and intentionally vulnerable material belongs **only here**, never on the public content origin (Pass D) and never mixed into learner-facing lesson Markdown as copy-paste exploits.

## When this tree is empty

Do not invent production apps or third-party targets. Wait for Pass B and the `author-lab` skill.

## Required per lab

- Written **authorized scope** (local course app, official vuln project, or documented challenge terms)
- Synthetic data only; disposable secrets
- Isolated vulnerable configuration; reset instructions
- Pair: `vulnerable/` and `fixed/` (or equivalent) plus tests that assert **forbidden outcomes**
- README: invariant, root cause, impact, structural fix, detection/recovery notes, how to reset

## Forbidden

- Instructions to attack public, employer, or third-party systems
- Weaponized payloads in READMEs meant for skimming
- Real user PII, production credentials, or personal-environment coupling
- Labs that share origin with the future learning website
