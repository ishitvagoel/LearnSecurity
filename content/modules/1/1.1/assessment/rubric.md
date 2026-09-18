# Module 1.1 assessment — learner evidence and rubric

This is learner-facing. Examiner examples, intended findings, and banding examples stay closed, in the examiner key under content assessment keys, and are never linked from this page.

## Required evidence pack

Submit one coherent pack containing:

1. a scoped SecureCollab Phase 1 product model (assets, minimum adversaries, trusted computing base) for this stage;
2. at least five catalogue rows with complete claim envelopes, each a distinct, system-specific claim rather than a generic claim repeated under five identifiers;
3. peer-review classifications and the resulting revisions;
4. a causal review of the vulnerable `SECURITY.md` and `security_claim.yaml`, following the reading order in [08-code-review.md](../lessons/08-code-review.md);
5. the vulnerable-fail and fixed-pass lab commands and their exact results;
6. one property-derived catalogue row built up from `01-property-vs-mechanism.md` through `04-smallest-mechanism.md`, with mechanism limits and proof obligations stated;
7. a normal/negative/abuse/failure evidence matrix for at least one row, with each mode observing the forbidden outcome rather than a control's presence;
8. one privacy-safe operate section (signal, threshold, containment, recovery, residual risk);
9. answers to `content/modules/1/1.1/assessment/items.md` #1–8;
10. the CivicClinic transfer catalogue and comparison memo if seeking transfer-ready evidence.

Do not include real targets, real PII, real credentials, or observations of a public system.

## Critical rubric

No compensating average is used. A developing result on any critical row makes the module result developing.

| Dimension | Developing | Competent | Transfer-ready evidence |
|---|---|---|---|
| Property and scope | Topic, CIA label, tool, or universal claim | At least five bounded, distinct SecureCollab rows name assets, subject/action, forbidden outcome, and non-goals | CivicClinic claims are independently bounded rather than copied, per item 7 |
| Distinctness | Rows are field-complete but generic or near-identical to each other | Every row's property and forbidden outcome is specific enough that it would not validate against an unrelated product | Learner can construct and explain a padded-duplicate counterexample (item 2) |
| Attacker, trust, state, and time | "Malicious user" or "the server is trusted" | Capabilities, the smallest trusted component, untrusted inputs, state, and time constrain every important row | Changed delegation, shared devices, scarce capacity, and revocation timing invalidate specific original assumptions (item 7) |
| Causal reasoning | Controls or symptoms are listed | Root cause, preconditions, impact, prevention, detection, and recovery are distinct; mechanism limits are concrete (item 4) | Learner compares alternatives (item 6) and predicts a non-obvious secondary property conflict |
| Evidence | Happy path, status, configuration, or scanner only | Normal, negative, abuse, and failure cases have property oracles, and a mode's content actually matches its label (item 3) | Transfer evidence changes with the new authority, boundary, state, or time model |
| Lab interpretation | Any failure is called success, or a passing validator is called implementation proof | Vulnerable fails and fixed passes for the intended semantic/safety reason; validator limits are stated | Learner demonstrates and explains a real semantic limitation of the validator safely (e.g., what it still cannot verify) |
| Operations and human factors | Prevention only; secrets or note contents proposed in logs | Privacy-safe event, signal, threshold with a stated false-positive cost, containment, recovery validation, and residual operator risk (item 8) | Human recovery and accessibility constraints change the operational claim in the transfer case |
| Communication and editorial integrity | Vague "more detail" comments, or a reviewer stamp treated as proof | At least four actionable comments identify an unsupported conclusion, missing model element, consequence, and minimum change; a plausible non-issue is correctly not reported as a finding | Comparison memo clearly explains which SecureCollab claims fail for CivicClinic and why |

## Supporting dimensions

These cannot repair a critical failure, but must still be satisfactory:

- standards are cited with version and status and used within their stated role;
- non-goals and leftover risk are honest rather than universal;
- review triggers correspond to assumption changes;
- the answer remains within local synthetic scope;
- the pack is structured so a second reviewer can trace outcome to explanation, design, evidence, and operation.

## Retryable knowledge check

Answer without naming a product as the property:

1. Why can a password hash support one bounded property while proving nothing about note authorization?
2. What does a time horizon add to a confidentiality claim?
3. Give one example of control-presence evidence and one example of forbidden-outcome evidence.
4. Why can accountability and privacy conflict?
5. What must be re-evaluated when a browser action moves to a background worker?

A knowledge score of 80% may be retried. It does not override practical critical gaps.

## Lab evidence format

Record:

- environment and Python version;
- exact vulnerable command and non-zero result;
- the intended semantic/scope errors, separated from environment errors;
- exact fixed command and zero result;
- one validator limitation.

Do not "fix" the vulnerable practice files in place.

## Self-review before submission

For every row, ask:

- Can another person construct a concrete counterexample?
- Is it inside the stated attacker, channel, state, and time?
- Does the evidence observe the forbidden outcome rather than a control label?
- Would this row still say something specific if every SecureCollab proper noun were deleted from it?
- If prevention fails, is any useful and privacy-safe outcome preserved?
- Which product change forces the row to be rewritten?

## Mastery states

- **Not finished:** no evidence pack.
- **Developing:** one or more critical dimensions are incomplete or mechanism-led.
- **Competent:** all critical and supporting dimensions are satisfactory for SecureCollab.
- **Transfer-ready:** competent plus satisfactory independent CivicClinic evidence and comparison memo.

This module contributes to Gate 1; it does not complete Gate 1 by itself.
