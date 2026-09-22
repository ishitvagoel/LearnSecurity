# Required and bridge are two different sets, computed by two different rules

**Kind:** design-exercise
**Loop step:** 4 Build

If a score cannot be the evidence Gate 1 needs (Claim 1), and a credential cannot substitute for the diagnostic's own observation (Claim 2), then the fix for both is not "check more carefully" — it is "stop reading that input in the decision at all." You should be able to predict `quiz_score_grants_phase1_skip`'s fixed body before reading it: a function that never inspects `score` cannot be tricked by any value of `score`, so the fix is `return False`, full stop, with no comparison anywhere in the function body for a later edit to loosen. The same reasoning predicts `tooling_bridge_required`'s fix: read `diagnostic_gap` and nothing else, so that a `job_title`, `vendor_cert`, or `lms_badge` key existing in the same dict has no code path that reaches it.

The vulnerable and fixed versions of `phase1_modules_for_learner` differ by exactly the lines this reasoning predicts, and nothing else:

```python
# vulnerable
required = set(REQUIRED_PHASE1_MODULES)
if quiz_score >= 80 or fast_track:
    required.discard("1.4")

# fixed
required = set(REQUIRED_PHASE1_MODULES)
```

`phase1_modules_for_learner` needs one more step than "stop reading an input," because the defect there is not one bad comparison — it is one set (`required`) that should never move, and one set (`bridge`) that should move only on real evidence, sharing a function body where nothing marks the difference. The structural fix is to stop computing `required` at all: return the constant `set(REQUIRED_PHASE1_MODULES)` directly, so there is no `discard`, no conditional, and no variable whose value depends on `quiz_score` or `fast_track` for that key. `bridge` keeps being computed from `tooling_gaps`, because that is the one input this function is actually supposed to vary on. The fix is not "check the discard condition more carefully before removing 1.4" — any condition guarding a removal of a Phase 1 module is already the bug, however it is spelled.

## Two candidate mechanisms for the credential problem, compared honestly

A competent engineer, told "credentials shouldn't override the diagnostic," might reasonably propose **downgrading a credential's weight instead of removing it** — let a `job_title` or `vendor_cert` count for something, say enough to waive a bridge unit only when combined with a diagnostic score above some lower bar, rather than enough on its own. This is a real, thoughtful attempt, and it fails at a specific point: it still makes the bridge decision partly a function of an unaudited external claim, just with a smaller coefficient. The moment that coefficient is nonzero, a sufficiently persuasive combination of claims — a job title plus a middling score — reaches the same forbidden outcome this module exists to prevent, only now hidden behind arithmetic instead of an obvious `if`. A weighted formula is harder to read as broken than a boolean short-circuit is, which makes it a worse fix, not a more sophisticated one.

The chosen mechanism — read only `diagnostic_gap`, ignore the rest entirely — is a hard line, and the honest place to say where it stops working is at the boundary of what a diagnostic can observe in the first place. If the diagnostic's Git probe genuinely cannot detect a particular kind of fluency (say, comfort with interactive rebase, versus the commands the probe actually runs), a learner who has that fluency and nothing the probe checks for will be assigned a bridge unit they do not need. That is a real cost of the hard line, and this module's answer to it is not "loosen the rule" but "improve the probe" — the fix belongs to whoever maintains the diagnostic's own gap-detection logic, not to `tooling_bridge_required`'s evidence-source rule, which should stay exactly as strict once the probe is better.

A second candidate for the `required`-set problem is **keeping the discard but gating it on an explicit, reviewed allowlist** of learners cleared to skip 1.4 — replacing "any fast score" with "an instructor said yes for this specific person." This is closer to defensible than the credential-weighting idea above, because a person is making the call rather than a threshold, and a reviewed exception is not automatically the same failure as an automatic one. It still fails as a fix for this function's own claim, though, for a narrower reason: `phase1_modules_for_learner` is a diagnostic-placement function, and an instructor's per-learner exception is a different kind of decision, made by a different actor, on a different timeline, than anything this function's arguments can represent — bolting it on here means the exception lives inside the same code path C1 and C3 both forbid credentials and scores from reaching, for the same reason a job title does not belong inside `tooling_bridge_required` either. If a genuine, reviewed exception process is wanted, it belongs outside this function entirely, as its own auditable record — not as a fourth argument this diagnostic learns to special-case.

## Where the framework's default is not the application's guarantee

A dictionary's `.get(key, default)` is a general-purpose tool with no opinion about security; a diagnostic evidence record with a missing `diagnostic_gap` key is a specific situation where the wrong default silently manufactures a claim of safety. `evidence.get("diagnostic_gap")` on a dict with no such key returns `None`, and `bool(None)` is `False` — "bridge not required" — which is exactly backwards for a record that means "no diagnostic ever ran," not "a diagnostic ran and found nothing." Python's dictionary default is doing precisely what it is documented to do; the application-level guarantee this module needs — a missing observation should never resolve to "positively observed, nothing wrong" — is not something `.get()` provides and was never going to provide, because a general-purpose accessor cannot know which missing key means "no result" versus "result was zero" versus "no diagnostic ran at all" in your specific domain. The fixed function states the guarantee explicitly instead of leaning on the accessor's default: `if "diagnostic_gap" not in evidence: return True`, so a missing observation fails toward requiring the bridge, not away from it.

## The transfer this sets up

The same distinction — a general-purpose accessor's default answering "what value should stand in here," and an application needing a specific, stricter answer for a security-relevant case — recurs once you leave this module. [Module 1.2's authority model](../../../1/1.2/lessons/01-property.md) asks you to name, for SecureCollab's own authorization checks, exactly which lookup misses should fail open and which must fail closed; `diagnostic_gap`'s missing-key case is the same question, asked here first at bridge-placement scale, so that when 1.2 asks it again about a real authorization check it is a recognized shape rather than a cold start.
