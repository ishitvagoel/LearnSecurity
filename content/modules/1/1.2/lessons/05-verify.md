# 1.2-LO-05 — Turn authority cells and lifecycle changes into evidence

**Kind:** verification-lab
**Loop step:** 5 Verify
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.1.1`, `v5.0.0-8.1.2`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.2.3`, `v5.0.0-8.3.1`, `v5.0.0-8.3.2`, and `v5.0.0-8.4.1`; Saltzer and Schroeder complete mediation and fail-safe defaults (1975, seminal).

## What observation would falsify each authority cell?

An authorization test needs a property oracle. “The `authorize` function was called” is a mechanism observation. “Bob receives no Tenant A note body and no partial state is committed through any in-scope path” is a property observation.

Start from the matrix cell, not from a test framework:

```text
subject × action × object × state/time -> expected decision and effect
```

For an allow cell, observe the intended effect and evidence. For a deny cell, observe both the denial and the absence of partial release or mutation. A status code alone may hide a leaked body, a committed write, an enqueued job, or an over-detailed event.

## Build tests from equivalence classes, not usernames

Alice and Bob are examples of authority classes.

- active same-tenant member;
- active cross-tenant member;
- inactive or revoked former member;
- scoped same-tenant administrator;
- administrator of another tenant;
- unauthenticated or unknown subject;
- subject with a valid bounded grant;
- subject with expired, revoked, wrong-audience, or overbroad delegation;
- service or worker with and without originating authority.

Objects and actions also have classes:

- same-tenant and cross-tenant object;
- existing, missing, deleted, or restricted object;
- summary field versus body field;
- read, list, update, delete, grant, revoke, export, and unknown action;
- direct, aggregate, administrative, background, retry, cache, and restore path.

A Cartesian product of every class may be too large. Select cases using the invariant, impact, implementation shape, and review triggers. Document what you did not cover.

## Four evidence modes

### Normal

Show that a positively authorized action succeeds with the intended projection and state. In the lab, Alice reads Tenant A’s note; Admin A deletes an A note; the modeled export decision succeeds with the documented distinct current approvals.

Normal evidence prevents “deny everyone” from masquerading as secure authorization.

### Negative

Use a clearly forbidden cell: Bob reads an A note, Admin A deletes a B note, a revoked member reads, one approval attempts a two-person action, or an unknown action is requested. Assert no protected output and no partial mutation.

### Abuse

Vary inputs and paths within the authorized local model:

- choose every object ID, not one convenient sample;
- use client-supplied tenant labels that conflict with stored state;
- repeat one approver ID;
- attempt list/aggregate release instead of only direct read;
- reorder grant, revoke, and use;
- try an action string not known to policy.

Abuse evidence tests whether the rule follows authority rather than expected UI behavior.

### Failure

Challenge dependencies and time:

- membership or policy lookup is unavailable;
- object lookup returns unknown state;
- authority changes after authentication;
- approval expires before execution;
- evidence emission fails;
- a cached decision is older than the accepted revocation window;
- a restore reintroduces old membership or grant records.

For this module’s scoped policy, unknown policy state denies. The product may need a usable failure message and operational path so people do not create an unsafe workaround.

## Trace the lab suite to the matrix

The local suite should include at least these shapes:

| Cell or transition | Property oracle | Vulnerable expectation | Fixed expectation |
|---|---|---|---|
| active A member × read × A note | intended body returned | pass | pass |
| active B member × read × A note | no A body returned | fail | pass |
| active A member × list × note collection | no B object returned | fail | pass |
| Admin A × delete × B note | B note unchanged / operation denied | fail | pass |
| revoked A member × read × A note | no body returned | fail | pass |
| one current approver × export A | decision denies | fail | pass |
| two distinct current A approvers × export A | decision allows | pass only if other policy facts hold | pass |
| any subject × unknown action | decision denies | fail | pass |

The expected vulnerable run is non-zero because selected forbidden outcomes occur. Do not mark a lab successful merely because “some test failed.” Record the test names and why the failures match the authority model.

## Assert effects, not just decisions

A policy-unit test can show that `decide(...)` returns deny. An integration test must show that the operation cannot bypass the result.

For a read:

- no protected fields are returned;
- no unauthorized cache entry, export, event, or derived output is created;
- the denial event contains only approved metadata;
- object state remains unchanged.

For a mutation:

- before/after protected state is identical on denial;
- no job or side effect was scheduled;
- transaction failure does not leave a partial change;
- retry does not convert a denial into a duplicate or allowed action.

The local fixture models selected service effects only. Later modules add HTTP, database, transaction, cache, and worker evidence.

## Use a counterfactual

For every critical rule, ask:

> If the enforcement were removed or weakened, would this test fail for the intended reason?

Temporarily replacing tenant comparison with `True`, treating inactive memberships as active, or changing unknown-action default to allow should make a relevant test fail. If the suite stays green, it may not exercise the policy path. If every test mocks the policy to return expected decisions, it has mocked away the property.

Mutation is diagnostic, not proof of completeness. A suite can kill selected policy mutations while an unmodeled route bypasses the policy entirely.

## Measure enforcement coverage separately from policy coverage

Two forms of completeness are needed:

1. **Policy coverage:** matrix cells, states, grants, and failure modes have oracles.
2. **Enforcement coverage:** every path capable of the protected effect consumes the relevant current decision.

Create an enforcement table:

| Effect | Path | Policy test | Operation test | Failure test | Owner / gap |
|---|---|---|---|---|---|

Do not infer enforcement coverage from a central library’s unit-test percentage. Route registration, query review, architecture constraints, database policies, and negative integration tests may all contribute evidence. None alone is universal proof.

## Delegation and revocation test sequence

When grants enter scope, test a sequence rather than isolated snapshots:

```text
issuer authorized
-> grant issued with narrow action/object/expiry
-> correct grantee uses it
-> wrong grantee/action/object is denied
-> grant revoked or issuer authority changes
-> later use is denied within the stated window
-> evidence identifies grant and policy versions without exposing secrets
```

Also test duplicate delivery, replay, clock disagreement, and unavailable revocation state according to the mechanism’s model. If the grant is a bearer capability, adjust the subject oracle: possession may intentionally be the grant, but scope, authenticity, time, and revocation still need evidence.

## Guided practice

Extend the SecureCollab matrix with a restricted-note body that requires an explicit reviewer grant while ordinary members may list its title.

Produce:

1. one normal body-read case;
2. two negative cases differing in subject or grant;
3. one abuse case using list or projection rather than direct read;
4. one failure case for unavailable or stale grant state;
5. the property oracle for each;
6. one policy-removal counterfactual;
7. one residual gap.

Your work is satisfactory when the title/body distinction, trusted attribute sources, denial side effects, grant lifecycle, and alternate path are observable. “Returns 403” is not enough.

## Independent practice

Without using the names Alice, Bob, note, or tenant, write four-mode evidence for a delegated action in another synthetic product. State which assumption changed and why a SecureCollab test cannot simply be renamed.

## Transfer

A release is approved at 10:00, the artifact changes at 10:03, the CI worker executes at 10:05, and an approver is revoked at 10:04. Which object was approved—the mutable branch, commit, artifact digest, or deployment request? Which time controls authority? LO-07 asks you to build tests that answer rather than assume.
