# 1.2-LO-08 — Review an authority change for hidden ambient paths

**Kind:** code-review
**Loop step:** 5 Verify and communicate
**Fixture:** `labs/1.2/1.2-authority-matrix/vulnerable/authority.py` and `vulnerable/SECURITY.md`
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.1.1`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.3.1`, and `v5.0.0-8.4.1`.

## Does the change preserve the matrix across every effect and authority state?

Treat the vulnerable fixture as a pull request proposing reusable authorization logic. Your task is not to count suspicious lines. Reconstruct the authority relation the code actually implements, compare it with the module invariant, and write changes a developer can verify.

Do not open `content/assessment/keys/1.2.md` until your review has been evaluated.

## Review boundary

Review only the local synthetic fixture. Do not translate the code into requests against a live application. No exploit payload or public target is needed; each counterexample is an in-process subject–action–object decision.

## 1. Reconstruct the implemented cells

For each public operation in the file, record:

| Operation/effect | Subject source | Object source | Action | Authority source | State/time | Default | Protected effect |
|---|---|---|---|---|---|---|---|

Do not accept function names as proof. A function called `authorize` may still trust an unscoped role, ignore current membership, or allow unknown actions.

## 2. Trace every attribute to its trust source

Ask:

- Is the subject authenticated, and is current membership separately resolved?
- Is tenant scope obtained from stored relationships or from caller-controlled input?
- Is object ownership resolved before the effect?
- Does role expansion preserve tenant, action, object, and state?
- Are approvers distinct, current, correctly scoped, and bound to this action?
- Is time evaluated at use rather than assumed from issue time?
- Does an absent rule, missing object, or policy error deny?

Write the actual answer from code. Do not repair missing information in your head.

## 3. Separate policy coverage from enforcement coverage

Compare direct read, aggregate list, delete, revocation, export approval, and unknown-action behavior. A correct branch in one operation does not mediate another.

For each path, identify:

- the policy decision point;
- the enforcement point;
- whether release or mutation occurs before the decision;
- whether the operation can use ambient process or role authority;
- which test observes the protected effect;
- which future path would invalidate the conclusion.

## 4. Review state and time

Authentication may outlive membership. Approval may outlive role, object, policy, or time window. Ask what happens when:

- a member is revoked after login;
- an admin changes tenant or role;
- an approval is duplicated;
- an object changes between decision and effect;
- a decision is cached;
- the policy cannot classify a new action.

If the code has no time or version model, record the limitation rather than claiming revocation behavior.

## 5. Write actionable comments

Each comment must include:

1. the unsupported allow or false assurance;
2. the exact missing or untrusted model element;
3. the forbidden effect and impact;
4. the minimum structural change;
5. the normal/negative/abuse/failure evidence that would evaluate it;
6. the remaining limit or review trigger.

Avoid “add an auth check.” Prefer a comment shaped like: “This operation expands a role without preserving the object’s authority domain. Resolve the current scoped membership and stored object domain at the trusted decision point, deny mismatch/unknown state, enforce before mutation, and add same-domain allow plus cross-domain, revoked, and policy-failure tests.”

## Required review output

Submit:

- the implemented-cell table for every public operation;
- at least six actionable comments across at least four distinct failure classes;
- one authority-map correction;
- one proposed bounded policy rule;
- one enforcement-inventory gap;
- one privacy-safe decision event;
- one revocation or stale-authority finding;
- one residual risk the fixed local fixture cannot remove;
- a short standards note mapping applicable exact ASVS IDs without claiming whole-module compliance.

## Review quality check

Your review remains developing if it only says “IDOR,” “broken access control,” “use RBAC,” “add middleware,” or “follow ASVS.” Those labels may communicate categories, but they do not state subject, object, action, authority source, trusted attributes, state/time, enforcement, or evidence.

## Transfer review

Review this sentence from a different design:

> The CI worker has a valid production credential and the job is signed, so the deployment is authorized.

Write one review comment that distinguishes machine ability, message authenticity, originating authority, approved artifact/environment, approval state, expiry/revocation, replay, enforcement time, evidence, and residual risk. Do not prescribe a vendor.
