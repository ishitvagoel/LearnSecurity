# Target shape of each lesson

Word counts are **floors that make room for reasoning**, not targets to pad toward. All eight files keep the existing frontmatter (`**Kind:**`, `**Loop step:**`); `01` and `05` add `**Standards:**`.

Headings below are described by what the section *does*. Do not copy them as literal heading text — `lesson-prose.mdc` forbids repeated scaffolding.

---

## `01-property.md` — Property · concept-model · 1,200–2,000 words

Open with teaching claim 1 as a single falsifiable sentence. Then:

- Unpack every clause of that sentence and say what would make it false.
- Define each technical term on first use in dual form.
- One trust-boundary diagram, ≥5 nodes, ≥2 distinct authority paths.
- Name what must be trusted **for this claim**, then show the list changing when the claim changes. `1.3/lessons/01-property.md` does this well: it lists what secrecy needs, then what availability needs, and they differ.
- State the attacker's capabilities explicitly, and the ones deliberately excluded.
- Close by previewing the remaining claims by name, with links.

Include the `**Standards:**` line with exact identifiers, version, and status.

## `02-model.md` — Model · design-exercise · 1,200–2,000 words

- A table with columns *word*, *precise question*, *this system, this phase* — covering actor, principal, component, channel, entry point, trust boundary. Copy the discipline of `1.3/lessons/02-model.md`, not its content.
- **Two worked discriminations**: one place that looks like a boundary and is not (a transparent relay adds a network hop but changes no assumption), and one that does not look like one and is (two functions in one process, where one cannot represent worker authority).
- State, time, and concurrency: what can change between the check and the use.
- One diagram — state machine, or data flow with authority annotations.

## `03-break.md` — Break · mechanism-lab · 900–1,500 words

- Derive the representative failure; do not announce it. Preconditions, the exact step where authority or grammar or state goes wrong, then blast radius.
- **One** authorized-scope sentence, immediately before the first command.
- Name the failing test and say what its failure means.
- Explain why this is the *smallest* representative failure: what was deliberately left out, and why leaving it out does not change the cause.
- No payloads, no live targets.

## `04-build.md` — Build · design-exercise · 1,000–1,600 words

- Derive the fix from the property. The reader should be able to predict the fix before reading it.
- Compare **two** candidate mechanisms honestly, one of which a competent engineer would reasonably propose, and say precisely where the weaker one breaks.
- State where the chosen mechanism itself stops working.
- Separate framework default from application guarantee with a concrete example of the default being insufficient — not the assertion that it is.

## `05-verify.md` — Verify · verification-lab · 900–1,500 words

- Normal, negative, abuse, and failure cases; for each, the observation that distinguishes a pass from a pass-for-the-wrong-reason.
- Explain the oracle: **why** this assertion catches the forbidden outcome, and what a green suite still does not prove.
- Describe the anti-fake test and the fake it rejects.
- `**Standards:**` line with exact identifiers.

## `06-operate.md` — Operate · operations-exercise · 900–1,400 words

- Signal design: the fields that make the signal useful, and **which field is omitted and why** — a log that carries the secret is a second leak.
- Alert threshold and its false-positive cost; who receives it.
- Containment, revocation, recovery.
- Accessibility and usability of any human-in-the-loop path (blueprint §16.12).
- Model operator failure as residual risk: what happens when nobody reads the alert.

## `07-transfer.md` — Transfer · transfer-challenge · 900–1,500 words

Change an **asset, actor, authority relation, boundary, state transition, or time horizon** — not product nouns. Swapping "notes app" for "clinic" while keeping every assumption is a rename, which is what most current transfer lessons do.

State explicitly which original claims survive the change, which break, and why. Give success criteria, not a step-by-step scaffold — the point is performance without the scaffold.

## `08-review.md` — Code review · code-review · 900–1,400 words

- A realistic diff of 10–40 lines in `labs/<id>/review/`, with 3–5 seeded issues of differing severity.
- **At least one plausible non-issue** that looks like a finding. Learning to not report it is half the skill.
- Teach the reading order — where authority is resolved, where state changes, where data crosses a grammar — instead of listing what to find.
- Findings and their rationales live only in `content/assessment/keys/<id>.md`.
