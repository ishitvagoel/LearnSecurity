# Module 1.2 assessment — learner evidence and rubric

This file is learner-facing. It contains prompts and evaluation criteria, not answers or seeded findings. Examiner anchors are isolated outside the learning site.

## Required evidence pack

Submit one coherent pack containing:

1. a scoped SecureCollab Phase 1 authority map;
2. an access matrix with at least twelve explicit allow/deny cells and no implicit defaults;
3. an enforcement inventory covering direct read, aggregate list, administrative mutation, revocation, unknown policy, and the modeled high-impact export decision;
4. a delegation record with issuer, grantee, action/object scope, constraints, time, revocation, evidence, and mechanism limits;
5. a causal diagnosis of every intended vulnerable-lab failure before comparison with the fixed tree;
6. exact vulnerable and fixed lab commands/results plus a matrix-to-test trace;
7. one policy-decision and enforcement-point design record with trusted attribute sources, rejected alternatives, failure behavior, and residual risk;
8. a four-mode authority test matrix and at least one policy-removal counterfactual;
9. an authority-lifecycle runbook covering grant, use, expiry, revocation, break-glass, evidence failure, recovery, and accessible administration;
10. the LO-08 seeded review deliverables;
11. a ReleaseDesk transfer pack and SecureCollab comparison memo.

Use only local synthetic course material. Do not include real credentials, real personal data, public-target instructions, or evidence from a system you are not authorized to test.

## Knowledge check — retryable at 80%

Answer each in two to five precise sentences.

1. Why can authentication be correct while authorization is wrong? Give a SecureCollab example.
2. What does an access matrix represent, and how do a role and an ACL relate to it?
3. Why is a random note identifier not automatically a capability?
4. What makes authority ambient? Name one application and one worker or infrastructure example.
5. Why does a central policy function not prove complete mediation?
6. What must delegation preserve or narrow at issue time and at use time?
7. Why are two clicks or duplicate approver IDs not separation of privilege?
8. What is the difference between policy coverage and enforcement coverage?
9. Why can revocation of a role fail to revoke authority?
10. Which conclusion may be supported by passing `v5.0.0-8.4.1` evidence, and which broader conclusions remain unsupported?

Revise missed answers before resubmission. The knowledge result cannot compensate for missing practical evidence.

## Authority-map and matrix task

Model only the current SecureCollab Phase 1 design. Explicitly mark files, sharing links, support impersonation, workers, caches, queues, webhooks, mobile offline state, production deployment, and cloud administrators as deferred review triggers.

Your matrix must include:

- active same-tenant and cross-tenant members;
- a revoked former member whose identity may still authenticate;
- a tenant-scoped administrator acting inside and outside that tenant;
- note summary and body as distinct fields;
- list, read, delete, membership, unknown, and modeled bulk-export actions;
- at least one high-impact action with justified independent conditions;
- positive authority source, state/time, decision, forbidden effect, and test name for every cell.

Add an enforcement inventory. A future gap may be marked out of scope, but it may not be silently labeled protected.

## Lab break/fix task

Run from the repository root:

```text
python -m pytest labs/1.2/1.2-authority-matrix/tests --impl vulnerable

python -m pytest labs/1.2/1.2-authority-matrix/tests --impl fixed
```

For every vulnerable failure, submit:

- matrix cell or lifecycle transition;
- required property;
- root cause and preconditions;
- trigger and impact;
- structural prevention and enforcement point;
- privacy-safe detection and bounded recovery;
- fixed test oracle;
- one remaining lab limitation.

Do not receive credit for “the vulnerable run is red and fixed is green” without causal explanation. Environment or import failures are not intended lab evidence.

## Build/design task

Choose note-body read, membership revoke, or the modeled bulk export. Produce a small implementation patch in a temporary learner copy or a detailed design record containing:

- a positive policy rule and fail-safe unknown behavior;
- current trusted sources for subject, object, action, state, grant, and time;
- explicit policy decision and enforcement points;
- role or delegation expansion that preserves tenant/action/object scope;
- revocation and policy-unavailable behavior;
- two plausible rejected repairs and why they do not restore the property;
- normal, negative, abuse, failure, and counterfactual evidence;
- operations, human-factor limits, residual risk, and review triggers.

Do not edit the course’s vulnerable or fixed directories in place.

## Verification task

Create a table with columns:

| Authority cell / transition | Initial state | Attacker or failure capability | Path | Oracle | Normal | Negative | Abuse | Failure | Counterfactual | Residual gap |
|---|---|---|---|---|---|---|---|---|---|---|

At least one row must distinguish summary from body, one must exercise revoked/stale authority, one must challenge an alternate path, one must validate genuinely distinct approval, and one must test policy or evidence failure. Explain which cases are executable now and which belong to named later modules.

## Operations task

Write a runbook for membership revocation or the modeled export authority. Include:

- privacy-safe decision fields and prohibited fields;
- grant, use, denial, expiry, revocation, and emergency evidence;
- signal with window/threshold rationale and false-positive risk;
- maximum revocation-effect interval for every authority copy in scope;
- evidence-pipeline failure behavior;
- narrow containment, root-cause repair, state/output recovery, retest, and communication;
- one keyboard/assistive-technology path, clear completion state, and safe failure alternative;
- one operator-compromise or shared-mechanism residual risk.

## Seeded code review

Review:

- `labs/1.2/1.2-authority-matrix/vulnerable/authority.py`
- `labs/1.2/1.2-authority-matrix/vulnerable/SECURITY.md`

Submit the implemented-cell table and at least six actionable comments across four distinct failure classes. Each comment must identify the unsupported allow, missing or untrusted model element, forbidden effect, minimum structural change, evidence, and residual limit. Include one exact ASVS mapping note. Do not open the examiner key first.

## Transfer task — ReleaseDesk

Complete LO-07’s synthetic release-approval pack. It must include:

- bounded production-deployment invariant and at least four forbidden effects;
- originating/effective subjects, objects, state machine, authority sources, and trusted components;
- at least twelve access-matrix cells;
- two-person approval independence argument;
- interpretation of the queued job as capability, re-authorization request, or reference to server-side authority;
- enforcement points from proposal through execution/retry/emergency use;
- normal, negative, abuse, and failure evidence;
- privacy-safe operations and accessible recovery;
- comparison memo explaining at least four SecureCollab assumptions that fail.

The transfer may not target or use a real repository, CI provider, cloud account, or deployment.

## Non-compensating rubric

Each critical dimension is evaluated independently.

| Dimension | Developing | Competent | Transfer-ready evidence | Critical |
|---|---|---|---|---|
| Bounded authority property | “Only admins” or tool/role slogan | Subject, action, object, grant, state/time, default, and forbidden effect are explicit | Claim is correctly revised after changed machine/time assumptions | yes |
| Authority model | Actors or roles listed without executable cells | Matrix, authority sources, trusted attributes, delegation, and state are reviewable | Model predicts a non-obvious stale, replay, or common-mechanism failure | yes |
| Causal diagnosis | Names IDOR/BOLA or missing check | Separates root cause, preconditions, trigger, impact, prevention, detection, and recovery across intended failures | Compares plausible fixes and predicts new failure paths | yes |
| Structural policy and enforcement | Adds denylist, hidden UI, middleware, or library call | Positive current server-resolved policy is enforced before every in-scope effect | Originating/effective authority and delayed execution are defended | yes |
| Delegation and separation | Scope/time/revocation absent; duplicate conditions accepted | Authority attenuates; approvers are distinct/current/scoped; failure is defined | Independence and common failure are critically defended in ReleaseDesk | yes |
| Verification | Happy path or status only | Normal, negative, abuse, failure, state/effect, and counterfactual oracles | Evidence covers delayed, replayed, revoked, and intermediary execution | yes |
| Safe lab interpretation | Green/red output without cause, or unsafe target | Exact local results and limits are recorded; no external target/data | Learner identifies an assurance gap not caught by the suite | yes |
| Operations and human factors | “Log and revoke”; sensitive evidence or unusable admin | Privacy-safe evidence, bounded revocation, containment/recovery, accessible journey | Break-glass and evidence common-mode failure are handled honestly | yes |
| Standards accuracy | Unversioned ASVS or checklist-as-proof | Exact v5.0.0 IDs, levels/applicability, and CISA unverified pin are represented accurately | Requirements are tailored to the changed system with explicit non-applicability | yes |
| Review communication | “Needs auth” or generic best practice | Actionable comments tie policy gaps to effects, changes, tests, and limits | Review reconstructs a changed authority model and challenges assumptions | no |
| Transfer | SecureCollab nouns renamed | ReleaseDesk changes actors, object, authority, state, time, and enforcement | Explains at least four failed assumptions and a non-obvious conflict | yes |
| Safety and editorial integrity | Real target/data or examiner content included | Local synthetic scope and isolated key boundary are preserved | Learner independently identifies and communicates safety/assurance limits | yes |

## Result rules

- **Not attempted:** required evidence is absent.
- **Developing:** any critical dimension is incomplete or unsafe.
- **Competent:** every critical dimension is satisfactory for SecureCollab and material findings are corrected.
- **Transfer-ready:** competent evidence plus a satisfactory ReleaseDesk transfer and explicit limitation analysis.

There is no compensating average. A polished transfer essay cannot compensate for a cross-tenant allow cell, default-allow unknown action, stale revocation, cosmetic approval, unsafe scope, or missing enforcement point. This module contributes evidence to Gate 1; it does not mark Gate 1 complete by itself.
