# 0.1 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another. Check-in 0 stays **not attempted** until this evidence exists.

## Module

Security engineering orientation — five teaching claims (C1–C5), named in `spec.md` §Teaching claims: reachability is not authorization, a vocabulary term is not a target list, fail-closed on the unknown, noticing a denial is not capturing it, and exact-match allow-listing that does not travel across a redirect or alias.

## Evidence checklist

- [ ] Scope map naming the three allowed hosts and the stop condition (Lesson 02); WSTG, NICE, and CSF explicitly labeled as vocabulary, never as authorization
- [ ] Local reproduction of all three of this module's forbidden outcomes (Lesson 03): a public host, a lookalike host (`evillab.securecollab.test`-shaped), and a malformed URL, each treated as authorized
- [ ] Lab `labs/0.1/0.1-orientation`: `vulnerable/` tests show 4 of 7 failing for the stated security reasons; `fixed/` tests show 7 of 7 passing
- [ ] Assessment items (`content/modules/0/0.1/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Seeded review (Lesson 08) completed via the four-question checklist — do not open the key first
- [ ] Operate signal for a denied host (Lesson 06): `out_of_scope host=<hostname> reason=<reason>`, never a response body, never a screenshot
- [ ] Transfer task (Lesson 07) naming a concrete written artifact for both the contractor's customer WordPress and the company staging URL, and which claim each bad justification violates

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools or slogans offered as evidence ("WSTG," "a proxy," "a login page") for scope, without the written-allow-list rule (C1); missing forbidden-outcome lab evidence for the public host, the lookalike host, or the malformed URL |
| Competent | All five claims stated as system-specific properties of this course's `target_is_authorized` check, not standard names; all three lab forbidden outcomes reproduced and mapped to the claim each one tests; the operate signal excludes response bodies |
| Transfer-ready | Lesson 07's transfer task completed, naming a concrete written artifact for both the contractor WordPress and the staging URL, and correctly separating a C1 failure (reachability, a recognizable product) from a C2 failure (citing a standard as if it were permission), without Top 10/live-target/"Gate 0 complete" language standing in for either |

Knowledge check (retryable, 80% threshold): the seven module-specific items in `content/modules/0/0.1/assessment/items.md`.

## Seeded review

Use the local `vulnerable/` artifact via Lesson 08's four-question checklist. Intended findings and banding live only in `content/assessment/keys/0.1.md`.
