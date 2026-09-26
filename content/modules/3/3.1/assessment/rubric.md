# 3.1 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another.

## Module

Assets, data classification, and security requirements — five teaching claims (C1–C5), named in `spec.md` §Teaching claims: a per-sink classification rule, authority-artifact inventory completeness, requirement derivation from a classification level, the fail-safe default for unclassified fields, and prevention paired with detection and recovery.

## Evidence checklist

- [ ] Data inventory, classification table, and security-requirements backlog (Lesson 02) naming every field this module's lab fixture uses — including the session token, classified as an authority artifact at least as sensitively as the note body — with a per-sink allow/deny and failure behavior for each
- [ ] Local reproduction of the module's forbidden outcomes (Lesson 03): the note body and the session token both reaching the application log, and the session token reaching a second, independently-reached error-dump sink
- [ ] Lab `labs/3.1/3.1-lab`: `vulnerable/` tests show 7 of 9 failing for the stated security reasons; `fixed/` tests show 9 of 9 passing
- [ ] Assessment items (`content/modules/3/3.1/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Operate signals (Lesson 06) for a redaction miss on both sinks, neither carrying a note body or session token, with a stated alert threshold and its false-positive cost
- [ ] Transfer task (Lesson 07) applying the same field-level, per-sink classification rule to a clinic booking card, correctly rejecting whole-record classification and naming which claim it violates
- [ ] Seeded review (Lesson 08) correctly locating the audit-export bypass in `labs/3.1/3.1-lab/review/candidate_fix.py` and correctly declining to treat the harmless default-argument change as an equivalent-severity finding

## Rubric

| Result | Meaning |
|---|---|
| Developing | Names classification as a spreadsheet label or a compliance document; treats "we have a classification table somewhere in the code" as equivalent to "this sink enforces it"; missing forbidden-outcome lab evidence for the note body or the session token |
| Competent | All five claims stated as system-specific properties of SecureCollab's assets, not tool names or generic data-handling slogans; every lab forbidden outcome reproduced and mapped to the claim it tests; the session token correctly classified at least as sensitively as the note body, with a stated reason tied to what possessing it grants |
| Transfer-ready | Lesson 07's transfer task completed, correctly distinguishing which of C1–C5 transfer unchanged to the clinic scenario and which (C5) requires new information about a retention obligation before it can be answered, without Top 10/CWE/compliance-checklist language standing in for the derivation |

Knowledge check (retryable, 80% threshold): the eight module-specific items in `content/modules/3/3.1/assessment/items.md`.

## Seeded review

Use the local `labs/3.1/3.1-lab/review/candidate_fix.py` artifact via Lesson 08's reading order. Intended findings and banding live only in `content/assessment/keys/3.1.md`.
