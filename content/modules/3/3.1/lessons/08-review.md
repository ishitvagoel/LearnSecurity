# Seeded review: a classification table nobody wired up

**Kind:** code-review
**Loop step:** Review

## What you are reviewing, and in what order

Open [`labs/3.1/3.1-lab/review/candidate_fix.py`](../../../../../labs/3.1/3.1-lab/review/candidate_fix.py). A teammate describes it as: "Added an audit-export sink for the compliance team's retention system, reusing our existing classification setup." Do not read this file top to bottom the way you would read a tutorial. Read it in the order this module's property actually resolves, because that order is what a skim misses and a careful review catches.

Start at the classification table and the sink policy — `CLASSIFICATION` and `SINK_POLICY` — and ask what each one *claims* a field or a sink is allowed to do. Then find every function that actually renders a field toward a sink, and for each one, ask whether it consults those two tables before rendering, or merely sits near code that does. This is the same question [`lessons/01-property.md`](01-property.md) asked about `vulnerable/app.py`'s own decorative `CLASSIFICATION` table: a table's presence in the file proves nothing about which functions read it. Only after tracing every rendering function should you look at the call sites — `note_read_handler`, here — because a call site can only be as correct as the functions it calls, and reviewing the call site first tends to anchor a reviewer on "does this call look reasonable" rather than "does the function it calls actually enforce anything."

## What to name as three distinct things, not one

For whatever you find wrong in this file, write three separate answers rather than one answer restated three times: the **root cause** (which specific line or omission produces the failure), the **precondition** (what has to be true elsewhere in the system for that line to matter — is it reached at all, and under what input), and the **impact** (what a party who exploits or merely benefits from the gap actually gains). A finding that says "this function doesn't redact properly" states none of the three. The function in question:

```python
def write_audit_export(context: dict) -> None:
    """Full audit trail for the compliance team's retention system."""
    _AUDIT_EXPORTS.append(dict(context))
```

reads, in isolation, like a plausible logging helper — it looks like it does something, because it does append something, to something. It still fails this module's property completely: `dict(context)` copies every field exactly as it arrived, with no call to `_redact` anywhere in the function, so whatever the caller handed it — including a note body or a session token — reaches `_AUDIT_EXPORTS` unchanged. A finding that says "`write_audit_export` appends `dict(context)` directly, without calling `_redact`; it is reached whenever `note_read_handler` is called with `note_id` equal to `"note_a"` or `"note_b"`; and a party who can read `_AUDIT_EXPORTS` — the compliance team, and anyone with the same access as them — receives the unredacted note body and session token for those two notes" states all three, separately, and a reader who has not seen the code can still evaluate whether the claim is correct.

## Reading the classification table's own claims skeptically

`SINK_POLICY`'s entry for `audit_export` allows both `"internal"` and `"confidential"` — a real widening of what that sink may carry, compared to the two existing sinks, which allow only `"internal"`. [`lessons/04-build.md`](04-build.md) derived that a sink's permitted levels have to reflect a real, documented operational need, decided deliberately — not whatever a single pull request's author found convenient while building an unrelated feature. Ask whether this PR's description names any such decision, or whether the policy entry simply appeared alongside the feature it enables, with no separate sign-off visible anywhere in the diff. A widened sink policy is not automatically wrong — a compliance export may genuinely need to carry Confidential fields — but it is a decision this module's own claims require to be named and owned, and a PR that both makes the decision and ships the feature that depends on it, in the same breath, has skipped the naming step even if the widening turns out to be the right call.

## A default that looks harmless because nothing currently triggers it

`_redact`'s signature changed from taking `sink` as a required argument to `sink: str = "application_log"`. Every call site in this file still passes `sink` explicitly, so as this diff stands, the default never actually fires — no current caller can accidentally get the wrong sink's policy applied. This is worth naming precisely because it is the kind of change a reviewer trained to be suspicious of default arguments will flag on instinct, and it is worth resisting that instinct here specifically: a finding that calls this the primary problem, without also naming that it currently has zero live effect, has produced a *plausible-sounding* finding rather than a *correct* one, and would spend review attention on a change with no current impact while two changes with clear, present impact sit nearby. Note the default for later — a genuine future risk exists if a new call site is added that omits `sink` by mistake — but naming it as equivalent in severity to the audit-export bypass misreads what each change currently does.

## What "close the finding" has to mean here

A finding on this file is not closed by a comment promising a follow-up PR, by rewording `write_audit_export`'s docstring to sound more careful, or by adding a code comment that says "TODO: redact this." [`lessons/05-verify.md`](05-verify.md) already established what actually counts as evidence: a test that exercises the fixed code path and fails on the unfixed one. A finding on this fixture is closed only when a corresponding assertion — in the shape of this module's own lab tests — passes against the corrected function and would have failed against the version you are reviewing now.

## Common misreadings this exercise is designed to catch

A reviewer who treats "there's a classification table" as evidence the PR handles classification correctly has made the exact mistake [`lessons/01-property.md`](01-property.md) opened with. A reviewer who treats the widened `audit_export` policy as automatically wrong, without asking whether a genuine documented need could justify it, has confused "undocumented" with "incorrect" — the finding is that the decision is unnamed, not that widening a policy is inherently a defect. A reviewer who spends their primary attention on the `_redact` default-argument change, because it looks like the kind of thing security reviews are supposed to catch, has let a stylistically suspicious change crowd out two changes with an immediate, traceable impact.

## What this lesson is not doing

Findings, their rationales, and which of this file's changes are genuine defects versus the deliberate non-issue live only in `content/assessment/keys/3.1.md`, not on this page. Do not import or execute `candidate_fix.py`; it is a reading fixture, not a runnable component, and it is not wired into this module's pytest suite.
