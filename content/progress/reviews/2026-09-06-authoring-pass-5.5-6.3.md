# Authoring pass notes — 5.5 and 6.1–6.3 (not independent review)

Date: 2026-09-06
Branch: `cursor/content-depth-2-4-c7cf`
Kind: authoring-pass conductor notes. **Not** an independent quality or lab-safety review. Does **not** confer `depth: publishable` or `quality: competent`.

## Modules

- 5.5 Database and persistence security — data vs SQL grammar; three gates (1.2, parameters, 3.3 role); RLS is extra
- 6.1 Interpreter confusion — data vs shell grammar; argv list; denylist refused
- 6.2 Browser injection — HTML text encoding; CSP3/Trusted Types draft
- 6.3 Cross-site — ambient cookies are not consent; origin × token

## What this pass did

Rewrote spec, `module.yaml`, eight lessons with named `## Mental model:` H2s and mermaid, lab README/tests, rubric, isolated keys, and SecureCollab stubs. Standards pinned to ASVS 5.0.0 exact ids. Level 3 items labeled advanced.

## What this pass did not do

Independent `quality-reviewer` / `lab-safety-reviewer` artifacts. Gates 0–10 and M0–M5 remain not-attempted. `revision.remaining` still lists these ids.

## Lab commands (authoring)

```
python3 -m pytest labs/5.5/5.5-lab/tests --impl vulnerable
python3 -m pytest labs/5.5/5.5-lab/tests --impl fixed
python3 -m pytest labs/6.1/6.1-lab/tests --impl vulnerable
python3 -m pytest labs/6.1/6.1-lab/tests --impl fixed
python3 -m pytest labs/6.2/6.2-lab/tests --impl vulnerable
python3 -m pytest labs/6.2/6.2-lab/tests --impl fixed
python3 -m pytest labs/6.3/6.3-lab/tests --impl vulnerable
python3 -m pytest labs/6.3/6.3-lab/tests --impl fixed
```

Vulnerable must fail forbidden-outcome tests. Fixed must pass.
