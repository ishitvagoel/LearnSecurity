# 3.2 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another.

## Module

Threat modeling — four teaching claims (C1–C4), named in `spec.md` §Teaching claims: a green scanner result cannot stand in for the versioned model's always-name set, a threat id present in the model cannot stand in for a traced flow, a priority ranking cannot stand in for a mitigation decision, and a self-reported update date cannot stand in for a recorded re-review.

## Evidence checklist

- [ ] Version-controlled threat-model document (Lesson 02) naming SecureCollab's Phase 3 actors, principals, boundaries, and flow ids, including `worker-share-redelivery` as a distinct flow from `member-note-read`
- [ ] Local reproduction of the module's forbidden outcome (Lesson 03): a green scanner result passing a threat model missing `cross-tenant-read` entirely
- [ ] Lab `labs/3.2/3.2-lab`: `vulnerable/` tests show 7 of 9 failing for the stated security reasons; `fixed/` tests show 9 of 9 passing
- [ ] Assessment items (`content/modules/3/3.2/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Operate signals (Lesson 06) for a missing or stale mandatory threat, naming a reason code and a threat id, never a note body, session token, or mitigation text, with a stated alert-scoping rationale
- [ ] Transfer task (Lesson 07) applying the always-name/flow-tracing/prioritized-mitigation/recorded-re-review structure to clinic SMS reminders, correctly rederiving new always-name threats rather than reusing `cross-tenant-read` verbatim
- [ ] Seeded review (Lesson 08) correctly locating the reintroduced scanner short-circuit and the substring-based mandatory-id check in `labs/3.2/3.2-lab/review/candidate_fix.py`, and correctly weighing the cosmetic global rename as a low-priority question rather than an equivalent-severity finding

## Rubric

| Result | Meaning |
|---|---|
| Developing | Treats a green scanner, a STRIDE workshop, or a code comment as evidence the threat model is current; missing forbidden-outcome lab evidence for the mandatory-id check |
| Competent | All four claims stated as system-specific properties of SecureCollab's CI gate and Phase 3 flows, not tool names or generic threat-modeling slogans; every lab forbidden outcome reproduced and mapped to the claim it tests; a threat id correctly distinguished from a traced flow |
| Transfer-ready | Lesson 07's transfer task completed, correctly rederiving new always-name threats, flows, and a trigger for a channel no HTTP scanner enumerates, without a vendor questionnaire or a Top 10/CWE list standing in for the derivation |

Knowledge check (retryable, 80% threshold): the eight module-specific items in `content/modules/3/3.2/assessment/items.md`.

## Seeded review

Use the local `labs/3.2/3.2-lab/review/candidate_fix.py` artifact via Lesson 08's reading order. Intended findings and banding live only in `content/assessment/keys/3.2.md`.
