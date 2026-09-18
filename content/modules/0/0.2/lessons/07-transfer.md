# A clinic's onboarding quiz, and a vendor's certificate

**Kind:** transfer-challenge
**Loop step:** 7 Generalize

Change the authority relation this module's claims were built against, and see which survive. A mid-size clinic-booking company is onboarding a new backend engineer. Their process has two steps that map onto this module's two forbidden outcomes, in a different domain with different stakes: a 92% score on an internal "secure coding basics" quiz, and a signed vendor letter stating the new hire "holds a current cloud-security certification," offered by the hiring manager as grounds to skip the company's own architecture threat-model review before the engineer gets production database access.

## Which claims transfer unchanged, and why

The substitution this section works through, stated compactly before the reasoning behind each line:

```text
SecureCollab: quiz_score_grants_phase1_skip(100)         == False
Clinic:       internal_quiz_grants_review_skip(92)       == False   # same rule, different subject
```

Both functions answer the identical question — does a diagnostic percentage authorize skipping a reviewed artifact — for a different artifact and a different organization. The rest of this section is the argument for why that substitution is legitimate for C1–C3, needs a small adjustment for C4, and what changes and does not change along the way.

**C1** transfers directly: a quiz score, at 92% or any other value, is not evidence that this specific engineer can find the clinic-booking system's actual trust boundaries — patient contact information flowing from the booking form into a shared calendar service, say — any more than a SecureCollab-scoped score is evidence of 1.2's authority map. The evidence-mismatch argument does not depend on which system the quiz was about; it depends only on a percentage being a different kind of measurement from a reviewed, system-specific artifact.

**C2** transfers directly, with the credential swapped for a closer analogue: the vendor's certification letter is exactly the "asserted, not observed" evidence [Claim 2](01-property.md) names, now arriving with a company letterhead instead of an LMS badge. The clinic's own threat-model review is the thing this course calls diagnostic evidence in this context — something the clinic itself must observe about this engineer, on this system — and a cloud-security certification from an unrelated vendor, however real, was never that observation. Accepting it in place of the review commits the identical error `tooling_bridge_required`'s vulnerable file commits: a credential from a different authority, for a different purpose, standing in for this organization's own evidence.

**C3** transfers with a change of subject: SecureCollab's fixed module set was `{"1.2", "1.3", "1.4"}`; the clinic's analogue is whatever set of reviews its own onboarding policy names as non-negotiable — say, the architecture threat-model review and a HIPAA-scoped data-handling walkthrough. The claim's shape survives exactly: no score on an internal quiz, and no unrelated tooling fluency the new hire happens to demonstrate quickly, may shrink that set. If the clinic's onboarding tool has an "experienced hire, fast-track" flag analogous to this module's `fast_track` argument, it is exactly as dangerous here, for exactly the same reason.

## Which claim needs a stated adjustment, and why

**C4** needs a genuine adjustment, because the specific standard changes: this course cites the NICE Secure Systems Development work role as informative vocabulary; the clinic's hiring rubric more plausibly cites a cloud-vendor certification's own stated scope, or a role description from a completely different framework. The underlying rule survives unchanged — vocabulary describing what a job or a credential covers is not equivalent to an organization's own reviewed evidence that this specific person, on this specific system, meets its bar — but naming the exact source correctly matters here exactly as it did in [Claim 4](02-model.md): if you cite the vendor certification's own marketing page as though it defined what the clinic's threat-model review checks, you have made the same category error C4 forbids, just against a different standard.

## What must not happen, stated as this module states it

`quiz_score_grants_phase1_skip(100)` being `True` is this module's forbidden outcome in SecureCollab's terms. The clinic's forbidden outcome is structurally identical, restated in its own terms: a 92% quiz score, or a vendor's certification letter, or the pair of them together, being read as authorization to skip the architecture threat-model review before this engineer gets production database access holding patient contact information. "They're clearly senior, look at the certificate" is not merely an unprofessional shortcut; it is the exact same evidence-source error this module's three lab functions were built to make impossible, transplanted into a hiring decision where the asset at risk is a patient's data rather than a fellow learner's placement record.

## A time-horizon difference worth naming separately

One property of the clinic scenario has no clean analogue in the original module and is worth naming rather than glossing over: a vendor certification carries an expiry date, where a placement quiz score does not meaningfully age in the same way (a score is never evidence regardless of when it was taken, per C1). This might suggest a fourth path around the review — "the certification was current when issued, even if it has since lapsed" — but it fails for the same reason an unexpired one would: C2's objection was never about the credential's currency, only about its source. A certification that is both current and from a recognized vendor still was never the clinic's own observation of this engineer against this system, so its expiry date is irrelevant to whether it should have counted in the first place.

## Success criteria

A complete answer names, for the clinic scenario: which of C1–C4 apply unchanged and which single word or phrase each one's SecureCollab-specific language needs replaced with (the quiz's subject, the credential's source, the required-review set, the cited standard); states the clinic's own forbidden outcome in one sentence, parallel in shape to this module's; and identifies the one architectural difference that raises the stakes without changing which claims apply — that a skipped review here risks a stranger's patient data, not a fellow learner's own placement record, which is a difference in consequence, not in cause. An answer that only asserts "the same rule applies" without doing this substitution, or that treats the vendor certificate as somehow more legitimate than an LMS badge because it has a company's name on it, has not transferred the claim — it has renamed the nouns and left the reasoning exactly where it started, which is the one outcome this exercise is built to make visible rather than reward.

## What this page is not doing

This is a prompt, not a live exercise against a real clinic system or a real vendor's certification portal. Do not contact a certification body to test whether this scenario is realistic, and do not use a real clinic's name or a real engineer's credentials in your answer.
