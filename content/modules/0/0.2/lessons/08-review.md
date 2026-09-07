# Would you merge this quiz-as-skip?

**Kind:** code-review
**Loop step:** Review
**Standards:** NICE as vocabulary. Gate 1 evidence rules.

## Review the practice files as if they were the course placement service

Review `labs/0.2/0.2-bridge/vulnerable/` as a pull request for a course tool. Check whether `quiz_score_grants_phase1_skip(100)` still returns true.

## Picture: if score >= 80: skip part 1

**`if score >= 80: skip_phase(1)`**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"score 100 skips 1.2"| Property["A rule - good if tested"]
  Q -->|LMS percentage| Mechanism[A tool - a number]
  Q -->|job title mapped| False[False assurance]
```

A part-1 skip still has to be denied. Without an always-false skip, a 100 score still walks into part 1.

## Problems to find (name them yourself)

- `if score >= 80: skip_phase(1)`
- No link from diagnostic to 1.2 evidence
- Badge screenshot as check-in 1
- Adaptive path hides 1.4 accessibility leftover

Also reject: live LMS attacks; keys in lessons; claiming check-in 0 or check-in 1; “they’re a senior hire”; treating a Git-bridge skip as a 1.2 skip.

## Common mix-ups

- Placement is a security clearance
- Fast learners skip rules
- Tool fluency is threat modeling
- A job-title competency is a 1.2 allow cell
- An LMS percentage is industry-list coverage

## Use it somewhere new

A clinic change that “added an onboarding quiz and a job-title mapping” without keeping 1.2 required is a skipped-check review. Name the independent falsehood that would still keep score 100 from skipping isolation labs.

## What this page is not doing

Do not ship a quiz-as-skip because a comment says advanced learners may skip. Nobody owns that leftover. Do not attack an LMS to prove the finding.
