# 1.4 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready.

## Module

Risk, people, economics, usable security, and resilience

## Items

Nine module-specific items live in [`items.md`](items.md): two discrimination, three diagnosis, two design, one transfer, and one operate item, covering all five of this module's teaching claims (C1–C5, see `spec.md` §Teaching claims). Answers, distractor rationales, and four-state banding are in the isolated key at `content/assessment/keys/1.4.md` — do not open it before attempting the items.

## Evidence checklist

- [ ] Risk register for the recovery-confirm journey, with assumptions, user-harm scenarios (at least three, in complete sentences, per Lesson 02), residual risk, and named owners
- [ ] WCAG-oriented review notes for this one journey specifically — not a claim of full-product conformance
- [ ] Transfer task (items.md #8): clinic and banking sketches, naming which of C1–C5 change and which do not
- [ ] Lab `labs/1.4/1.4-risk-register`: forbidden outcome **a high-impact recovery control is color- or mouse-only**
- [ ] `vulnerable/` tests: 3 of 6 fail for the stated security reason; `fixed/` tests: 6 of 6 pass (authorized local practice files only)
- [ ] Seeded review walkthrough (Lesson 08) — do not look at the key first
- [ ] Operate signal (items.md #9) that carries no recovery codes or note bodies

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed instead of a named harm; missing attacker capability or trust boundary; a residual with no owner or trigger |
| Competent | System-specific rule stated and checked against the lab; lab result correctly mapped to a register row; operate signal present and privacy-safe |
| Transfer-ready | Item 8 done: at least one claim reworded (not merely restated) for the clinic/bank setting, with the coercion invariance explained in mechanism terms |

Knowledge-check items (retryable) are items 1–6 in `items.md`; design, transfer, and operate items (7–9) require satisfactory evidence, not a retry-to-80% threshold — a critical gap here (for example, allowing the support-read-aloud row without an audit mechanism) is not compensated by strong answers elsewhere.

## Seeded review

Apply the four-question checklist in `lessons/08-review.md` §The submission under review to both submissions in that lesson (the notes-app PR, and the clinic transfer submission). Intended findings live only in `content/assessment/keys/1.4.md` §Seeded review — intended findings.
