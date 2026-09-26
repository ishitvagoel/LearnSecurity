# 3.1 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/3.1.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, mechanism, or false assurance

Four statements a reviewer might find in a design document for SecureCollab's note-logging feature:

**A.** "We labeled the note body field `Confidential` in our data classification spreadsheet."
**B.** "`log_event`'s `_redact` function denies any field whose classification level is not in the calling sink's own `SINK_POLICY` entry, and defaults an unrecognized field to the most restrictive level."
**C.** "Our logging vendor is SOC 2 certified, so anything in our logs is handled appropriately."
**D.** "We added a code comment above `log_event` noting that the note body must never be logged."

Sort each statement into **rule**, **mechanism**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Given a field and a candidate sink, decide allow or deny for that field-sink pair and name the classification level and the check that produced the decision.

## 2. Discrimination — which asset was left off the inventory

Four inventory entries a teammate proposes for SecureCollab's Phase 2 assets:

**A.** "Note body: Confidential. Must not appear in the application log or the error dump."
**B.** "Note id: Internal. May appear in the application log."
**C.** "Company id: Internal. May appear in the application log."
**D.** "Session token: not listed — it isn't data the user typed, so it doesn't belong in a data classification table."

Identify which entry is the actual defect in this inventory (not a defect in any single sink's behavior — a defect in the inventory itself), and explain, using this module's own reasoning about what possessing a value grants versus what a value's content reveals, why the session token has to be classified at least as sensitively as the note body rather than left off the table.

**Claim assessed:** C2 · **Outcome:** Identify every authority artifact an inventory limited to content fields would omit, and justify classifying each at least as sensitively as the content it gates.

## 3. Diagnosis — a default that looks safe

```python
def _redact(context: dict, sink: str) -> dict:
    allowed_levels = SINK_POLICY[sink]
    out = {}
    for key, value in context.items():
        level = CLASSIFICATION.get(key, "internal")
        out[key] = value if level in allowed_levels else f"[redacted-{level}]"
    return out
```

This is not `fixed/app.py`'s `_redact` — it is a different implementation, differing in exactly one default value. Give it a context containing a field named `draft_billing_note` that is not present anywhere in `CLASSIFICATION`, being logged to the `application_log` sink (whose `SINK_POLICY` entry is `{"internal"}`). Name the root cause of why this field reaches the rendered log line, the precondition under which the gap matters in practice, and the impact if this version ships — as three distinct answers, not one answer restated three times.

**Claim assessed:** C4 · **Outcome:** Given a newly added, unclassified field, predict how each existing sink treats it by default and explain why that default is a decision already made, not a delay.

## 4. Diagnosis — a sink that bypasses the mechanism entirely

```python
def write_audit_export(context: dict) -> None:
    """Full audit trail for the compliance team's retention system."""
    _AUDIT_EXPORTS.append(dict(context))
```

This function exists alongside a correctly-implemented `_redact` and `log_event` elsewhere in the same file. Explain, as three distinct answers, the root cause of why this function fails this module's property even though `_redact` itself is correct, the precondition for this function to be reached with a Confidential field present, and the impact on whoever can read `_AUDIT_EXPORTS`. Then state, in one sentence, why C1's claim — worded as a per-sink rule rather than a per-field promise — predicts that a correct `_redact` elsewhere in the file guarantees nothing about this function.

**Claim assessed:** C1, C5 · **Outcome:** Design a detection signal and a purge/rotation response for a redaction miss, and explain why a fix at one call site does not cover a second, independently-reached sink.

## 5. Design — two candidate fixes under a stated constraint

Recall this module's two candidate fixes: (A) strip `note_body` and `session_token` at each handler before calling `log_event`, versus (B) a default-deny, table-driven allow-list inside `log_event` itself. Under the constraint that SecureCollab's engineering team plans to add three new endpoints that log request context over the next quarter, each written by a different engineer who has not read this module's lessons, argue for one candidate over the other. Your argument must name specifically what happens under this constraint for the candidate you reject — not merely assert that it is worse in general.

**Claim assessed:** C1, C3 · **Outcome:** Given a field and a candidate sink, decide allow or deny for that field-sink pair and name the classification level and the check that produced the decision.

## 6. Design — a widened sink policy with no visible decision

A pull request adds `"audit_export": {"internal", "confidential"}` to `SINK_POLICY`, alongside a new `write_audit_export` function, in a PR titled "fix: fully redact audit logs." Determine whether adding this policy entry is, by itself, a defect — distinguish this question from whether `write_audit_export` correctly uses `_redact` (a separate question item 4 already covers) — and state what this module's claim about requirements (not levels) says must accompany a policy change like this one before it ships, regardless of whether the widening turns out to be operationally justified.

**Claim assessed:** C3 · **Outcome:** Write a requirements-backlog entry for a classified field naming the sink, the allow/deny decision, and the failure behavior when a field's status is unknown, and explain why a level alone is insufficient.

## 7. Transfer — the clinic booking card

Using the clinic scenario from `lessons/07-transfer.md`, a teammate proposes: "Chart text and appointment time are both patient data, so let's just classify the whole booking-card record as Confidential and be done with it." State which of this module's claims this proposal violates, name the specific operational cost of the proposal that the teammate has not accounted for, and explain — using this module's own vocabulary of classification level versus sink policy versus requirement — what the teammate's proposal gets backwards about the relationship between a field and a record.

**Success criteria:** Your answer must identify that classifying at the *record* level rather than the *field* level collapses two fields with different, legitimate sink requirements into one level, which either over-restricts the appointment time (denying it from sinks that have a genuine, documented need for Internal-level scheduling data) or, if the team then quietly treats "Confidential" as loosely enforced to avoid that cost, under-restricts the chart text instead. It must name C1 (a per-field, per-sink rule, not a whole-record label) as the claim this proposal violates most directly.

**Claim assessed:** C1, C3 · **Outcome:** Given a newly added, unclassified field, predict how each existing sink treats it by default and explain why that default is a decision already made, not a delay.

## 8. Operate — two signals, two thresholds

Write the two distinct `log_redaction_miss` lines SecureCollab's fixture would emit for: (a) a Confidential field denied by the `application_log` sink's policy, and (b) the same field denied by the `error_dump` sink's policy. Then explain why a sustained-rate alert threshold tuned for sink (a) might reasonably need a different rate than one tuned for sink (b), given how often each sink fires under ordinary, non-incident traffic — and name the operational cost of setting both thresholds identically low.

**Claim assessed:** C5 · **Outcome:** Design a detection signal and a purge/rotation response for a redaction miss, and explain why a fix at one call site does not cover a second, independently-reached sink.

---

## Evidence checklist

- [ ] Data inventory, classification table, and security-requirements backlog (Lesson 02) naming every field this module's lab fixture uses, including the session token as an authority artifact
- [ ] Local reproduction of the module's forbidden outcomes (Lesson 03): the note body and the session token both reaching the application log, and the session token reaching the error dump
- [ ] Lab `labs/3.1/3.1-lab`: `vulnerable/` tests show 7 of 9 failing for the stated security reasons; `fixed/` tests show 9 of 9 passing
- [ ] Transfer answer (item 7) correctly rejecting whole-record classification and naming C1 as the claim it violates
- [ ] Operate signals (item 8) for both sinks, neither carrying the denied value itself
