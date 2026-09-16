# 2.1 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Bytes, text, formats, parsers, and interpreters

## Items

Nine module-specific items live in [`items.md`](items.md): two discrimination, three diagnosis, two design, one transfer, and one operate item, covering all five of this module's teaching claims (C1–C5, see `spec.md` §Teaching claims). Answers, distractor rationales, and four-state banding are in the isolated key at `content/assessment/keys/2.1.md` — do not open it before attempting the items.

## Evidence checklist

- [ ] Parser-boundary map naming every reader on the ingest path (Lesson 02)
- [ ] Local differential annotation: which two readers disagree, and on what specific input (Lesson 03)
- [ ] Transfer task (items.md #8): clinic REST/GraphQL scenario, naming which of C1–C5 change and which do not, with the GraphQL `variables`-JSON mechanism explained accurately (not the alias mechanism, which does not carry this defect)
- [ ] Lab `labs/2.1/2.1-parser-boundaries`: forbidden outcome **a parser differential where the ACL tenant disagrees with the stored tenant**
- [ ] `vulnerable/` tests: 6 of 9 fail for the stated security reason; `fixed/` tests: 9 of 9 pass (authorized local practice files only)
- [ ] Seeded review checklist answers (Lesson 08) — do not look at the key first
- [ ] Operate signal (items.md #9) that carries no note body or raw JSON text

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools or library names listed instead of a named reader-disagreement; missing trust boundary between readers; a check that compares two positions but is asserted as complete |
| Competent | System-specific rule stated and checked against the lab; lab result correctly mapped to a reader in the boundary map; operate signal present and free of raw content |
| Transfer-ready | Item 8 done: the `variables`-JSON mechanism explained accurately in the learner's own words (variable coercion happening once per operation is correctly distinguished from the transport JSON beneath it), connected explicitly to the "check every occurrence" principle from Lesson 03 |

Knowledge-check items (retryable) are items 1–5 in `items.md` (discrimination and diagnosis); design, transfer, and operate items (6–9) require satisfactory evidence, not a retry-to-80% threshold — a critical gap here (for example, a fix that only handles the two-key case) is not compensated by strong answers elsewhere.

## Seeded review

Apply the four-question checklist in `lessons/08-review.md` §Picture: problems to find to `vulnerable/parse_note.py` yourself before reading that lesson's worked example. Intended findings live only in `content/assessment/keys/2.1.md`.
