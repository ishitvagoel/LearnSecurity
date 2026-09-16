# 1.4 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/1.4.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — residual risk vs. a filled-in table

Four statements about SecureCollab's account-recovery confirm step:

**A.** "Residual risk: users should be careful when recovering their account."
**B.** "Residual risk: coercion by a person physically present at the device remains even after the confirm control is made keyboard-operable and named; owned by the product lead for identity; revisit when recovery adds a second factor or a safe-word mechanism."
**C.** "We reduced residual risk by adding a CAPTCHA to the recovery flow."
**D.** "Residual risk is low because our accessibility scanner reports green."

Identify which statement (if any) actually names a residual risk in the sense Lesson 01 and Lesson 02 define it, and explain what is missing from each of the other three.

**Claim assessed:** C1 · **Outcome:** Produce a SecureCollab risk register with assumptions, uncertainty, user-harm, residual risk, and owners

## 2. Diagnosis — the checker's quiet gap

```python
def is_usable_accessible(control: dict) -> bool:
    if control.get("mouse_only"):
        return False
    if not control.get("name"):
        return False
    return True
```

Given the input `{"name": "Confirm", "mouse_only": False}` (no `keyboard` key at all), name the root cause of why this function accepts it, the precondition that must hold for this to matter in practice, and the impact if it ships this way. Give three distinct answers, not one answer restated three times.

**Claim assessed:** C2 · **Outcome:** Treat security friction and inaccessibility as security outcomes

## 3. Diagnosis — reading a "fixed" diff

A pull request changes the vulnerable object to `{"id": "confirm-recovery", "name": "Confirm", "color": "green", "mouse_only": False}` and nothing else. Using the fixed checker's logic from Lesson 04, determine whether this object passes `is_usable_accessible`, and explain your reasoning without running the code first.

**Claim assessed:** C2 · **Outcome:** Treat security friction and inaccessibility as security outcomes

## 4. Diagnosis — friction theater vs. a convenience hole

A team proposes lengthening the recovery-confirm session timeout from 5 minutes to 24 hours, arguing this "reduces friction for legitimate users." Using Lesson 01's two-effort model, name which of the two failure branches (friction theater or convenience hole) this proposal risks, identify the precondition under which it would actually cause harm, and state the impact on the who-is-allowed check specifically.

**Claim assessed:** C3 · **Outcome:** Treat security friction and inaccessibility as security outcomes

## 5. Design — two candidate fixes

Given the vulnerable fixture in `labs/1.4/1.4-risk-register`, two engineers propose fixes: Engineer A sets `mouse_only: False` and stops there; Engineer B adds `keyboard: True` and updates the checker to require it. Under the constraint that the fix must be verifiable by a test that does not depend on which module's factory produced the object under test, choose between the two proposals and defend your choice, including the specific case where your chosen fix still falls short.

**Claim assessed:** C2 · **Outcome:** Treat security friction and inaccessibility as security outcomes

## 6. Design — actors and the support-read-aloud row

Lesson 02's design table denies the row "Support × backup codes × read aloud." A colleague argues this row should be allowed during a declared incident, since the alternative is locking out legitimate users at scale. Under the constraint that any allowed action must be independently auditable after the fact, propose a design that addresses the colleague's operational concern without allowing that specific row, and state what your proposal still leaves as residual risk.

**Claim assessed:** C4, C5 · **Outcome:** Model threat actors by capability and incentive, including human error, coercion, and abuse economics

## 7. Transfer — the clinic and bank sketches

Using the clinic second-factor scenario from `lessons/07-transfer.md`, state which of this module's five claims (C1–C5) survive unchanged when the object being protected changes from a notes account to a patient chart, which claims need a materially different harm statement, and why the coercion residual specifically does not shrink or disappear in the new setting.

**Success criteria:** Your answer must name at least one claim that needs rewording (not merely restating) for the new setting, and must explain the coercion point in terms of physical presence rather than repeating the phrase "coercion remains" without justification.

**Claim assessed:** C1–C5 · **Outcome:** Transfer the register after changed actor capability or a failing accessible recovery flow

## 8. Operate — the deny-line signal

Write the log line your system would emit when a recovery attempt is denied because the confirm control could not be verified as keyboard-operable. State which fields it must carry, which two fields it must never carry, and who receives the resulting alert.

**Claim assessed:** C5 · **Outcome:** Include graceful degradation, detection, and recovery when prevention is not absolute

---

## Evidence checklist

- [ ] Risk register with assumptions, user-harm scenarios, residual risk, and owners (Lesson 02)
- [ ] WCAG-oriented review notes for the recovery-confirm journey specifically, not the whole product
- [ ] Lab `labs/1.4/1.4-risk-register`: forbidden outcome named as **a high-impact recovery control is color- or mouse-only**
- [ ] `vulnerable/` tests show 3 of 6 failing for the stated security reason; `fixed/` tests show 6 of 6 passing
- [ ] Transfer answer (item 7) naming which claims change and which do not
- [ ] Operate signal (item 8) that carries no recovery codes or note bodies
