# A denial that leaks the thing it denies is not a fix

**Kind:** operations-exercise
**Loop step:** 6 Operate

Fixing `quiz_score_grants_phase1_skip`, `tooling_bridge_required`, and `phase1_modules_for_learner` stops a bad decision from being made once. It does not, by itself, give anyone a way to notice a "fast-track seniors" branch being added back six months from now, by someone who never read this module. That is what an operational signal is for, and Claim 5 exists because the obvious way to build one — log enough to prove the deny fired — is also the easiest way to reopen the confidentiality problem this course keeps separate elsewhere: quiz items and their answer keys.

## Designing the signal: what it needs, and the field it must not have

`phase1_skip_denied` needs three fields to be useful to an auditor six months later: the learner id the decision was about, the module id that was requested — so a cohort export can group how many people tried to skip [1.4 Risk, people, economics, usable security, and resilience](../../../1/1.4/lessons/01-property.md) specifically from how many tried [1.2 Authority and protection](../../../1/1.2/lessons/01-property.md) — and a timestamp. It should also carry which of this module's three functions fired — a score-based attempt, a credential-based attempt, or a required-set-shrink attempt — because those three failure classes have different likely causes and different people to talk to about preventing a recurrence.

A complete line for one credential-based attempt looks like this:

```text
phase1_skip_denied learner_id=dev-1 module_requested=1.4 basis=credential timestamp=2026-09-18T14:02:00Z
```

`basis=credential` is what lets a later cohort export separate this attempt from a score-based one without opening a single ticket by hand. The field it must never carry is the content that made the attempt look plausible: the quiz's item text, the specific answer given, or an image of the badge or certificate a manager attached. Logging "learner X attempted a skip with score 100" is a governance record. Logging "learner X attempted a skip with score 100, having answered 'the OWASP Top 10 defines the syllabus' to item 7" pastes the quiz's own content — the exact material `assessment-items.mdc` keeps out of learner-facing files — into a ticketing system that was never scoped to hold it, for no evidentiary gain: the deny fired or it did not, and the item text does not change which answer is correct. A signal built to prove a denial happened does not need the denial's raw inputs any more than a bank's fraud alert needs to quote the stolen card's full number to prove a transaction was blocked.

## Threshold, false-positive cost, and who receives it

`phase1_skip_denied` firing once for a given learner is not itself an incident — a hurried learner clicking "skip" and being told no is the system working, not an attack. The signal earns attention at a different threshold: a spike across many learners in a short window, which suggests either a UI bug inviting people to try (a skip button that should not exist yet does) or a cohort being coached to attempt it by someone outside the course. That distinction is exactly why the "which function fired" field from the previous section matters operationally: a spike concentrated in credential-based attempts points at a hiring process leaning on this course's diagnostic in a way it should not, while a spike in score-based attempts points at the UI itself. The receiving audience is whoever owns the cohort export and the diagnostic's own configuration — not the learner's manager, and not a public dashboard, both of which would turn a governance signal into a performance one.

## Containment, revocation, and recovery

Nothing in this module needs "revocation" in the sense a session or a credential does — there is no state to invalidate, because the fixed functions never granted the skip in the first place. What this module's recovery step guards against is different: back-dating. If an audit later discovers that a learner's cohort export shows Gate 1 as passed on a date the actual 1.2–1.4 evidence review had not yet happened, the recovery is to correct the record to the true review date, not to leave the earlier date standing because changing it looks like an admission. A back-dated Gate 1 is worse than an honestly-late one, because the later date is evidence someone can check against a reviewer's actual notes, and the earlier one is not.

## The accessible path this signal feeds

If a future diagnostic UI ever shows a learner or an instructor which modules are required versus bridged, that display inherits [Claim 1](01-property.md)'s and this lesson's Standards line's accessibility constraint directly: a required-versus-skipped indicator that is color-only fails WCAG 2.2's Success Criterion 1.4.1 the same way a green dashboard tile does elsewhere in this course, and an instructor reviewing a `phase1_skip_denied` spike who cannot operate that UI without a mouse has the same friction problem [1.4 Risk, people, economics, usable security, and resilience](../../../1/1.4/lessons/01-property.md) names for a learner-facing recovery flow — the roles are reversed, but the requirement is not.

## What happens when nobody reads the alert

A signal nobody reads is not a control; it is a line in a file that makes the team feel covered without covering anyone. If `phase1_skip_denied` fires and no one is watching the cohort export, the practical outcome is identical to the vulnerable fixture never having been fixed: a learner or a hiring manager who tries enough combinations eventually finds one that is not blocked by this module's functions but by an unrelated, unreviewed process gap — a manual override left enabled, a second diagnostic instance that never got the fix deployed. Naming this residual honestly matters more than promising it away: an alerting pipeline this module's fixture does not build is not a claim this spec makes, and a future Tier-2 lab with a real audit store is where that pipeline's own tests would belong.

## Practice

Draft one `phase1_skip_denied` log line for a score-based attempt and one for a credential-based attempt, using the three fields this lesson names plus the fourth (which function fired). Then check each draft against the one rule this lesson insists on: could you delete the item-text or credential-image field from your draft and lose nothing an auditor needs? If deleting it changes what the line proves, the line was built around the wrong evidence.
