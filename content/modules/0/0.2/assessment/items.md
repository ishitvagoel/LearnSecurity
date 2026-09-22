# 0.2 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/0.2.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find describing a placement-diagnostic change:

**A.** "`quiz_score_grants_phase1_skip` has no comparison against `score` anywhere in its body; it returns `False` unconditionally."
**B.** "We only show a 'you might be ready to skip ahead' banner above a 90% score, and a skip still requires a separate manager approval click."
**C.** "Our LMS already tracks completion percentage for this module, so Gate 1 is effectively tracked too."
**D.** "We added a check that denies the skip specifically when `score == 100`, but scores below that still fall through to the old logic."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Refuse a diagnostic score, at any value, as authorization to skip modules 1.2, 1.3, 1.4, or Gate 1's evidence review

## 2. Discrimination — property vs. mechanism for tooling-bridge evidence

Four statements offered as grounds for skipping a Git bridge unit:

**A.** "The diagnostic itself ran a Git probe against this learner and recorded `diagnostic_gap: False`."
**B.** "The learner's resume lists five years of professional Git use."
**C.** "A vendor-issued certification states the learner passed a Git proficiency exam last year."
**D.** "The learner's manager vouches for their Git skill in a private message to the instructor."

Identify which statement states the property this module calls C2, and rank the other three by how close each comes to being real evidence for it.

**Claim assessed:** C2 · **Outcome:** Grant a tooling-bridge skip only on the diagnostic's own observed gap evidence, never on a job title, vendor certification, or LMS badge claim

## 3. Diagnosis — a third implementation's gap

```python
def tooling_bridge_required(evidence: dict) -> bool:
    if evidence.get("diagnostic_gap") is not None:
        return bool(evidence["diagnostic_gap"])
    if evidence.get("vendor_cert"):
        return False
    return True
```

This is not `vulnerable/diagnostic.py`, and it is not `fixed/diagnostic.py` — it is a third implementation, written by someone who believed they had removed the credential problem by only letting `vendor_cert` matter "when the diagnostic didn't run at all." Give it `evidence = {"vendor_cert": True}` — no `diagnostic_gap` key present. Name the root cause of why this function waives the bridge for this input, the precondition under which the gap matters in practice, and the impact if it ships this way — as three distinct answers, not one answer restated three times.

**Claim assessed:** C2 · **Outcome:** Grant a tooling-bridge skip only on the diagnostic's own observed gap evidence, never on a job title, vendor certification, or LMS badge claim

## 4. Diagnosis — reading a candidate fix

A teammate proposes this fix, reasoning that requiring *both* a high score and the fast-track flag together is safer than either alone:

```python
def phase1_modules_for_learner(quiz_score, tooling_gaps=None, fast_track=False):
    gaps = tooling_gaps or {}
    required = {"1.2", "1.3", "1.4"}
    if fast_track and quiz_score >= 90:
        required.discard("1.4")
    bridge = {name for name, gap in gaps.items() if gap}
    return {"required": required, "bridge": bridge}
```

Determine, without running any code, whether this fix's `required` set contains `"1.4"` for a call with `quiz_score=95, fast_track=True`, and explain your reasoning by tracing that exact input through this exact function.

**Claim assessed:** C3 · **Outcome:** Keep modules 1.2, 1.3, and 1.4 in every learner's required path regardless of score, fast-track flag, or bridge assignment

## 5. Design — staleness vs. a different authority, under a constraint

A diagnostic team wants to let a contractor who was diagnosed recently skip a redundant Git bridge unit without re-running the probe every time. Two proposals: **Option A** accepts a diagnostic result from up to 30 days ago as still valid evidence. **Option B** accepts a signed note from a different course's instructor who directly observed the same skill in a prior session. Under the constraint that the decision must remain traceable back to an observation *this diagnostic* made, choose between the two options and defend your choice, including where your chosen option stops working.

**Claim assessed:** C2 · **Outcome:** Grant a tooling-bridge skip only on the diagnostic's own observed gap evidence, never on a job title, vendor certification, or LMS badge claim

## 6. Design — a label under a constraint

Two proposals for what a learner's placement summary should display next to a completed Git bridge unit. **Option A** shows the specific diagnosed gap and the date it was observed ("Git branching: diagnosed gap, closed 2026-09-02"). **Option B** shows "Meets NICE Secure Systems Development work role" as a single completion label. Under the constraint that the label must not claim more than the diagnostic actually evidenced, choose between the two options and state exactly what Option B would need to add, or remove, to become acceptable.

**Claim assessed:** C4 · **Outcome:** Treat the NICE Secure Systems Development work role as informative placement vocabulary, not as Gate 1 evidence or a substitute syllabus

## 7. Transfer — the clinic's onboarding quiz and the vendor certificate

Using the clinic scenario from `lessons/07-transfer.md`, state which of this module's claims (C1–C4) apply to the clinic's hiring process unchanged, which one needs its cited standard swapped for a different one and why, and state the clinic's own forbidden outcome in one sentence, parallel in shape to this module's.

**Success criteria:** Your answer must state C1–C3 as applying with only the subject-matter nouns changed (the quiz's topic, the required-review set), must identify C4 as needing its standard reference swapped (the NICE work role for whatever credential or role description the clinic's own hiring rubric cites) while the underlying rule is unchanged, and must state the clinic's forbidden outcome as: a quiz score or a vendor certification being read as authorization to skip the architecture threat-model review before production database access holding patient contact information is granted.

**Claim assessed:** C1–C4 · **Outcome:** Transfer this module's claims to a clinic's hiring diagnostic and a vendor certification

## 8. Operate — the skip-denial signal

Write the `phase1_skip_denied` log line your system would emit for a credential-based skip attempt (a `job_title` claim on a learner with no genuine diagnosed gap), including every field this module's operate lesson names as necessary. State which field you deliberately omit and why, who should receive the signal, and the threshold at which a series of these signals becomes worth investigating rather than routine.

**Claim assessed:** C5 · **Outcome:** Record a denied skip attempt without leaking the diagnostic's item text, answer content, or a badge image, and without back-dating Gate 1

---

## Evidence checklist

- [ ] Evidence-source table (Lesson 02) distinguishing observed diagnostic evidence from asserted credential claims
- [ ] Lab `labs/0.2/0.2-bridge`: forbidden outcomes named as **a quiz score granting a Phase 1 skip**, **a credential overriding real diagnostic evidence**, and **a score or flag dropping module 1.4 from the required set**
- [ ] `vulnerable/` tests show 8 of 15 failing for the stated reasons; `fixed/` tests show 15 of 15 passing
- [ ] Seeded review (Lesson 08) completed via the four-question checklist, including the one non-issue line — do not open the key first
- [ ] Transfer answer (item 7) naming which claim needs its standard reference swapped
- [ ] Operate signal (item 8) that carries no quiz item text, answer content, or badge image
