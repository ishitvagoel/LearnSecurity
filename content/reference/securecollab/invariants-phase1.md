# SecureCollab — Phase 1 invariant catalogue

**Owner:** Module 1.1
**State:** design reference, not implementation assurance
**Version:** 1, 2026-08-25

This artifact is the first SecureCollab spiral model. It records the outcomes later phases must preserve and test. No product runtime or milestone evidence exists yet.

## Product scope

Included now:

- tenants, members, and tenant administrators;
- tenant membership;
- text notes;
- privacy-safe security events;
- design-time request, log, export, deletion, retention, and restore horizons.

Deferred and review-triggering:

- files and sharing links;
- support impersonation;
- caches, queues, background workers, and webhooks;
- billing simulation and AI features;
- mobile offline state;
- production capacity, real PII, real payments, and assurance against the cloud administrative plane.

The browser and all client-supplied identifiers, tenant labels, role labels, headers, and timing are untrusted. Each invariant names its narrower trusted base.

## Catalogue summary

| ID | Property | Primary forbidden outcome | Trusted dependency | Residual risk / next owner |
|---|---|---|---|---|
| SC-CONF-01 | Tenant A note bodies must never be returned to Tenant B members through in-scope API, log, or tenant-export paths. | B receives bytes derived from an A note body. | Server policy binds subject/object/action/tenant; event and export schemas are server-controlled. | Direct snapshot administration deferred to data/key lifecycle; alternate paths reopen the row. |
| SC-INTEG-01 | Membership and note records must change only through an authorized transition; denial, failure, or retry leaves no partial forbidden state. | A member or revoked admin mutates membership, or a failed request partially commits. | Current authority and transaction use the same context; operation identity is correctly scoped. | Module 1.2 owns the authority matrix; distributed workflows reopen the transition model. |
| SC-ACCT-01 | Every tenant-admin membership change must produce privacy-safe evidence attributable through the incident/recovery interval. | A high-impact change has no usable decision evidence, or evidence contains protected content. | Event is coupled to the committed decision; access and retention are controlled. | One operator controlling state and the only evidence store remains a concentration of trust. |
| SC-AVAIL-01 | One tenant’s expensive work must not consume all ordinary read capacity for other tenants beyond the stated recovery objective. | B’s work exhausts A’s reads or recovery destroys valid data. | Work accounting and limits bind to the server-resolved tenant. | No production objective or distributed scheduler exists in Phase 1. |
| SC-PRIV-01 | Expired note titles and contact metadata must remain absent from ordinary events and tenant exports after the declared lifecycle transition. | A later export, event, or restore exposes an expired value. | Lifecycle state is enforced on export/event/restore paths. | Backup media outside the modeled restore path is deferred to the data-lifecycle design. |

The executable local fixture expands these rows with attackers, preconditions, candidate mechanisms and limits, four evidence modes, detection/recovery, non-goals, and review triggers. The fixture is a model-quality exercise, not product proof.

## Cross-property dependencies

### Accountability versus privacy

SC-ACCT-01 needs enough event context to reconstruct a membership decision. SC-PRIV-01 prohibits copying note contents, credentials, and unnecessary contact values into ordinary evidence. The design consequence is a versioned event schema with opaque identifiers and policy-decision context rather than arbitrary request serialization.

If investigators later demand more content, both rows must be reviewed; “security logging” cannot silently override the privacy property.

### Availability versus isolation

SC-AVAIL-01 uses tenant-bound work accounting. If the tenant label comes from the client, the mechanism can undermine both availability and authorization: abusive work can be charged to another tenant. The server-resolved authority context must therefore feed the work key. Module 1.2 refines that authority; later worker modules revisit distributed accounting.

### Recovery versus integrity

SC-INTEG-01 requires denied or failed transitions to leave no partial state. Recovery may intentionally write corrective state using privileged authority. That path needs its own subject, action, object, approval, evidence, and idempotency model; an “emergency” label is not authority.

### Deletion versus restore

SC-PRIV-01 cannot end at a successful DELETE response. A restore can reintroduce an expired value. The later data-lifecycle design must state retention and reconciliation behavior; until then, backup media outside the modeled restore path remains residual risk.

## Evidence roadmap

Evidence is deliberately staged.

| Property | Phase 1 evidence | Later executable owner |
|---|---|---|
| SC-CONF-01 | Claim-envelope and semantic-validator evidence | 1.2 authority model, 4.4 tenant-isolation tests, 5.5 persistence/backup, 10.5 evidence operations |
| SC-INTEG-01 | State/time and forbidden-outcome design | 2.4 concurrency/failure, 3.4 business logic, 6.6 workflow/race, 7.4 workers |
| SC-ACCT-01 | Privacy-safe event and failure-behavior specification | 9.1 traceability, 9.3 tests, 10.5 incident evidence |
| SC-AVAIL-01 | Bounded property, attacker, and residual-risk design | 6.7 resource abuse, 7.4 worker accounting, 10.5 recovery |
| SC-PRIV-01 | Purpose/retention/export/restore claim | 5.1 data lifecycle, 5.5 persistence, 8.2 offline state, 10.5 recovery |

Future tests must not be cited as current proof. Each later module updates this table and records actual evidence.

## Review triggers

Reopen the catalogue when any of these changes:

- asset: files, attachments, search indexes, analytics, or AI summaries;
- principal: support, service, worker, guardian, external collaborator, or mobile device;
- authority: delegated action, impersonation, emergency override, or new role;
- boundary: CDN, cache, queue, webhook provider, mobile storage, or backup operator;
- state/time: retries, offline edits, restore, legal hold, longer retention, or deletion semantics;
- harm/objective: real payments, real PII, regulated data, or a production recovery target;
- evidence: new event fields, evidence storage, administrative access, or investigation needs.

A triggered row is not automatically false. Its previous assurance no longer covers the changed assumption until it is revised and re-evaluated.

## Non-goals and honest limits

- This document does not define a complete authority matrix or trust-boundary diagram; Modules 1.2 and 1.3 own those artifacts.
- It does not select production cryptography, hosting, log products, rate limits, or retention periods.
- It does not claim ASVS verification, penetration-test coverage, compliance, or milestone completion.
- It does not protect a public deployment because no public product deployment exists.
- It does not contain real personal data or credentials.

Security in this reference means preserving these bounded outcomes under the recorded model—not accumulating control names.
