# 1.2-LO-06 — Grant, observe, expire, revoke, and recover authority

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** Saltzer and Schroeder psychological acceptability, separation of privilege, least privilege, and compromise recording (1975, seminal); OWASP ASVS 5.0.0 `v5.0.0-8.3.2` and `v5.0.0-8.3.3` as advanced review anchors.

## Can the system explain and remove authority when the original assumption changes?

Authorization is not a request-time boolean. Authority has a lifecycle:

```text
requested -> reviewed -> granted -> active -> used
                                   |       |
                                   v       v
                               expired / revoked
                                   |
                                   v
                           recovered and reviewed
```

The secure property must survive mistakes, revocation, evidence loss, emergency action, and human stress. Prevention matters, but an invisible or irreversible authorization failure leaves the product unable to contain or learn from compromise.

## Make grants reviewable before activation

An administrative grant screen should show the effect a reviewer is authorizing:

- grantee’s stable identity and relevant tenant or organization;
- exact actions;
- object or object-set scope;
- start and expiry;
- delegation and onward-delegation rules;
- high-impact consequences;
- who requested and who approved;
- whether approval is independent;
- revocation method and expected effect time;
- evidence and notification behavior.

“Make Cara admin” hides too much. Does it allow reading every note body, changing membership, exporting data, deleting the tenant, viewing audit evidence, creating new admins, or using emergency paths? A role can simplify common decisions, but the UI must make high-impact expansion understandable.

Secure defaults matter here: new objects, roles, tenants, and integrations should begin with the narrow documented authority. The curriculum snapshot treats this as consistent with CISA Secure by Design guidance, but the canonical page was unavailable during the 2026-08-25 recheck; the pin is marked unverified rather than pretending a live confirmation.

## Record decisions without copying protected content

A useful authority event can include:

- event schema and policy version;
- originating and effective subject IDs;
- tenant or authority domain;
- action and object identifier or safe class;
- grant, role, or delegation version;
- decision and stable reason code;
- enforcement point;
- trustworthy timestamp and correlation ID;
- whether the decision was fresh, cached, emergency, or delegated.

It should normally exclude:

- note bodies and restricted fields;
- passwords, session cookies, bearer capabilities, tokens, or authorization headers;
- raw request bodies and arbitrary exception context;
- unnecessary email, phone, or display-name data;
- secret approval material.

The evidence itself becomes a protected object. Who may read, export, modify, or delete it? How long is it kept? Which operator can change both product state and the only record of that change? Those are authority questions, not merely logging configuration.

## Turn events into signals

“Log denied access” is not a detection design. Name a pattern and the uncertainty it represents.

| Signal | Why it matters | Possible legitimate cause | Response boundary |
|---|---|---|---|
| one subject requests many cross-tenant objects | enumeration or confused tenant context | stale client links or support investigation | validate identity/context, contain session if warranted |
| admin action targets a different tenant | unscoped ambient role or client attribute confusion | test fixture or migration tool | block effect, inspect enforcement point |
| revoked authority continues to produce allows | stale cache/token/grant or failed invalidation | documented bounded delay | compare against objective; disable affected high-impact path if exceeded |
| two-person action uses duplicate/correlated approval | separation is cosmetic | small team or emergency | require alternate approved path or record risk decision |
| unknown-policy decisions occur | deployment mismatch or new path | staged rollout | deny effect and alert owner; do not silently default allow |
| authority events disappear while mutations continue | evidence path failure or suppression | telemetry outage | invoke documented fail-closed or durable-evidence behavior |

Thresholds and windows are product hypotheses. A single confirmed cross-tenant success is different from repeated denied probes. Avoid universal alert numbers; record false positives, false negatives, and which effects warrant immediate containment.

## Define revocation as an outcome with a clock

“Role removed” is an administrative action. The security outcome is that the removed authority stops producing protected effects within a stated interval across every relevant representation.

Inventory copies of authority:

- server-side membership and role state;
- sessions and security context;
- self-contained tokens or claims;
- policy caches;
- capability links or delegation records;
- queued jobs and approvals;
- offline device state;
- database roles or temporary credentials;
- restored backups.

For each, define invalidation or expiry, maximum stale window, high-impact exceptions, evidence, and failure behavior. If disclosure occurs during the stale window, later revocation cannot retrieve the information. State that mechanism limit honestly.

ASVS `v5.0.0-8.3.2` treats immediate application of authorization changes as the goal and describes mitigation where immediate change is impossible. Use the exact requirement only where applicable; do not turn it into a claim that every token system has solved revocation.

## Design break-glass authority as a separate path

Emergency access is not `if emergency: allow`. A defensible break-glass design may require:

- declared incident or recovery purpose;
- narrowly scoped action and object set;
- short lifetime;
- independent approval or a justified exception when unavailable;
- strong, usable identity evidence appropriate to the risk;
- clear warning and completion state;
- separate, durable evidence and owner notification;
- automatic expiry and explicit post-use review;
- tests for unavailable approver, evidence failure, and accidental repeat.

The path may deliberately trade confidentiality or least privilege for safety or availability. Record the owner, conditions, residual harm, and recovery. “Emergency” does not erase the invariant; it defines a different bounded policy state.

## Preserve the originating subject through intermediaries

A worker, support agent, or service may be the effective subject that executes the operation. Operations evidence should preserve both:

- **originating subject:** who requested, approved, or delegated the effect;
- **effective subject:** which service or person actually performed it.

If a worker’s ambient service credential becomes the only authority, every job may inherit broad storage access. The product must decide whether execution uses the originator’s current authority, a frozen scoped grant, or independent service authority. Each has different revocation, replay, availability, and audit consequences.

## Human factors are enforcement dependencies

An authority system fails when legitimate administrators cannot understand or complete the secure path.

Avoid:

- color-only allowed/denied indicators;
- permission names without effect descriptions;
- mouse-only scope selection or revocation;
- approval dialogs that hide tenant, object set, duration, or environment;
- silent success that encourages repeated high-impact actions;
- inaccessible recovery that drives credential sharing;
- alarms with no safe next action.

Provide keyboard and assistive-technology operation, text labels, a reviewable summary before commitment, explicit completion and failure states, safe cancellation, and a recovery alternative. Psychological acceptability does not mean reducing every control; it means making the correct secure action fit the user’s mental model and operational reality.

## Response and recovery sequence

For suspected over-authority:

1. **Validate the signal:** confirm decision, policy, grant, and enforcement versions without opening protected content unnecessarily.
2. **Contain narrowly:** revoke the implicated session, membership, grant, worker, approval, or path; do not disable every tenant by reflex.
3. **Preserve evidence:** protect decision and state-transition records with independent access control and retention.
4. **Scope effects:** enumerate direct, aggregate, admin, cache, worker, retry, export, and restore paths that share the rule.
5. **Repair the root cause:** correct policy meaning, attribute source, enforcement coverage, or authority lifecycle—not only the observed user.
6. **Recover state:** remove unauthorized grants or outputs, restore intended data, rebuild caches, and reconcile queued work.
7. **Validate:** rerun normal, negative, abuse, failure, and counterfactual evidence.
8. **Communicate:** tell affected owners what is known, uncertain, contained, and required next.
9. **Revise:** update matrix, review triggers, tests, runbook, and standards traceability.

Recovery is not complete because an account was disabled. The bounded authority property must be re-established across affected paths and state.

## Operations practice

Write a two-page runbook fragment for either membership revocation or the illustrative bulk-export authority. Include:

- grant/use/revocation event fields and prohibited fields;
- one signal, threshold/window rationale, and likely false positive;
- maximum effect time across every authority representation in scope;
- containment owner and blast radius;
- evidence-pipeline failure behavior;
- root-cause repair and recovery validation;
- break-glass behavior and post-use review;
- one accessible administrative path and safe failure alternative;
- one operator-compromise or common-mechanism residual risk.

Peer-check it under a scenario where the only approver is unavailable and the policy store is degraded. If the runbook’s answer is “temporarily give everyone admin,” revise it.

## Transfer

In ReleaseDesk, an approver may be revoked after approving but before the CI worker executes. Decide whether the approval is a historical fact that remains valid for a bound artifact and short window, or whether current approver authority is re-evaluated at execution. State the safety, availability, and incident-recovery trade-off; do not hide it in token expiry.
