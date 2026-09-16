# <module-id> — independent review, <YYYY-MM-DD>

**Reviewed commit:** `<sha>` on `<branch>`
**Reviewer:** <agent or person>
**Independence statement:** I did not author or revise any file in this review's scope. <If false, stop — a different reviewer is required.>

## Files inspected

<Every file read, by path. A directory listing is not inspection.>

## Semantic scores

Score 0–3 against `.cursor/skills/quality-gate/references/publishability.md`. Cite a file path and a concrete passage or test result for every score. Word counts, headings, and schema validity are diagnostics only and never justify a score.

| Dimension | Critical | Score | Evidence |
|---|---|---|---|
| Property and question | yes | | |
| Attacker, authority, trust, state, time | yes | | |
| Causal explanation | yes | | |
| Worked reasoning | no | | |
| Practice and feedback | no | | |
| Safe executable lab | yes | | |
| Assessment alignment | yes | | |
| Standards accuracy | yes | | |
| Operations and human factors | no | | |
| Transfer and review triggers | yes | | |
| Safety and scope | yes | | |
| Editorial integrity | yes | | |

## Prose bar

Checked against `lesson-prose.mdc`. Linter output is necessary, not sufficient — record whether the words carried reasoning.

| Check | Result | Evidence |
|---|---|---|
| Derivation precedes assertion | | |
| Terms defined in dual form, then used | | |
| ≤3 rejected alternatives, each reasoned | | |
| One scope statement per lesson | | |
| Diagrams meet kind and node minimums | | |
| Cross-references resolve and are titled | | |
| Word floors carried reasoning, not padding | | |

## Coverage contract

Confirm no empty cells, and that ≥2 teaching claims carry lab assertions.

## Lab

Exact commands and real output, run in a clean environment:

```
$ python3 -m pytest labs/<id>/<id>-lab/tests --impl vulnerable
<output — must fail on the forbidden outcome>

$ python3 -m pytest labs/<id>/<id>-lab/tests --impl fixed
<output — must pass>
```

Tier: <1|2|3>. Test count: <n>. Anti-fake test: `<name>` — rejects <the plausible fake>.

## Blockers

Numbered, each naming a file and what would close it. Any critical dimension below 2 is a blocker and cannot be averaged away.

## Verdict

- [ ] `quality: developing` — any required dimension below 2
- [ ] `quality: competent` — every required dimension ≥2
- [ ] `depth: publishable` — every required dimension ≥2, all critical ≥2, clean lab pair passes, this artifact exists
- [ ] `quality: transfer-ready` — satisfactory evidence from the materially changed transfer task

STATUS was updated by: <reviewer or human>. An authoring agent may not write this line.
