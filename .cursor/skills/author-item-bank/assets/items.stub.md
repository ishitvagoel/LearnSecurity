# <id> assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/<id>.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — <short title>

<Four candidate statements. Identify which states a property and which name mechanisms, and justify.>

**Claim assessed:** C<n> · **Outcome:** <outcome text>

## 2. Discrimination — <short title>

## 3. Diagnosis — <short title>

```<language>
<8–20 lines of code or configuration>
```

Name the root cause, the preconditions that must hold for it to be reachable, and the impact — as three distinct answers, not one restated.

## 4. Diagnosis — <short title>

## 5. Design — <short title>

<Two mechanisms, one stated constraint. Choose and defend the trade-off, including where your choice stops working.>

## 6. Transfer — <short title>

<The scenario from `lessons/07-transfer.md`. State which original claims survive the changed assumption, which break, and why.>

**Success criteria:** <what a competent answer must contain — not a step-by-step scaffold>

## 7. Operate — <short title>

<Write the signal, its fields, the field you deliberately omit and why, the recipient, and the recovery step.>

---

## Evidence checklist

- [ ] <module-specific artifact>
- [ ] Lab `labs/<id>/<id>-lab`: forbidden outcome **<name it>**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass, in a clean environment
- [ ] Transfer answer with the changed assumption named
