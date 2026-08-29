# 1.2-LO-07 — Transfer authority reasoning to ReleaseDesk

**Kind:** transfer-challenge
**Loop step:** 7 Generalize
**Gate 1 contribution:** define who may cause a high-impact effect without using a product, role name, or checklist as the definition of authority
**Standards:** Saltzer and Schroeder (1975, seminal); OWASP ASVS 5.0.0 `v5.0.0-8.1.1`, `v5.0.0-8.2.1`, `v5.0.0-8.3.1`, `v5.0.0-8.3.2`, and `v5.0.0-8.3.3` as applicable anchors.

## Which SecureCollab authority claims fail when a machine executes a delayed, approved effect?

Changing “note” to “release” is not transfer. ReleaseDesk changes the object, authority source, state transition, trusted components, time horizon, and impact. You must rebuild the model and explain which earlier reasoning still applies.

Use only the synthetic product card below. Do not inspect or operate a real CI/CD system, cloud account, repository, or deployment.

## Product card: ReleaseDesk

ReleaseDesk coordinates production deployments for a small software company.

- A developer proposes deployment of one immutable artifact digest to one named environment.
- The proposer cannot be the sole approver.
- Two current approvers from the owning service team must approve a production deployment.
- Approval expires after 15 minutes and is bound to artifact digest, environment, service, and requested change ID.
- A CI worker performs the deployment later using a machine identity.
- The worker receives jobs through an at-least-once queue, so duplicate delivery is possible.
- An approval may be revoked, an approver may leave the team, or the artifact may be replaced before execution.
- A break-glass on-call path exists for a declared incident, has a five-minute scope, notifies the service owner, and requires post-use review.
- Production credentials are not exposed to developers or approvers.
- Some approvers use keyboard-only or assistive-technology workflows.
- All data and identities in this exercise are synthetic.

## What materially changed?

Compared with SecureCollab Phase 1, consider at least:

- the effective subject is a CI worker, while authority may originate from proposer and approvers;
- the protected object is a state transition involving an immutable artifact and environment, not a stored note;
- authorization is assembled from multiple independent conditions;
- the effect occurs after approval and may be delivered more than once;
- identity, team membership, artifact, approval, queue, and environment state can change independently;
- denial or delay can affect incident recovery and availability, not only confidentiality;
- machine credentials provide technical ability that must not become ambient product authority;
- an accessible approval and emergency journey is part of whether the policy works.

Do not treat this list as a completed matrix. It identifies dimensions you must resolve.

## Required deliverable

Produce one coherent authority pack.

### 1. Bounded invariant

State who may cause a production deployment of which artifact to which environment, under which approvals, state, and time. Name at least four forbidden effects, including wrong artifact/environment, insufficient or correlated approval, expired/revoked authority, and duplicate execution.

### 2. Subject and authority map

Include proposer, two approvers, service-team membership source, queue, CI worker, deployment environment, break-glass on-call, and evidence owner. Distinguish originating and effective subjects. Identify the smallest trusted behavior of each component.

### 3. Objects, actions, and state machine

Split proposal, approval, artifact digest, job, environment, deployment, emergency grant, and decision evidence where their authority differs. Model at least:

```text
proposed -> approved -> queued -> executing -> completed
       \-> rejected   \-> expired / revoked / cancelled
```

Define which transitions are irreversible, retryable, or idempotent.

### 4. Access matrix and separation argument

Write at least twelve allow/deny cells. Explain why the two approvals are meaningfully independent—or record the shared failure that remains. Show that proposer, approvers, worker, and break-glass subject hold different authority rather than a shared “deploy role.”

### 5. Delegation or capability interpretation

Decide what the queued job represents. Is it a scoped capability, a request that requires current re-authorization, or a reference to server-side approval state? Define authenticity, scope, audience, expiry, replay behavior, revocation, and whether the worker can act beyond it.

### 6. Enforcement inventory

Identify where policy is enforced at proposal, approval, enqueue, execution, retry, cancellation, and emergency use. Explain why checking only when the job is created is or is not sufficient.

### 7. Four-mode evidence and operations

Specify normal, negative, abuse, and failure tests, including artifact substitution, duplicate delivery, expiry, approver revocation, unavailable policy/evidence, and emergency use. Add privacy-safe decision events, containment, recovery, accessible approval/revocation, and one operator or infrastructure residual risk.

### 8. Comparison memo

Use three headings:

- **Reasoning that transfers:** identify structural ideas such as hostile clients, positive authority, fail-safe unknowns, or enforcement coverage and explain why they remain valid.
- **SecureCollab claims that fail:** name at least four original subjects, objects, states, time assumptions, or effects that cannot be copied and why.
- **New conflicts and limits:** explain at least one security-versus-availability or safety conflict, one common-mechanism risk, and one mechanism that supports a property while creating another risk.

## Constraints

- Do not answer “use RBAC,” “use signed tokens,” “require MFA,” or “use a policy engine” as the authority model.
- Do not assume a valid signature proves that the current action remains authorized.
- Do not count one person, account, device, or identity event twice as independent approval without justification.
- Do not let the CI worker’s production credential define product permission.
- Do not probe a real repository, CI provider, cloud service, or deployment.
- Do not copy SecureCollab tenant names into the solution.
- Do not open the examiner key before evaluation.

## Success criteria

A **competent** pack is internally consistent, testable, safe, and explicit about defaults, authority sources, state, time, and enforcement. A **transfer-ready** pack also:

- explains at least four SecureCollab assumptions that fail rather than only renaming them;
- discovers a non-obvious stale-authority, replay, or common-mechanism failure;
- distinguishes machine ability from originating authority;
- defends or rejects the independence of the approval conditions;
- narrows a universal revocation or “exactly once” claim after modeling failure;
- provides usable emergency and recovery paths without turning break-glass into global ambient authority;
- states which ASVS requirements apply and which advanced references are only design anchors.

Completion of the prompt does not itself mark Gate 1 transfer-ready. The isolated examiner rubric determines whether the evidence is satisfactory.
