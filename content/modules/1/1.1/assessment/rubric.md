# Module 1.1 assessment — learner evidence and rubric

This is learner-facing. Examiner examples and intended seeded findings are isolated outside the site.

## Required evidence pack

Submit one coherent pack containing:

1. a scoped SecureCollab Phase 1 product model;
2. at least five invariant rows with complete claim envelopes;
3. peer-review classifications and resulting revisions;
4. a causal review of the vulnerable SECURITY.md;
5. the vulnerable-fail and fixed-pass lab commands and results;
6. one property-derived mechanism design record with alternatives and proof obligations;
7. a normal/negative/abuse/failure evidence matrix;
8. one privacy-safe operate section;
9. four actionable seeded-review comments;
10. the CivicClinic transfer catalogue and comparison memo if seeking transfer-ready.

Do not include real targets, PII, credentials, or public-system observations.

## Critical rubric

No compensating average is used. A developing result on any critical row makes the module result developing.

| Dimension | Developing | Competent | Transfer-ready evidence |
|---|---|---|---|
| Property and scope | Topic, CIA label, tool, or universal claim | At least five bounded SecureCollab invariants name assets, subject/action, forbidden outcome, non-goals, and scope | CivicClinic claims are independently bounded rather than copied |
| Attacker, trust, state, and time | “Malicious user” or “backend trusted” | Capabilities, smallest trusted base, untrusted client inputs, state, and time constrain every important row | Changed delegation, vendors, shared devices, scarcity, and recovery invalidate specific original assumptions |
| Causal reasoning | Controls or symptoms are listed | Root cause, preconditions, impact, prevention, detection, and recovery are distinct; mechanism limits are concrete | Learner compares alternatives and predicts a non-obvious secondary property conflict |
| Evidence | Happy path, status, configuration, or scanner only | Normal, negative, abuse, and failure cases have property oracles and residual gaps | Transfer evidence changes with the new authority, boundary, state, or time model |
| Lab interpretation | Any failure is called success, or passing validator is called implementation proof | Vulnerable fails and fixed passes for the intended semantic/safety reason; validator limits are stated | Learner demonstrates and explains an important semantic limitation of the validator safely |
| Operations and human factors | Prevention only; secrets or note contents proposed in logs | Privacy-safe event, signal, failure behavior, containment, root-cause repair, recovery validation, communication, and residual operator risk | Human recovery and accessibility constraints change the operational claim in the transfer case |
| Communication and editorial integrity | Vague “more detail” comments or reviewer stamp as proof | At least four actionable comments identify unsupported conclusion, missing model, consequence, minimum change, and evidence | Comparison memo clearly explains which SecureCollab claims fail and why |

## Supporting dimensions

These cannot repair a critical failure, but must still be satisfactory:

- standards are cited with version/status and used within their stated role;
- non-goals and residual risk are honest rather than universal;
- review triggers correspond to assumption changes;
- the answer remains within local synthetic scope;
- the pack is structured so a second reviewer can trace outcome to explanation, design, evidence, and operation.

## Retryable knowledge check

Answer without naming a product as the property:

1. Why can a password hash support one bounded property while proving nothing about note authorization?
2. What does a time horizon add to a confidentiality claim?
3. Give one example of mechanism evidence and one example of property evidence.
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

Do not “fix” the vulnerable fixture in place.

## Self-review before submission

For every invariant, ask:

- Can another person construct a concrete counterexample?
- Is it inside the stated attacker, channel, state, and time?
- Does the evidence observe the property rather than a control label?
- Does the mechanism have a named bypass or limit?
- If prevention fails, is any useful and privacy-safe outcome preserved?
- Which product change forces the row to be rewritten?

## Mastery states

- **Not-attempted:** no evidence pack.
- **Developing:** one or more critical dimensions are incomplete or mechanism-led.
- **Competent:** all critical and supporting dimensions are satisfactory for SecureCollab.
- **Transfer-ready:** competent plus satisfactory independent CivicClinic evidence and comparison memo.

This module contributes to Gate 1; it does not complete Gate 1 by itself.
