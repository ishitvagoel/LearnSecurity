# 1.1-LO-02 — Build SecureCollab’s first invariant catalogue

**Kind:** design-exercise  
**Loop step:** 2 Model

## Product card: only model what exists

SecureCollab Phase 1 is a design sketch, not a production service. It has tenants, members, tenant administrators, notes, membership, and security-relevant events. Files, external sharing, webhooks, billing simulation, support impersonation, background workers, and offline mobile state arrive later.

That boundary matters. A useful catalogue is versioned against a product model. It does not pretend that future assets are already protected.

### Actors and capabilities

Use at least these actors:

| Actor | Capability for this exercise | Trust position |
|---|---|---|
| Unauthenticated internet client | Sends arbitrary public requests and identifiers | Untrusted |
| Tenant A member | Uses legitimate A credentials and fully controls the browser/request | Client untrusted; identity evidence conditionally trusted |
| Tenant B member | Same capability for B and actively probes cross-tenant identifiers | Untrusted adversarial principal |
| Tenant administrator | Changes membership inside one tenant | Authorized only for stated administrative actions |
| Application operator | Reads selected logs and performs restore operations | Privileged; not automatically trusted for every asset |
| API policy path | Resolves subject, object, action, and tenant before access | Intended trusted computing base; later modules test this assumption |
| PostgreSQL persistence path | Stores notes, membership, and audit records | Intended trusted computing base; backups and roles require later analysis |

Do not write “the backend is trusted” if only one policy decision needs trust. Trust is a dependency to minimize and later verify.

### State and time

Model at least four moments:

1. before a request, when membership and note ownership already exist;
2. during a request, when identity and authorization are evaluated;
3. after a state change, when audit evidence and caches may persist;
4. after deletion, export, or restore, when old copies may reappear.

A request-time test cannot prove a retention-time property.

## Catalogue record

Create a file named invariants-v1.md or an equivalent structured artifact. Each row should contain:

| Field | Required reasoning |
|---|---|
| ID and property name | Stable identifier such as SC-CONF-01 and a named property |
| Property | Subject, action, object, allowed condition, and forbidden outcome |
| Assets | Specific records or effects protected |
| Attacker | Capabilities, access already held, and channels controlled |
| Trust | Smallest components or people whose correct behavior the claim depends on |
| Time horizon | Request, session, retention, backup, restore, or incident interval |
| Preconditions | State that must exist before the failure is possible |
| Supporting mechanisms | Candidate controls, explicitly labeled as mechanisms |
| Mechanism limits | Where those controls do not enforce the property |
| Evidence | Normal, negative, abuse, and failure evidence |
| Detection and recovery | What remains true when prevention fails |
| Residual risk and non-goals | Risk accepted now and the reason |
| Review triggers | Product or assumption changes that invalidate the row |

## Guided example: scope a confidentiality row

Begin with a weak line:

> Tenant data is confidential.

Interrogate it.

- **Which data?** Note bodies, note titles, membership, and audit metadata have different exposure and retention.
- **Against whom?** A Tenant B member is different from a cloud administrator with snapshot access.
- **Through which paths?** API responses, application logs, exports, backups, browser caches, and notifications are separate paths.
- **For how long?** Deletion from the live table does not delete a retained backup.
- **What disproves it?** Name a response, log event, or restored record that would violate the row.

A bounded Phase 1 row might cover cross-tenant API responses and application logs, while recording cloud snapshot access as residual risk for the later data and key-lifecycle modules. The narrower claim is more honest and more useful than “confidential forever.”

Do not copy that row unchanged. Choose the channels and assumptions you can justify from your model.

## Model dependencies, not isolated labels

Properties can conflict:

- Accountability may require event evidence; privacy limits what that evidence contains and how long it remains.
- Availability may favor caching or replication; confidentiality and deletion requirements constrain copies.
- Recovery may require a powerful operator path; authorization and accountability constrain that path.
- Safety and usable recovery may reject a control that technically denies every suspicious request.

Add a dependency note to at least two rows. A catalogue is not eight independent checkboxes.

## Required learner artifact

Produce at least five system-specific rows and cover the following shapes:

1. a cross-tenant disclosure property;
2. an authorized state-change/integrity property;
3. an accountability property that does not log note bodies or credentials;
4. an availability or recovery property with a bounded objective;
5. a privacy or safety property that changes what another row may do.

For every row:

- name a hostile or failure capability;
- identify trusted and untrusted components;
- state a time horizon;
- name at least one forbidden outcome;
- separate mechanisms from the property;
- propose evidence;
- state residual risk or a non-goal.

Also include a short product-scope section and a review-trigger section for files, sharing, workers, support, and offline clients.

## Peer review protocol

Exchange catalogues with a peer. For each row, the reviewer asks:

1. Can I construct a concrete forbidden counterexample?
2. Is that counterexample inside the stated attacker, channel, and time horizon?
3. Does the evidence observe the property, or merely the presence of a mechanism?
4. Is a trusted component doing more work than the row admits?
5. Would one listed product change invalidate the claim?

Label the row **testable**, **underspecified**, **mechanism-only**, or **out-of-scope but explicit**. Rewrite every underspecified or mechanism-only row.

## A useful stopping condition

The catalogue is ready for this module when another person can challenge every row without asking what “secure,” “proper,” “sensitive,” “authorized,” or “always” means. It is not finished for the life of the product; review triggers make that impossible by design.
