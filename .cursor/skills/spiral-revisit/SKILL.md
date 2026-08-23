---
name: spiral-revisit
description: After a module changes assets, boundaries, authority, data, or failure modes, update SecureCollab artifacts and list which prior tests and reviews must be re-run. Use at milestones or when identity, persistence, mobile, queues, or CDN assumptions change.
---

# Spiral revisit

## When to use

- After Pass B/C that changes SecureCollab assumptions
- At milestones M0–M5
- User asks what earlier artifacts are invalidated

## Instructions

1. Read blueprint §9.1 (phase evolution) and §9.2 (milestones). Read STATUS `milestones` and `spiral_deltas`.
2. Record a delta: which assets, boundaries, authority paths, retained data, dependencies, or failure modes changed.
3. Update or stub the affected SecureCollab design artifacts under `content/modules/` notes and, when those files exist, `content/reference/securecollab/` (create only markdown stubs if the code project does not exist yet). Do **not** start a greenfield product in this skill.
4. List prior tests, threat-model sections, and reviews that must be repeated. Write them into STATUS `spiral_deltas` and the module changelog.
5. Milestone evidence is not a feature demo: re-run the seven-step loop on the new assumptions.

| Milestone | After gate | Integrated evidence |
|---|---|---|
| M0 Observable skeleton | 2 | Browser → edge → API → DB path, traces, boundaries, non-goals |
| M1 Identity vertical slice | 4 | Account lifecycle, auth/recovery, sessions, authorization policy, abuse tests, revised threat model |
| M2 Secure web/API alpha | 7 | Persistence, data lifecycle, structural fixes, API/webhook/worker authority, regression pack |
| M3 Mobile slice | 8 | Hostile client, local/offline policy, native redirects, MASVS evidence |
| M4 Release candidate | 10 | Traceability, pipeline/deployment, SBOM/provenance, detections, restore, risk acceptance |
| M5 Defended capstone | 11 | Findings repaired, incident scenario, frozen evidence, architecture defense |
