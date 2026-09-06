# Authoring pass notes — 6.4–6.7 (not independent review)

Date: 2026-09-06
Branch: `cursor/content-depth-2-4-c7cf`
Kind: authoring-pass conductor notes. **Not** an independent quality or lab-safety review. Does **not** confer `depth: publishable` or `quality: competent`.

## Modules

- 6.4 Files/paths — filename is data; join, canonicalize, prefix
- 6.5 SSRF / URL — preview URL is untrusted authority; predicate only, no fetch
- 6.6 Workflow — invite consume-once; fail-closed
- 6.7 Resource abuse — per-subject export quota; fourth denied

## What this pass did

Rewrote spec, `module.yaml`, eight lessons with named `## Mental model:` H2s and mermaid, lab README/tests, rubric, isolated keys, and SecureCollab stubs. Standards pinned to ASVS 5.0.0 exact ids. Level 3 items labeled advanced.

## What this pass did not do

Independent `quality-reviewer` / `lab-safety-reviewer` artifacts. Gates 0–10 and M0–M5 remain not-attempted. `revision.remaining` still lists these ids.

## Lab commands (authoring)

```
python3 -m pytest labs/6.4/6.4-lab/tests --impl vulnerable
python3 -m pytest labs/6.4/6.4-lab/tests --impl fixed
python3 -m pytest labs/6.5/6.5-lab/tests --impl vulnerable
python3 -m pytest labs/6.5/6.5-lab/tests --impl fixed
python3 -m pytest labs/6.6/6.6-lab/tests --impl vulnerable
python3 -m pytest labs/6.6/6.6-lab/tests --impl fixed
python3 -m pytest labs/6.7/6.7-lab/tests --impl vulnerable
python3 -m pytest labs/6.7/6.7-lab/tests --impl fixed
```

Vulnerable must fail forbidden-outcome tests. Fixed must pass.
